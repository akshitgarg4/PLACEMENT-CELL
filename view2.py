#!C:/Users/AKSHIT/AppData/Local/Programs/Python/Python37-32/python
import cgi
import pymysql
print("Content-type:text/html\r\n\r\n")
fi=cgi.FieldStorage()
cid=fi.getvalue("cid")
cp=fi.getvalue("cp")


db=pymysql.connect("localhost","root","","placementcell")
cur=db.cursor()
q="select * from company where companyid='%s' and password ='%s' "%(cid,cp)
cur.execute(q)
res=cur.fetchall()
if res=={}:
    print("Company ID or Password is incorrect")
else:
    for row in res:
        
        ci=row[0]
        n=row[1]
        e=row[2]
        c=row[3]
        t=row[4]
        cg=row[5]
        ad=row[6]
        pas=row[7]
        print(" COMPANY ID '%s'  NAME '%s' EMAIL '%s' CONTACT %d TWELTH PERCENTAGE '%s' CGPA '%S' D.O.B '%s' PASSWORD '%s'"%(ci,n,e,c,t,cg,ad,pas))

