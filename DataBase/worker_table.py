import mysql.connector as connection
class DB_Helper:
    def __init__(self):
        try:
     
            self.con = connection.connect(host="localhost",
                                         username = "root",
                                         password = "Arzoo@6552",
                                         database = 'myorg'
                                         )
            print("Database Connected...")
        except Exception as e:
            print(e)
    def create_table(self,query):
        try:
            self.query = query
            cur = self.con.cursor()
            cur.execute(query)
            print("Table Ceated....")
        except Exception as e:
            print(e)
    
    def insert_data_worker(self,worker_id,first_name,last_name,salary,joining_date,department):
        try:
            query = '''insert into worker(worker_id,first_name,last_name,salary,joining_date,department) values({} ,'{}', 
                                        '{}',{} ,'{}', '{}')'''.format(worker_id,first_name,last_name,salary,joining_date,department)

    #         print(query)
            cur  =  self.con.cursor()
            cur.execute(query)
            self.con.commit()
            print("Data Inserted into Worker Table......")
        except Exception as e:
            print(e)

    def insert_data_bonus(self,worker_ref_id,bonus_amount,bonus_date):
        try:
            query = ''' insert into bonus(worker_ref_id,bonus_amount,bonus_data) values({} , {}, '{}')'''.format(worker_ref_id,bonus_amount,bonus_date)
            cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
            print("Data Inserted into Bonus Table....")
        except Exception as e:
            print(e)
        
    def insert_data_title(self,worker_ref_id,worker_title,affected_from):
        try:
            query = ''' insert into title(worker_ref_id,worker_title,affected_from) values( {} , '{}','{}')'''.format(worker_ref_id,worker_title,affected_from)
            cur = self.con.cursor(query)
            cur.execute(query)
            self.con.commit()
            print("Data Inserted into Title table....")
        except Exception as e:
            print(e)


        
#create sample worker table           
# query = '''create table if not exists worker(worker_id int primary key,
#                                     first_name varchar(25) ,
#                                     last_name varchar(25),
#                                     salary int(10) , 
#                                     joining_date datetime, 
#                                     department varchar(25))'''  
#create sample bonus table
# query = ''' create table if not exists bonus(worker_ref_id int , bonus_amount int(10),bonus_data datetime , foreign key(worker_ref_id) references worker(worker_id) on delete cascade)
#             '''

#create  sample title table
query = ''' create table if not exists title(worker_ref_id int, worker_title varchar(15) , affected_from datetime, foreign key(worker_ref_id) references worker(worker_id) on delete cascade)
        '''

db = DB_Helper()
db.create_table(query)

#inserting the data into the worket table

# db.insert_data_worker("%03d" % (1,), 'Monika', 'Arora', 100000, '14-02-20 09.00.00', 'HR')
# db.insert_data_worker("%03d" % (2,),'Niharika', 'Verma', 80000, '2014-06-11 09.00.00', 'Admin')
# db.insert_data_worker("%03d" % (3,), 'Vishal', 'Singhal', 300000, '14-02-20 09.00.00', 'HR')
# db.insert_data_worker("%03d" % (4,), 'Amitabh', 'Singh', 500000, '14-02-20 09.00.00', 'Admin')
# db.insert_data_worker("%03d" % (5,), 'Vivek', 'Bhati', 500000, '14-06-11 09.00.00', 'Admin')
# db.insert_data_worker("%03d" % (6,), 'Vipul', 'Diwan', 200000, '14-06-11 09.00.00', 'Account')
# db.insert_data_worker("%03d" % (7,), 'Satish', 'Kumar', 75000, '14-01-20 09.00.00', 'Account')
# db.insert_data_worker("%03d" % (8,), 'Geetika', 'Chauhan', 90000, '14-04-11 09.00.00', 'Admin')

#inserting the data into bonus table

# db.insert_data_bonus("%03d" % (1,), 5000, '16-02-20')
# db.insert_data_bonus("%03d" % (2,), 3000, '16-06-11')
# db.insert_data_bonus("%03d" % (3,), 4000, '16-02-20')
# db.insert_data_bonus("%03d" % (1,), 4500, '16-02-20')
# db.insert_data_bonus("%03d" % (2,), 3500, '16-06-11')

#inserting the data into the title table

# db.insert_data_title("%03d" % (1,), 'Manager', '2016-02-20 00:00:00')
# db.insert_data_title("%03d" % (2,), 'Executive', '2016-06-11 00:00:00')
# db.insert_data_title("%03d" % (8,), 'Executive', '2016-06-11 00:00:00')
# db.insert_data_title("%03d" % (5,), 'Manager', '2016-06-11 00:00:00')
# db.insert_data_title("%03d" % (4,), 'Asst. Manager', '2016-06-11 00:00:00')
# db.insert_data_title("%03d" % (7,), 'Executive', '2016-06-11 00:00:00')
# db.insert_data_title("%03d" % (6,), 'Lead', '2016-06-11 00:00:00')
# db.insert_data_title("%03d" % (3,), 'Lead', '2016-06-11 00:00:00')

class SQL_Query(DB_Helper):
    def quest(self,query):
        try:
            cur = db.con.cursor()
            cur.execute(query)
            print("\nShowing the result: \n")
            for i in cur:
                print(i)
        except Exception as e:
            print(e)
