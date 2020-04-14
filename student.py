#!C:/Users/AKSHIT/AppData/Local/Programs/Python/Python37-32/python
import cgi
import pymysql
print("Content-type:text/html\r\n\r\n")
fi=cgi.FieldStorage()
f=fi.getvalue("f")
s=fi.getvalue("s")
e=fi.getvalue("e")
c=int(fi.getvalue("c"))
t=fi.getvalue("t")
cg=fi.getvalue("cg")
d=fi.getvalue("d")
p=fi.getvalue("p")

db=pymysql.connect("localhost","root","","placementcell")
cur=db.cursor()
q="insert into student(name,sid,email,contact,twelth,cgpa,dob,password)values('%s','%s','%s',%d,'%s','%s','%s','%s')"%(f,s,e,c,t,cg,d,p)
cur.execute(q)
db.commit()
print("SUCCESSFULLY REGISTERED")
