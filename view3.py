#!C:/Users/AKSHIT/AppData/Local/Programs/Python/Python37-32/python
import cgi
import pymysql
print("Content-type:text/html\r\n\r\n")
fi=cgi.FieldStorage()
sid=fi.getvalue("sid")
n=fi.getvalue("n")
pa=fi.getvalue("pa")
db=pymysql.connect("localhost","root","","placementcell")
cur=db.cursor()
q="select * from student where sid='%s' and name='%s' and  password ='%s' "%(sid,n,pa)
cur.execute(q)
res=cur.fetchall()
if res=={}:
    print("sid or name or password is incorrect")
else:
    cu=db.cursor()
    x="select c.companyid,c.name,c.email,c.contact from student s,company c where s.sid=%d and s.name='%s' and c.twelth<=s.twelth and c.cgpa<=s.cgpa"%(sid,n)
    cu.execute(x)
    re=cu.fetchall()
    print(re)
        

