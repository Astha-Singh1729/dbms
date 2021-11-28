#Frontend

from tkinter import *
import tkinter.messagebox
import MiniProject_Backend

MiniProject_Backend.MovieData()
class Movie:
	def __init__(self, root):
		self.root=root
		self.root.title("Online Movie Ticket Booking System")
		self.root.geometry("1350x750+0+0")
		self.root.config(bg="#151D31")

		Movie_Name=StringVar()
		Movie_ID=StringVar()
		Release_Date=StringVar()
		Director=StringVar()
		Cast=StringVar()
		Budget=StringVar()
		Duration=StringVar()
		Rating=StringVar()

		#Fuctions
		def iExit():
			iExit=tkinter.messagebox.askyesno("Online Movie Ticket Booking System", "Are you sure???")
			if iExit>0:
				root.destroy()
			return

		def clcdata():
			self.txtMovie_ID.delete(0,END)
			self.txtMovie_Name.delete(0,END)
			self.txtRelease_Date.delete(0,END)
			self.txtDirector.delete(0,END)
			self.txtCast.delete(0,END)
			self.txtBudget.delete(0,END)
			self.txtRating.delete(0,END)
			self.txtDuration.delete(0,END)

		def adddata():
			if(len(Movie_ID.get())!=0):
				MiniProject_Backend.AddMovieRec(Movie_ID.get(),Movie_Name.get(),Release_Date.get(),Director.get(),Cast.get(),Budget.get(),Duration.get(),Rating.get())
				MovieList.delete(0,END)
				MovieList.insert(END,(Movie_ID.get(),Movie_Name.get(),Release_Date.get(),Director.get(),Cast.get(),Budget.get(),Duration.get(),Rating.get()))

		def disdata():
			MovieList.delete(0,END)
			for row in MiniProject_Backend.ViewMovieData():
				MovieList.insert(END, row, str(""))

		def movierec(event):
			global sd
			searchmovie=MovieList.curselection()[0]
			sd=MovieList.get(searchmovie)

			self.txtMovie_ID.delete(0,END)
			self.txtMovie_ID.insert(END,sd[0])
			self.txtMovie_Name.delete(0,END)
			self.txtMovie_Name.insert(END,sd[1])
			self.txtRelease_Date.delete(0,END)
			self.txtRelease_Date.insert(END,sd[2])
			self.txtDirector.delete(0,END)
			self.txtDirector.insert(END,sd[3])
			self.txtCast.delete(0,END)
			self.txtCast.insert(END,sd[4])
			self.txtBudget.delete(0,END)
			self.txtBudget.insert(END,sd[5])
			self.txtDuration.delete(0,END)
			self.txtDuration.insert(END,sd[6])
			self.txtRating.delete(0,END)
			self.txtRating.insert(END,sd[7])

		def deldata():
			if(len(Movie_ID.get())!=0):
				MiniProject_Backend.DeleteMovieRec(sd[0])
				clcdata()
				disdata()

		def searchdb():
			MovieList.delete(0,END)
			for row in MiniProject_Backend.SearchMovieData(Movie_ID.get(),Movie_Name.get(),Release_Date.get(),Director.get(),Cast.get(),Budget.get(),Duration.get(),Rating.get()):
				MovieList.insert(END, row, str(""))

		def updata():
			if(len(Movie_ID.get())!=0):
				MiniProject_Backend.DeleteMovieRec(sd[0])
			if(len(Movie_ID.get())!=0):
				MiniProject_Backend.AddMovieRec(Movie_ID.get(),Movie_Name.get(),Release_Date.get(),Director.get(),Cast.get(),Budget.get(),Duration.get(),Rating.get())
				MovieList.delete(0,END)
				MovieList.insert(END,(Movie_ID.get(),Movie_Name.get(),Release_Date.get(),Director.get(),Cast.get(),Budget.get(),Duration.get(),Rating.get()))

		#Frames
		MainFrame=Frame(self.root, bg="#151D31")
		MainFrame.grid()

		TFrame=Frame(MainFrame, bd=5, padx=54, pady=8, bg="#151D31", relief=RIDGE)
		TFrame.pack(side=TOP)

		self.TFrame=Label(TFrame, font=('Road Rage', 51, 'bold'), text="ONLINE MOVIE TICKET BOOKING SYSTEM", bg="#151D31", fg="#E6DDC4")
		self.TFrame.grid()

		BFrame=Frame(MainFrame, bd=2, width=1350, height=70, padx=15, pady=10, bg="#151D31", relief=RIDGE)
		BFrame.pack(side=BOTTOM)

		DFrame=Frame(MainFrame, bd=2, width=1300, height=400, padx=20, pady=20, bg="#151D31", relief=RIDGE)
		DFrame.pack(side=BOTTOM)

		DFrameL=LabelFrame(DFrame, bd=2, width=1000, height=600, padx=20, bg="#151D31", relief=RIDGE, font=('Road Rage', 20, 'bold'), text="Movie Info_\n", fg="#F0E9D2")
		DFrameL.pack(side=LEFT)

		DFrameR=LabelFrame(DFrame, bd=2, width=450, height=300, padx=31, pady=3, bg="#151D31", relief=RIDGE, font=('Road Rage', 20, 'bold'), text="Movie Details_\n", fg="#F0E9D2")
		DFrameR.pack(side=RIGHT)

		#Labels & Entry Box

		self.lblMovie_ID=Label(DFrameL, font=('Road Rage', 15, 'bold'), text="Movie ID:", padx=2, pady=2, bg="#151D31", fg="#E6DDC4")
		self.lblMovie_ID.grid(row=0, column=0, sticky=W)
		self.txtMovie_ID=Entry(DFrameL, font=('Road Rage', 15, 'bold'), textvariable=Movie_ID, width=39, bg="#151D31", fg="#F0E9D2")
		self.txtMovie_ID.grid(row=0, column=1)

		self.lblMovie_Name=Label(DFrameL, font=('Road Rage', 15, 'bold'), text="Movie Name:", padx=2, pady=2, bg="#151D31", fg="#E6DDC4")
		self.lblMovie_Name.grid(row=1, column=0, sticky=W)
		self.txtMovie_Name=Entry(DFrameL, font=('Road Rage', 15, 'bold'), textvariable=Movie_Name, width=39, bg="#151D31", fg="#F0E9D2")
		self.txtMovie_Name.grid(row=1, column=1)

		self.lblRelease_Date=Label(DFrameL, font=('Road Rage', 15, 'bold'), text="Release Date:", padx=2, pady=2, bg="#151D31", fg="#E6DDC4")
		self.lblRelease_Date.grid(row=2, column=0, sticky=W)
		self.txtRelease_Date=Entry(DFrameL, font=('Road Rage', 15, 'bold'), textvariable=Release_Date, width=39, bg="#151D31", fg="#F0E9D2")
		self.txtRelease_Date.grid(row=2, column=1)

		self.lblDirector=Label(DFrameL, font=('Road Rage', 15, 'bold'), text="Director:", padx=2, pady=2, bg="#151D31", fg="#E6DDC4")
		self.lblDirector.grid(row=3, column=0, sticky=W)
		self.txtDirector=Entry(DFrameL, font=('Road Rage', 15, 'bold'), textvariable=Director, width=39, bg="#151D31", fg="#F0E9D2")
		self.txtDirector.grid(row=3, column=1)

		self.lblCast=Label(DFrameL, font=('Road Rage', 15, 'bold'), text="Cast:", padx=2, pady=2, bg="#151D31", fg="#E6DDC4")
		self.lblCast.grid(row=4, column=0, sticky=W)
		self.txtCast=Entry(DFrameL, font=('Road Rage', 15, 'bold'), textvariable=Cast, width=39, bg="#151D31", fg="#F0E9D2")
		self.txtCast.grid(row=4, column=1)

		self.lblBudget=Label(DFrameL, font=('Road Rage', 15, 'bold'), text="Budget (Crores INR):", padx=2, pady=2, bg="#151D31", fg="#E6DDC4")
		self.lblBudget.grid(row=5, column=0, sticky=W)
		self.txtBudget=Entry(DFrameL, font=('Road Rage', 15, 'bold'), textvariable=Budget, width=39, bg="#151D31", fg="#F0E9D2")
		self.txtBudget.grid(row=5, column=1)

		self.lblDuration=Label(DFrameL, font=('Road Rage', 15, 'bold'), text="Duration (Hrs):", padx=2, pady=2, bg="#151D31", fg="#E6DDC4")
		self.lblDuration.grid(row=6, column=0, sticky=W)
		self.txtDuration=Entry(DFrameL, font=('Road Rage', 15, 'bold'), textvariable=Duration, width=39, bg="#151D31", fg="#F0E9D2")
		self.txtDuration.grid(row=6, column=1)

		self.lblRating=Label(DFrameL, font=('Road Rage', 15, 'bold'), text="Rating (Out of 5):", padx=2, pady=2, bg="#151D31", fg="#E6DDC4")
		self.lblRating.grid(row=7, column=0, sticky=W)
		self.txtRating=Entry(DFrameL, font=('Road Rage', 15, 'bold'), textvariable=Rating, width=39, bg="#151D31", fg="#F0E9D2")
		self.txtRating.grid(row=7, column=1)

		#ListBox & ScrollBar
		sb=Scrollbar(DFrameR)
		sb.grid(row=0, column=1, sticky='ns')

		MovieList=Listbox(DFrameR, width=38, height=16, font=('Road Rage', 12, 'bold'), bg="#151D31", fg="#F0E9D2", yscrollcommand=sb.set)
		MovieList.bind('<<ListboxSelect>>', movierec)
		MovieList.grid(row=0, column=0, padx=8)
		sb.config(command=MovieList.yview)

		#Buttons
		self.btnadd=Button(BFrame, text="Add New", font=('Road Rage', 20, 'bold'), width=10, height=1, bd=4, bg="#E6DDC4", command=adddata)
		self.btnadd.grid(row=0, column=0)

		self.btndis=Button(BFrame, text="Display", font=('Road Rage', 20, 'bold'), width=10, height=1, bd=4, bg="#E6DDC4", command=disdata)
		self.btndis.grid(row=0, column=1)

		self.btnclc=Button(BFrame, text="Clear", font=('Road Rage', 20, 'bold'), width=10, height=1, bd=4, bg="#E6DDC4", command=clcdata)
		self.btnclc.grid(row=0, column=2)

		self.btnse=Button(BFrame, text="Search", font=('Road Rage', 20, 'bold'), width=10, height=1, bd=4, bg="#E6DDC4", command=searchdb)
		self.btnse.grid(row=0, column=3)

		self.btndel=Button(BFrame, text="Delete", font=('Road Rage', 20, 'bold'), width=10, height=1, bd=4, bg="#E6DDC4", command=deldata)
		self.btndel.grid(row=0, column=4)

		self.btnup=Button(BFrame, text="Update", font=('Road Rage', 20, 'bold'), width=10, height=1, bd=4, bg="#E6DDC4", command=updata)
		self.btnup.grid(row=0, column=5)

		self.btnx=Button(BFrame, text="Exit", font=('Road Rage', 20, 'bold'), width=10, height=1, bd=4, bg="#E6DDC4", command=iExit)
		self.btnx.grid(row=0, column=6)


if __name__=='__main__':
	root=Tk()
	datbase=Movie(root)
	root.mainloop()