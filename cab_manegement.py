#Project
#Cab Management Application

#Using
    #Sqlite Database
    #List
    #Dictonary

#Modules
    #Cab Owner (Dealer) -> Reg,Manege Cab
    #Users -> Reg,Search Cab,Update Profile
    #Admin -> Manage Cab Owners,Users,Delete,Update

#Functions
    #init() -> For Showing Choices
    #dealreg() -> for get info (nm,pswd,email,phno) for reg
    #userreg() -> for get info (nm,pswd,email(unique),phno)
    #deallogin() ->login using credentials
                #addcab() -> add cab info(id,nm,from,to,etc) in db
                #viewcab()  -> view all cabs data from db
                #delcab() -> remove cab
                #updtcab() ->update cab info
    #userlogin()
                #viewcab() -> view all cabs
                #searchcab() -> serach cab info
                #updtprofile() -> update user pfofile


#----------------------------------------------------------------------------------------------

#database tables

#admin (admin_id,admin_username,admin_password)

#cab_dealers (cab_dealerid,cab_dealername,cabdealerpassword,cab_dealeremail,cab_dealerphone)

#cabs (cab_id,cab_number,cab_name,cab_type(4,7 seater),
#cab_model,cab_dealerid(for relation to cab_dealer table),cab_status)


#users (user_id,user_name,user_password,user_email,user_phone)


#----------------------------------------------------------------------------------------------

import sqlite3

conn=sqlite3.connect("cabsbooking.db")#creating and connection database
x=conn.cursor()#creating cursor object

global dealerid
global userid
global adminid

def createTable():
    try:
        ad='''CREATE TABLE admin(
                admin_id INTEGER PRIMARY KEY,
                admin_username VARCHAR(20) NOT NULL,
                admin_password VARCHAR(20) NOT NULL)'''
        x.execute(ad)

        cbd='''CREATE TABLE cab_dealers(
                cab_dealerid INTEGER PRIMARY KEY,
                cab_dealername VARCHAR(20) NOT NULL,
                cab_dealerpassword VARCHAR(20) NOT NULL,
                cab_dealeremail VARCHAR(20) NOT NULL,
                cab_dealerphone VARCHAR(20) NOT NULL)'''

        x.execute(cbd)

        cab='''CREATE TABLE cabs(
                cab_id INTEGER PRIMARY KEY,
                cab_name VARCHAR(20) NOT NULL,
                cab_type VARCHAR(20) NOT NULL,
                cab_model VARCHAR(20) NOT NULL,
                cab_dealerid INT(20) NOT NULL,
                cab_from VARCHAR(20) NOT NULL,
                cab_to VARCHAR(20) NOT NULL,
                cab_number VARCHAR(20) NOT NULL)'''

        x.execute(cab)

        usr='''CREATE TABLE users(
                user_id INTEGER PRIMARY KEY,
                user_name VARCHAR(20) NOT NULL,
                user_password VARCHAR(20) NOT NULL,
                user_email VARCHAR(20) NOT NULL,
                user_phone VARCHAR(20) NOT NULL)'''

        x.execute(usr)
        
        ad="INSERT INTO admin VALUES(1,'admin','admin')"

        x.execute(ad)
        
        print("Tables Are Created Successfully...!!")
    except Exception as z:
        print("Databse Error...",z)


#----------------------------------------------------------------------------------------------

def dealerReg():
    print("===========================Dealer Registration==========================")
    cab_dealername=input("Enter Cab Dealer Name : ")
    cab_dealerpassword=input("Enter Password : ")
    cab_dealeremail=input("Enter Email Id : ")
    cab_dealerphone=input("Entr Phone No. : ")
    
    dt=x.execute("SELECT * FROM cab_dealers where cab_dealeremail='"+cab_dealeremail+"'")
    if(len(dt.fetchall())==0):

        ins="INSERT INTO cab_dealers(cab_dealername,cab_dealerpassword,cab_dealeremail,cab_dealerphone)VALUES ('"+cab_dealername+"','"+cab_dealerpassword+"','"+cab_dealeremail+"','"+cab_dealerphone+"')"

##    ins=(f'''INSERT INTO cab_dealers(
##                cab_dealername,
##                cab_dealerpassword,
##                cab_dealeremail,
##                cab_dealerphone)
##                VALUES (
##                {cab_dealername},
##                {cab_dealerpassword},
##                {cab_dealeremail},
##                {cab_dealerphone})''')


        x.execute(ins)
        conn.commit()
        print("========================================================================")
        print("\nDealer Registered Successfully...!\n")
        init()
    else:
        print("========================================================================")
        print("\nDealer Email Alreday Exists...!\n")
        init()
    

def userReg():
    print("===========================User Registration============================")
    user_name=input("Enter Name : ")
    user_password=input("Enter Password : ")
    user_email=input("Enter Email : ")
    user_phone=input("Enter Phone No. : ")

    dt=x.execute("SELECT * FROM users where user_email='"+user_email+"'")
    if(len(dt.fetchall())==0):
        ins="INSERT INTO users (user_name,user_password,user_email,user_phone) VALUES ('"+user_name+"','"+user_password+"','"+user_email+"','"+user_phone+"')"
    
        x.execute(ins)
        conn.commit()
        print("========================================================================")
        print("User Registered Successfully...!")
        init()
    else:
        print("========================================================================")
        print("User Email Alreday Exists...!")
        init()

def dealInit():
    global dealerid
    print("============================Dealer Dashboard============================")
    print('''1).Add Cabs
2).View Cabs
3).Delete Cab
4).Update Cab
5).Logout''')
    print("========================================================================")
    ch=int(input("Enter Your Choice : "))

    if ch==1:
        addCab()
    elif ch==2:
        viewCabs()
    elif ch==3:
        delCab()
    elif ch==4:
        updtCab()
    elif ch==5:
        del dealerid
        print("Logout Successfully...!")
        init()
        
def dealerLogin():
    print("============================Dealer Login================================")
    global dealerid
    cab_dealername=input("Enter Name : ")
    cab_dealerpassword=input("Enter Password : ")
    dt=x.execute("SELECT * FROM cab_dealers WHERE cab_dealername='"+cab_dealername+"' and cab_dealerpassword='"+cab_dealerpassword+"'")
    d=dt.fetchall()
    for i in d:
        dealerid=i[0]
        
    if(len(d)!=0):
        print("========================================================================")
        print("\nLogin Successfully...!\n")
        dealInit()
        
    else:
        print("========================================================================")
        print("\nInvalid Username and Password...!\n")
        dealerLogin()

def addCab():
    print("=================================Add Cabs===============================")
    global dealerid
    cab_name=input("Enter Cab Name : ")
    cab_type=input("Enter Cab Type : ")
    cab_model=input("Enter Car Model : ")
    cab_dealerid=dealerid
    cab_from=input("Enter Cab From : ")
    cab_to=input("Enter Cab To : ")
    cab_number=input("Enter Cab No. : ")

    ins=f'''INSERT INTO cabs(
            cab_name,
            cab_type,
            cab_model,
            cab_dealerid,
            cab_from,
            cab_to,
            cab_number)
            VALUES(
            '{cab_name}',
            '{cab_type}',
            '{cab_model}',
            {cab_dealerid},
            '{cab_from}',
            '{cab_to}',
            '{cab_number}')'''

    x.execute(ins)
    conn.commit()
    print("========================================================================")
    print("\nCab Added Successfully....!\n")
    dealInit()
    
def viewCabs():
    print("================================All Cabs================================\n")
    global dealerid
    se=f"SELECT c.cab_id,c.cab_name,c.cab_type,c.cab_model,d.cab_dealername,c.cab_from,c.cab_to,c.cab_number FROM cabs c inner join cab_dealers d ON c.cab_dealerid='"+str(dealerid)+"'"
    d=x.execute(se)
    data=d.fetchall()
    print('''{0:<10} {1:<10} {2:<10} {3:<10} {4:<20} {5:<10} {6:<10}'''
            .format("Cab Id","Cab Name",
                    "Cab Type","Cab Model",
                    "Cab Dealer Name","Cab From",
                    "Cab To","Cab Number"))

    for i in data:
        print('''{0:<10} {1:<10} {2:<10} {3:<10} {4:<20} {5:<10} {6:<10}'''
            .format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    print("\n")
    dealInit()

def delCab():
   global dealerid
   cabid=input("Enter Cab Id : ")
   de="DELETE FROM cabs WHERE cab_id='"+cabid+"' and cab_dealerid='"+str(dealerid)+"'"
   x.execute(de)
   conn.commit()
   print("Cab Deleted Successfully...!")
   dealInit()

def updtCab():
    print("===============================Update Cabs==============================\n")
    global dealerid
    cabid=input("Enter Cab Id : ")
    se="SELECT * FROM cabs WHERE cab_id='"+cabid+"' and cab_dealerid='"+str(dealerid)+"'"
    d=x.execute(se)
    dt=d.fetchall()
    if(len(dt)!=0):
        cab_name=input("Enter Cab Name : ")
        cab_type=input("Enter Cab Type : ")
        cab_model=input("Enter Car Model : ")
        cab_dealerid=dealerid
        cab_from=input("Enter Cab From : ")
        cab_to=input("Enter Cab To : ")
        cab_number=input("Enter Cab No. : ")

        upt=f"UPDATE cabs SET cab_name='{cab_name}',cab_type='{cab_type}',cab_model='{cab_model}',cab_from='{cab_from}',cab_to='{cab_to}',cab_number='{cab_number}' WHERE cab_id='"+cabid+"' and cab_dealerid='"+str(dealerid)+"'"
        x.execute(upt)
        conn.commit()
        print("========================================================================")
        print("\nCab Updated Successfully....!\n")
    else:
        print("========================================================================")
        print("\nCab Not Found....!\n")

    dealInit()

def userLogin():
    print("==============================User Login================================")
    global userid
    username=input("Enter Name : ")
    password=input("Enter Password : ")
    d=x.execute("SELECT * FROM users WHERE user_name='"+username+"' and user_password='"+password+"'")
    dt=d.fetchall()
    for i in dt:
        userid=i[0]
    if(len(dt)!=0):
        print("========================================================================")
        print("\nLogin Successfully...!\n")
        initUser()
    else:
        print("========================================================================")
        print("\nInvalid Username and Password...!\n")
        userLogin()

def viewUserCab(cab_from="",cab_to=""):
    print("================================All Cabs================================\n")
    if cab_from =="" and cab_to=="":
        se="SELECT c.cab_id,c.cab_name,c.cab_type,c.cab_model,d.cab_dealername,c.cab_from,c.cab_to,c.cab_number FROM cabs c inner join cab_dealers d ON c.cab_dealerid=d.cab_dealerid"
    else:
        se=f'''SELECT c.cab_id,c.cab_name,
                c.cab_type,c.cab_model,
                d.cab_dealername,c.cab_from,
                c.cab_to,c.cab_number
                FROM cabs c inner join cab_dealers d
                ON c.cab_dealerid=d.cab_dealerid
                WHERE cab_from="{cab_from}" and cab_to="{cab_to}"'''

    d=x.execute(se)
    data=d.fetchall()
    print('''{0:<10} {1:<10} {2:<10} {3:<10} {4:<20} {5:<10} {6:<10}'''
            .format("Cab Id","Cab Name",
                    "Cab Type","Cab Model",
                    "Cab Dealer Name","Cab From",
                    "Cab To","Cab Number"))

    for i in data:
        print('''{0:<10} {1:<10} {2:<10} {3:<10} {4:<20} {5:<10} {6:<10}'''
            .format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    print("\n")
    initUser()

def updateUser():
    global userid
    print("==============================Update Profile============================")
    user_eamil=input("Enter Eamil : ")
    user_phone=input("Enter Phone Number : ")
    upt="UPDATE users SET user_email='"+user_eamil+"',user_phone='"+user_phone+"' WHERE user_id='"+str(userid)+"'"
    x.execute(upt)
    conn.commit()
    print("========================================================================")
    print("\nUser Data Updated Successfully...!\n")
    initUser()

def changeUserPass():
    print("==============================Change Password===========================")
    global userid
    old=input("Enter Your Old Password : ")
    d=x.execute("SELECT * FROM users WHERE  user_password='"+old+"' and user_id='"+str(userid)+"'")
    dt=d.fetchall()
    if(len(dt)!=0):
        newpass=input("Enter New Password : ")
        cpass=input("Enter Confirm Password : ")
        if(newpass==cpass):
            upt="UPDATE users SET user_password='"+newpass+"' WHERE user_id='"+str(userid)+"'"
            x.execute(upt)
            conn.commit()
            print("========================================================================")
            print("\nPassword Changed Successfully...!\n")

        else:
            print("========================================================================")
            print("\nNew Password and Confirm Password Not Matching...!\n")

    else:
        print("========================================================================")
        print("\nInvalid Password...!\n")

    initUser()
    
def initUser():
    print("============================User Dashboard==============================")
    global userid
    print('''1).View All Cabs
2).Search Cab
3).Update Profile
4).Change Password
5).Logout''')
    print("========================================================================")
    ch=int(input("Enter Your Choice : "))

    if ch==1:
        viewUserCab()
    elif ch==2:
        cab_from=input("Enter Cab From : ")
        cab_to=input("Enter Cab TO : ")
        viewUserCab(cab_from,cab_to)
    elif ch==3:
        updateUser()
    elif ch==4:
        changeUserPass()
    elif ch==5:
        del userid
        init()

def adminLogin():
    global adminid
    print("===========================Admin Login=================================")
    admin_username=input("Enter Username : ")
    admin_password=input("Enter Password : ")
    d=x.execute("SELECT * FROM admin WHERE admin_username='"+admin_username+"' and admin_password='"+admin_password+"'")
    dt=d.fetchall()
    for i in dt:
        adminid=i[0]
    if(len(dt)!=0):
        print("========================================================================")
        print("\nLogin Successfully...!\n")
        initAdmin()
    else:
        print("========================================================================")
        print("\nInvalid Username and Password...!\n")
        adminLogin()
        

def viewUsers():
    print("==============================All Users=================================\n")
    print("{0:^10}{1:^15}{2:^25}{3:^15}".format("User Id","User Name","User Email Id","User Phone Number"))

    se="SELECT user_id,user_name,user_email,user_phone FROM users"
    d=x.execute(se)
    dt=d.fetchall()
    for i in dt:
        print("{0:^10}{1:^15}{2:^25}{3:^15}".format(i[0],i[1],i[2],i[3]))

    print("\n1).Delete User \n2).Back")
    ch=int(input("Enter Your Choice : "))
    if ch==1:
        userid=input("Enter User Id : ")
        de="DELETE FROM users WHERE user_id='"+userid+"'"
        x.execute(de)
        conn.commit()
        print("========================================================================")
        print("\nUser Deleted Successfully...!\n")

        initAdmin()

    elif ch==2:
        initAdmin()
    else:
        print("========================================================================")
        print("\nInvalid Choice....!\n")
        viewUsers()

    initAdmin()

def viewDealers():
    print("==============================All Dealers===============================\n")
    print("{0:^10}{1:^15}{2:^20}{3:^15}".format("Delaer Id","Dealer Name","Dealer Email Id","Dealer Phone Number"))

    se="SELECT cab_dealerid,cab_dealername,cab_dealeremail,cab_dealerphone FROM cab_dealers"
    d=x.execute(se)
    dt=d.fetchall()
    for i in dt:
        print("{0:^10}{1:^15}{2:^20}{3:^15}".format(i[0],i[1],i[2],i[3]))

    print("\n1).Delete Dealer \n2).Back")
    ch=int(input("Enter Your Choice : "))
    if ch==1:
        dealerid=input("Enter Dealer Id : ")
        de="DELETE FROM cab_dealers WHERE cab_dealerid='"+dealerid+"'"
        x.execute(de)
        conn.commit()
        print("========================================================================")
        print("\nUser Deleted Successfully...!\n")

        initAdmin()

    elif ch==2:
        initAdmin()
    else:
        print("========================================================================")
        print("\nInvalid Choice....!\n")
        viewDealers()

    initAdmin()
    

def viewAllCab():
    print("================================All Cabs================================\n")
    se='''SELECT c.cab_id,c.cab_name,
                c.cab_type,c.cab_model,
                d.cab_dealername,c.cab_from,
                c.cab_to,c.cab_number
                FROM cabs c inner join cab_dealers d
                ON c.cab_dealerid=d.cab_dealerid'''
    d=x.execute(se)
    data=d.fetchall()
    print('''{0:^10} {1:^10} {2:^10} {3:^10} {4:^20} {5:^10} {6:^10}'''
            .format("Cab Id","Cab Name",
                    "Cab Type","Cab Model",
                    "Cab Dealer Name","Cab From",
                    "Cab To","Cab Number"))

    for i in data:
        print('''{0:^10} {1:^10} {2:^10} {3:^10} {4:^20} {5:^10} {6:^10}'''
            .format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))

    print("\n1).Delete Cab \n2).Back")
    ch=int(input("Enter Your Choice : "))
    if ch==1:
        cabid=input("Enter Cab Id : ")
        de="DELETE FROM cabs WHERE cab_id='"+cabid+"'"
        x.execute(de)
        conn.commit()
        print("========================================================================")
        print("\nCab Deleted Successfully...!\n")

        initAdmin()

    elif ch==2:
        initAdmin()
    else:
        print("========================================================================")
        print("\nInvalid Choice....!\n")
        viewAllCab()

def changeAdminPass():
    global adminid
    print("==============================Change Password===========================")
    old=input("Enter Your Old Password : ")
    d=x.execute("SELECT * FROM admin WHERE  admin_password='"+old+"' and admin_id='"+str(adminid)+"'")
    dt=d.fetchall()
    if(len(dt)!=0):
        newpass=input("Enter New Password : ")
        cpass=input("Enter Confirm Password : ")
        if(newpass==cpass):
            upt="UPDATE admin SET admin_password='"+newpass+"' WHERE admin_id='"+str(adminid)+"'"
            x.execute(upt)
            conn.commit()
            print("========================================================================")
            print("\nPassword Changed Successfully...!\n")

        else:
            print("========================================================================")
            print("\nNew Password and Confirm Password Not Matching...!\n")

    else:
        print("========================================================================")
        print("\nInvalid Password...!\n")

    initAdmin()
    
def initAdmin():
    global adminid
    print("============================Admin Dashboard=============================")
    print('''1).View All Users
2).View All Dealers
3).View All Cabs
4).Change Password
5).Logout''')
    print("========================================================================")
    ch=int(input("Enter Your Choice : "))

    if ch==1:
        viewUsers()
    elif ch==2:
        viewDealers()
    elif ch==3:
        viewAllCab()
    elif ch==4:
        changeAdminPass()
    elif ch==5:
        del adminid
        print("========================================================================")
        print("\nLogout Successfully...!\n")
        init()

def init():
    print("=======================Cab Management Application=======================")
    print('''1).Dealer Registration
2).Dealer Login
3).User Registration
4).User Login
5).Admin Login
6).Exit''')
    print("========================================================================")
    ch=int(input("Enter Your Choice : "))
    if ch==1:
        dealerReg()
    elif ch==2:
        dealerLogin()
    elif ch==3:
        userReg()
    elif ch==4:
        userLogin()
    elif ch==5:
        adminLogin()
    elif ch==6:
        print("========================================================================")
        exit()

        
#createTable()
init()
