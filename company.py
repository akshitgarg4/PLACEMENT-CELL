#!C:/Users/AKSHIT/AppData/Local/Programs/Python/Python37-32/python
import cgi
import pymysql
print("Content-type:text/html\r\n\r\n")
fi=cgi.FieldStorage()
cid=fi.getvalue("f")
n=fi.getvalue("s")
e=fi.getvalue("e")
c=int(fi.getvalue("c"))
t=fi.getvalue("t")
cg=fi.getvalue("cg")
a=fi.getvalue("d")
p=fi.getvalue("p")

db=pymysql.connect("localhost","root","","placementcell")
cur=db.cursor()
q="insert into company(companyid,name,email,contact,twelth,cgpa,address,password)values('%s','%s','%s',%d,'%s','%s','%s','%s')"%(cid,n,e,c,t,cg,a,p)
cur.execute(q)
db.commit()
print("SUCCESSFULLY REGISTERED")
