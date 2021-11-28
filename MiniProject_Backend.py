# backend
import sqlite3
import traceback
import sys


def MovieData():
    con = sqlite3.connect("movie1.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, Movie_ID text,Movie_Name text,Release_Date text,Director text,Cast text,Budget text,Duration text,Rating text)")
    con.commit()
    con.close()


def AddMovieRec(Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating):
    con = sqlite3.connect("movie1.db")
    cur = con.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?, ?,?,?,?,?,?,?)", (Movie_ID,
                                                                    Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating))
    con.commit()
    con.close()


def ViewMovieData():
    con = sqlite3.connect("movie1.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    con.close()
    rows2 = [x[1:] for x in rows]
    return rows2


def DeleteMovieRec(id):
    con = sqlite3.connect("movie1.db")
    cur = con.cursor()
    cur.execute("DELETE FROM book WHERE Movie_ID=?", (str(id)))
    con.commit()
    con.close()


def SearchMovieData(Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating):
    con = sqlite3.connect("movie1.db")
    con.set_trace_callback(print)
    cur = con.cursor()
    sql = "SELECT * FROM book WHERE (Movie_ID=%s OR Movie_Name=%s OR Release_Date=%s OR Director=%s OR Budget=%s OR Duration=%s OR Rating=%s)"
    cur.execute((sql),
            (Movie_ID or 'XXX', Movie_Name or 'XXX', Release_Date or 'XXX', Director or 'XXX', Budget or 'XXX', Duration or 'XXX', Rating or 'XXX',))
    rows = cur.fetchall()
    con.close()
    rows2 = [x[1:] for x in rows]
    return rows2


def UpdateMovieData(id, Movie_ID="", Movie_Name="", Release_Date="", Director="", Cast="", Budget="", Duration="", Rating=""):
    con = sqlite3.connect("movie1.db")
    cur = con.cursor()
    cur.execute("UPDATE book SET Movie_ID=?,Movie_Name=?,Release_Date=?,Director=?,Cast=?,Budget=?,Duration=?,Rating=?, WHERE id=?",
                (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating))
    con.commit()
    con.close()
