import sqlite3 as sq
import csv
conn=sq.connect("c://student.db")
cur=conn.cursor()
cur.execute(" " "create table if not exists result(sid int primary key,sname text, sub_1 int,sub_2 int,sub_3 int,sub_4 int,sub_5 int)""")
put="insert into result values(?,?,?,?,?,?,?)"
record=[]
for i in range(2):
    no=int(input("Enter student id:"))
    sn=input("Enter student name:")
    sub1=int(input("Enter subject 1 marks:"))
    sub2=int(input("Enter subject 2 marks:"))
    sub3=int(input("Enter subject 3 marks:"))
    sub4=int(input("Enter subject 4 marks:"))
    sub5=int(input("Enter subject 5 marks:"))
    li=[no,sn,sub1,sub2,sub3,sub4,sub5]
    record.append(li)
    cur.executemany(put,record)
#dump table in csv
cur.execute('select * from result;')
r=cur.fetchall()
conn.commit()
h=['sid','sname','sub_1','sub_2','sub_3','sub_4','sub_5']
with open("c:\\sqlite3\\csv\\result.csv","w",newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(h)
    writer.writerows(r)
#add total and percentage colunms
i=0
add=[]
with open("c:\\result.csv","r") as csvfile:
    read = csv.reader(csvfile)
    header=next(read)
    for row in read:
        i=i+1
        print("Record{}:".format(i))
        print("id:",row[0])
        print("name:",row[1])
        print("sub_1:",row[2])
        print("sub_2:",row[3])
        print("sub_3:",row[4])
        print("sub_4:",row[5])
        print("sub_5:",row[6])
        row.append(int(row[2])+int(row[3])+int(row[4])+int(row[5])+int(row[6]))
        row.append(row[7]/5)
        print("Total marks:",row[7])
        print("percentage:",row[8])
        if records[8]>80:    #Based on condition grade is assigned
                records.append('Distinction')
        elif records[8]>65 and records[8]<=80:
                records.append('First Class')
        elif records[8]>50 and records[8]<=65:
                records.append('Second Class')
        elif records[8]>35 and records[8]<=50:
                records.append('Pass')
        else:
                records.append('Fail')
        print("grade:",row[9])
        add.append(row)
with open("c:\\result.csv","w") as f1:
    write=csv.writer(f1)
    h.extend(('total','percentage','grade'))
    write.writerow(h)
    write.write.rows(add)
#print top 3 student
with open("c:\\result.csv","r") as csvfile:
        read_obj=csv.reader(csvfile)
        read=list(read_obj)
        i=0
        L=[]
        for row in read:
            L.append(row[8])  
        L.pop(0)
        L.sort(reverse=True)     
        for per in L[:3]:        
            for list in read :
                if per in list:       
                    i=i+1
                    print("Top:",i)
                    print("ID:",list[0])
                    print("Name:",list[1])
                    print("Total:",list[7])
                    print("Percentage:",list[8])
