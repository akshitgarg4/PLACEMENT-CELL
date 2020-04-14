#!C:/Users/AKSHIT/AppData/Local/Programs/Python/Python37-32/python
import cgi
import pymysql
print("Content-type:text/html\r\n\r\n")
fi=cgi.FieldStorage()
s=fi.getvalue("s")
p=fi.getvalue("p")


db=pymysql.connect("localhost","root","","placementcell")
cur=db.cursor()
q="select * from student where sid='%s' and password ='%s' "%(s,p)
cur.execute(q)
res=cur.fetchall()
if res=={}:
    print("sid or password is incorrect")
else:
    for row in res:
        n=row[0]
        si=row[1]
        e=row[2]
        c=row[3]
        t=row[4]
        cg=row[5]
        d=row[6]
        pas=row[7]
        print("NAME '%s' SID %d EMAIL '%s' CONTACT %d TWELTH PERCENTAGE '%s' CGPA '%s' D.O.B '%s' PASSWORD '%s'"%(n,si,e,c,t,cg,d,pas))
