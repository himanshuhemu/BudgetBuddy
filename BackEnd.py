import sqlite3
db_con = sqlite3.connect("dat.db")
db_cursor = db_con.cursor() 

def add(name, amnt , date ,typ):
    if typ:
        db_cursor.execute("CREATE TABLE IF NOT EXISTS EXPENSE(NAME TEXT , AMNT NUMBER , DATE DATE )")
        db_cursor.execute("INSERT INTO EXPENSE(NAME, AMNT ,DATE) values(?,?,?)",(name,amnt,date))
    else:
        db_cursor.execute("CREATE TABLE IF NOT EXISTS INCOME(NAME TEXT , AMNT NUMBER , DATE DATE )")
        db_cursor.execute("INSERT INTO INCOME (NAME, AMNT,DATE) values(?,?,?)",(name,amnt,date))
    db_con.commit()
def find(name,db_name):
        sumItem=0    
        val=db_cursor.execute("select AMNT from "+db_name+" where NAME = "+name).fetchall()
        val1=[x[0] for x in val]
        for item in val1:
             sumItem +=item
        print(sumItem)
        return sumItem

        
def disp1(sdate,edate):
         sumItem=0
         val=db_cursor.execute("SELECT  AMNT FROM dated_view where DATE >= "+sdate+" AND DATE <= "+edate).fetchall()
         val=[x[0] for x in val]
         for item in val:
             sumItem +=item
         print(sumItem)
         return sumItem

def createView(sdate,edate):
        try:
        ##creating view
            db_cursor.execute("CREATE VIEW dated_view  AS SELECT * FROM EXPENSE where DATE >= "+sdate+" AND DATE <= "+edate)
            #search of total expense in these dates 
            an=disp1(sdate,edate)
            db_cursor.execute("DROP VIEW dated_view")
        except IOError:
            #handle
            print("error")  
                
        return an

def createView1(sdate,edate,item):
        try:    
            ##creating view
            db_cursor.execute("CREATE VIEW dated_view AS SELECT * FROM EXPENSE where DATE >= "+sdate+" AND DATE <= "+edate)
            #search of total expense in these dates 
            an1=find(item,'dated_view')
            db_cursor.execute("DROP VIEW dated_view")
        except IOError:
            #handle
            print("error")    
         
        return an1 
##################################
def report(sdate,edate):
        try:
        ##creating view
            db_cursor.execute("CREATE VIEW dated_view  AS SELECT * FROM EXPENSE where DATE >= "+sdate+" AND DATE <= "+edate)
            #generating the report in these dates 
            #fn call
            nval=db_cursor.execute("SELECT  * FROM dated_view where DATE >= "+sdate+" AND DATE <= "+edate).fetchall()
            msg="Success"
            db_cursor.execute("DROP VIEW dated_view")
        except IOError:
            #handle
            msg="Error"        
                
        return nval, msg
 
def reportView(sdate,edate):
            val=db_cursor.execute("SELECT  * FROM dated_view where DATE >= "+sdate+" AND DATE <= "+edate).fetchall()
            return val
                    
#report("'2018-08-01'","'2018-08-05'")
###########################

def check(amount,date):
        try:
          sumItem=0
          ndiff=0
          amount=int(amount)  
          ndt=date.split('-')
          mdate=ndt[1]
          ydate=ndt[0]
          sdate="'"+ydate+"-"+mdate+"-"+"01"+"'"
          edate="'"+ydate+"-"+mdate+"-"+"31"+"'"
          val=db_cursor.execute("SELECT  AMNT FROM INCOME where DATE >= "+sdate+" AND DATE <= "+edate).fetchall()
          val_=[x[0] for x in val]
          for item in val_:
             sumItem +=item
 
          val1=db_cursor.execute("SELECT  AMNT FROM EXPENSE where DATE >= "+sdate+" AND DATE <= "+edate).fetchall() 
          sumItem1=0
          val_1=[x[0] for x in val1]
          for item1 in val_1:
              sumItem1 +=item1
          #print(sumItem1)
          msg="Success"
          diff=sumItem-sumItem1
          ndiff=diff-amount
          if ndiff>0:
              return True,ndiff,msg
          else:
              return False,ndiff,msg
        except ValueError:
           msg="Error"
           return False,ndiff,msg
          
            
import xlsxwriter

# Create a workbook and add a worksheet.
def func(expenses):
    workbook = xlsxwriter.Workbook('Report.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.set_column('A:D', 12)
    # Write the caption.
    
    # Add a table to the worksheet.
    worksheet.add_table('A1:D10', {'data': expenses,
                                   'columns': [{'header': 'Name'},
                                               {'header': 'Amount'},
                                               {'header': 'Date'},
                                               ]})
    
    # Some data we want to write to the worksheet.
    
    # Start from the first cell. Rows and columns are zero indexed.
    row = 1
    col = 0
    add=0
    # Iterate over the data and write it out row by row.
    for item, cost , date in (expenses):
        worksheet.write(row, col,     item)
        worksheet.write(row, col + 1, cost)
        worksheet.write(row, col + 2, date)
        add+=cost
        row += 1

    # Write a total using a formula.
    worksheet.write(row, 0, 'Total')
    worksheet.write(row, 1 , add)
    workbook.close()

    
          

db_con.commit()
'''
#generating full report 
db_cursor.execute("select * from EXPENSE")
print(db_cursor.fetchall())

           
#checking whether the amount user trying to add is not more than the salary in that month 

check(659,'2018-08-15')          

createView("'2018-08-01'","'2018-08-05'")
#db_cursor.execute("select *from dated_view").fetchall()
add("food",100,'2018-08-01',typ=True)
add("food",1200,'2018-08-02',typ=True)
add("invest",300,'2018-08-03',typ=True)
add("invest",400,'2018-08-04',typ=True)
add("invest",100,'2018-08-05',typ=True)


find("'transport'",'EXPENSE')
db_con.commit()       
'''