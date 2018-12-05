# cunk is GB con (connect to the database and give it a name)
# crsr01 is GB cur (cursor defined and instantiated)
# kenect is GB connect or konect
# doctran.db is name of database in sqlite3
# doc_data_tbl is name of first table in database
# fields in first table : id, when,dlrs,who_store,pmt_kind

import sqlite3
def kenect():
    cunk=sqlite3.connect ("doctran.db")
    crsr01=cunk.cursor()
    crsr01.execute("CREATE TABLE IF NOT EXISTS doc_data_tbl (id INTEGER PRIMARY KEY, \
        wheen text, dlrs text, who_store text, pmt_kind text)")

    cunk.commit()
    cunk.close()
# ==30Nov18 :see vid Mr Garside YT_2
# == with squlite3.connect (quiz.db) as db:
#=======cursor-db.connect
#==end comment
def addrec(wheen,dlrs,who_store,pmt_kind):
    cunk=sqlite3.connect("doctran.db")
    crsr01=cunk.cursor()
#    wheen=wheen.rstrip()
#    dlrs=dlrs.rstrip()
#    who_store=who_store.restrip()
#    pmt_kind=pmt_kind.restrip()
    crsr01.execute ("INSERT INTO doc_data_tbl \
            VALUES(NULL,?,?,?,?)",(wheen,dlrs,who_store,pmt_kind))
# line below print is early version for printing back to command line
# remove or comment out later when running (good for test)
# GB code below has this line missing
#    print ("just put this in: " wheen,dlrs,who_store,pmt_kind)
    cunk.commit()
    cunk.close()
# GB shows the above cunk and cunk as indented as shown above
#========= execute the above command ftn =====
# ==== Phase Three : defining additional instructions to db called by frontend=
def view():
    cunk=sqlite3.connect("doctran.db")
    crsr01=cunk.cursor()
    crsr01.execute("SELECT * FROM doc_data_tbl")
    rows=crsr01.fetchall()
    cunk.close()
    return rows
# === the "return rows" returns the captured data to the "calling function"
# === above defines a new variable "rows" (could be any non-reserved word) ==
# === and passes that "loaded cursor (crsr01)" back to the front end cmd ftn that called this
# == backend ftn useing the "return" instruction ====
#=== end view ftn ===
# === begin findit functions ====== 17Nov18 tt ====
def findit(wheen="",dlrs="",who_store="",pmt_kind=""):
    cunk=sqlite3.connect("doctran.db")
    crsr01=cunk.cursor()
#    cur=conn.cursor()
#    print(mq1,ma1)
    crsr01.execute("SELECT * FROM doc_data_tbl WHERE WHEEN=? OR DLRS=? \
        OR WHO_STORE=? OR PMT_KIND=?",(wheen,dlrs,who_store,pmt_kind))
#    cur.execute("SELECT * FROM qtable WHERE q1=? or a1=?", (mq1, ma1,))
    rows=crsr01.fetchall()
    cunk.close()
    return rows
# === the "return rows" returns the captured data to the "calling function"
# ==== end findit command in back end file ===

# === copying dele cmd from below ====1615Nov18
# === working with backund updt secton 05Dec18 tt ===

def updt(id,fn="",ln="",dept="",sal=0):
    cunk=sqlite3.connect("doctran.db")
    crsr01=cunk.cursor()
#    conn=sqlite3.connect("emps.db")  ===GB code ==
#    cur=conn.cursor()  == GB cde ==
    crsr01.execute("UPDATE doc_data_tbl SET WHEEN=?, DLRS=?, WHO_STORE=?, PMT_KIND=? WHERE id=?", (wheen,dlrs,who_store,pmt_kind))
    cunk.commit()
    cunk.close()


def dele(id):
    cunk=sqlite3.connect("doctran.db")
    crsr01=cunk.cursor()
#    conn=sqlite3.connect("questions.db")
#    cur=conn.cursor()
#    crsr01.execute("SELECT * FROM doc_data_tbl")
#    cur.execute
    crsr01.execute("DELETE FROM doc_data_tbl WHERE id=?",(id,))
    cunk.commit()
    cunk.close()

# below kenect is the instruction to re-loop to top to begin reading down again=
kenect()
    # ====== above execute is isolated for clarity ====
"""
# =============GB code below commented out for study 15Nov18 12noon ======

#########   zbe.py  #########################
"""
"""
#===== tf say connect and addrec sections below are done 15Nov18 PHASE ONE===
import sqlite3

def connect():
    conn=sqlite3.connect("questions.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE \
        IF NOT EXISTS qtable \
        (id INTEGER PRIMARY KEY, \
        q1 text, a1 text)")
    conn.commit()
    conn.close()

def addrec(mq1,ma1):
    conn=sqlite3.connect("questions.db")
    cur=conn.cursor()
    mq1=mq1.rstrip()
    ma1=ma1.rstrip()
    cur.execute("INSERT INTO qtable VALUES(NULL,?,?)",(mq1,ma1,))
    conn.commit()
    conn.close()
#===== tf say connect and addrec sections above  are done 15Nov18 PHASE ONE===

def dele(mid):
    conn=sqlite3.connect("questions.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM qtable WHERE  id=?", (mid,))
    conn.commit()
    conn.close()

def updt(mid,mq1="",ma1=""):
    conn=sqlite3.connect("questions.db")
    cur=conn.cursor()
    mq1=mq1.rstrip()
    ma1=ma1.rstrip()
    cur.execute("UPDATE qtable SET q1=?, a1=? WHERE id=?", (mq1,ma1,mid,))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("questions.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM qtable")
    rows=cur.fetchall()
    conn.close()
    return rows

def findit(mq1="",ma1=""):
    conn=sqlite3.connect("questions.db")
    cur=conn.cursor()
    print(mq1,ma1)
    cur.execute("SELECT * FROM qtable WHERE q1=? or a1=?", (mq1, ma1,))
    rows=cur.fetchall()
    conn.close()
    return rows

#==================================
connect()
#==================================
"""
  