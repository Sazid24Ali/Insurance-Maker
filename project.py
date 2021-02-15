import random as rd
import mysql.connector as sql
import random
import time
con=sql.connect(host='localhost',user='root',password='mysql')
curs=con.cursor()
def about():
    print('''
        ----------------------------------------------

                                      ABOUT   
                                    --------
         THIS PROGRAMM IS WRITTEN IN PYTHON
             THIS PROGRAM IS BASICALLY DEALS WITH BUYING INSURANCE ONLINE WITH NO INSECURITY
             ITS AN HIGHLY SECURE ADMIN-USER TYPE MODEL USED IN THIS PROJECT.

    IN TO THE PROJECT  |:::|
        THERE ARE TWO TYPES OF POLICIES I HAVE CONCENTRATED ON :\\
     1) General insurance
        (i)  Motor insurance
            (a) BIKE INSURANCE
            (b) AUTO INSURANCE
        (ii) Home insurance  
     2) Life insurances
         (i)Term insurance
         (ii)Pension Plans
            House,Life  insurance are classified under 4- plans
                50k,1L,1.5L,2L with tere own rate of EMI's
                For Monthly,Quaterly and Annually
            
            You can also avail your insurance using an unique id the is generated during the creation of your account .
                                            ```Remember Your ID to see your ```
    Your are also given oppurtunity you to just view through the prompt
    By enterning the default/guest user where you have to login as an user
    
    ''')


    input("                     ENter Any Key to Exit ")
    print("------------------------------------------------------------------------------------")
    welc()
            
'''//////////////////////////////////-----------------------------------------------------------///////////////////////////////////////////'''
def adm_ins():
    print('''
            Sir Entered the Insurance Log

                1) Manuplilation records
                2) Go back to last menu
                3) To exit the prompt''')
    i=int(input('''
                         Entered the option From above :--  '''))
    print('''
                            '''+captcha()+''' ''')
    b=input(" Enter the captcha :-- ")
    if i==3 or b!='':
        print('''
        ----------------------------------------------''')
        welc()
    elif i==2:admin_pow()
    elif i== 1:
        curs.execute(" SELECT * FROM INSUR; ")
        K=curs.fetchall()
        for i in K:
            for j in i:
                print(j ,end='   ')
            print()
        m=int(input('''
                1) Delete the users records
                2) Update the records
                3) To back to the prompt
                4) Exit
                    Enter the option :-- '''))
        if m==1:
            M=int(input('''
                    Enter the id Of the customer You want delete : '''))
            if M==0:print('''
                 Admin cannot be deleted
          ----------------------------------------------''');admin_pow()
            else:
                curs.execute("SELECT * FROM INSUR WHERE ID=%d ;"%M)
                c=curs.fetchall()
                print('''
                        user : ''', c[1],''' Is being Deleted''')
                curs.execute("DELETE FROM USERS WHERE ID=%d ;"%M)
                con.commit()
                print(''' Sucessfully deleted the record
        ----------------------------------------------''')
                adm_use()
        elif m==2:
            E=int(input('''
                    Entered the updating log
                            1) update all the records
                            2) specific record
                            3) Back to menu
                            '''))
            if E==3:print('''
        ----------------------------------------------''');admin_pow()
            elif E==2:
                S=int(input('''
                Enter the Id of the user :-- '''))
                curs.execute("UPDATE TABLE INSUR SET TER_LEFT=TER_LEFT-1 WHERE ID=%d;"%S)
                con.commit()
                print('''
                    UPDATED RECORD SUCCESFULLY''')
                adm_ins()
            elif E==1:
                curs.execute("UPDATE TABLE INSUR SET TER_LEFT=TER_LEFT-1;")
                con.commit()
                print('''
                    UPDATED RECORDS SUCCESFULLY''')
                adm_ins()
            else:
                print('''
                WRONG INPUT
                        TAKING YOU TO LAST MENU
        ----------------------------------------------''')
                admin_pow()
        elif m==3:
            print('''
        ----------------------------------------------''')
            admin_pow()
        elif m==4:exit
    else:print('''
                     Getting you back to the home page
       ----------------------------------------------
            ''');welc()                             
'''/////////////////////////////////////////////////---------------------------------/////////////////////////////////////////////////////////'''
def adm_use():
    print('''
            Sir Entered the Users Log

                1) Manuplilation records
                2) Go back to last menu
                3) To exit the prompt''')
    i=int(input('''
                         Entered the option From above :--  '''))
    print('''
                            '''+captcha()+''' ''')
    b=input(" Enter the captcha :-- ")
    if i==3 or b!='':
        print('''
                CULPRIT
        ----------------------------------------------''')
        welc()
    elif i==2:admin_pow()
    elif i== 1:
        curs.execute(" SELECT * FROM USERS; ")
        K=curs.fetchall()
        for i in K:
            for j in i:
                print(j ,end='   ')
            print()
        m=int(input('''
                1) Delete the users records
                2) Add the new users
                3) To back to the prompt
                4) Exit
                    Enter the option :-- '''))
        if m==1:
            M=int(input('''
                    Enter the id Of the customer You want delete : '''))
            if M==0:print('''
                 Admin cannot be deleted
          ----------------------------------------------''');admin_pow()
            else:
                curs.execute("SELECT * FROM USERS WHERE ID=%d ;"%M)
                c=curs.fetchall()
                c=c[0]
                print('''
                        user : ''', c[1],''' Is being Deleted''')
                curs.execute("DELETE FROM USERS WHERE ID=%d ;"%M)
                con.commit()
                print(''' Sucessfully deleted the record
        ----------------------------------------------''')
                adm_use()
        elif m==2:
            I=input('''
                   ENTER THE DETAILS
                                    NAME : ''')
            K=input('''
                              USERNAME : ''')
            J=input('''
                              PASSWORD : ''')
            M=input('''
                                      TYPE :  ''')
            curs.execute("SELECT ID FROM USERS;")
            L=curs.fetchall()
            s=True
            while s:
                V=rd.randint(10,999)
                if V != L:break
            curs.execute("INSERT INTO USERS VALUES(%d,'%s','%s','%s','%s');"%(V,I,K,J,M))
            con.commit()
            print('''
                Sucessfully added the record
        ----------------------------------------------''')
            adm_use()
        elif m==3:
            print('''
         ----------------------------------------------''')
            admin_pow()
        elif m==4:exit
    else:print('''
                     Getting you back to the home page
       ----------------------------------------------
            ''');welc()                             
'''//////////////////////////////////-----------------------------------------------------------///////////////////////////////////////////'''
def admin_pow():
    print( 50 * '\n')
    print('''
     Mr Sazid,
             Lets us know what you want to do from below ''')
    SD=input('''

        See existing users :-- seu
        See existing insurance holders :-- seh
        :---- ''')
    if SD=='seu':adm_use()
    elif SD=='seh':adm_ins()
    else:print('''
             Enter the correct option ''');admin_pow()
'''//////////////////////////////////-----------------------------------------------------------///////////////////////////////////////////'''
def master_tbl(name,typ_ins,price,term,installm,prem):
    print('''
           ----------------------------------------------
We are almost done with this so we are updating everything
                So from now after every '''+str(installm)+'''th month
                                we will transact an amount of '''+str(prem)+'''

        Use Your ID  will be used as an key to see your
        plan an also how many installments are being transcated ''')
    curs.execute("SELECT ID FROM USERS WHERE NAME='%s';"%(name))
    ide=curs.fetchall()
    ide=int(ide[0][0])
    curs.execute("INSERT INTO INSUR VALUES(%d,'%s','%s',%d,'%s',%d,%d);"%(ide,name,typ_ins,price,term,installm,prem))
    con.commit()
    print('''
        The ID given for your insurance is :-- '''+ str(ide) +''' 
                You  can see  the updates through this id
    ----------------------------------------------''')
    welc()
'''//////////////////////////////////-----------------------------------------------------------///////////////////////////////////////////'''        
def ins(name,tpin,price,term,instl,pre):
    time.sleep(2)
    ''' name  you have to pay a sum of _ money for a term of _ years and  '''  
    print('''
    So Mr/Mrs  '''+name+''' ,
                After analyzing the data we have your plans ready
                        You have to pay a premeium of Rs.'''+ str(pre)+'''
                                for every '''+str(instl)+'''th month of an year
                                                            for '''+term+'''years
------------------------------------***************************************************-----------------------------------------------''')
    if name=='GUEST':
        print('''  You have Entered as an default user
                            Therefore you are restricted to this window only
                                        Now taking you to the main window
                 ----------------------------------------------''')
        welc()
    
    xs=input('''
         Do you want to avail this offer then TYPE ``1``
                                TO see Other plans  TYPE ``0``
If you type anything else we will take you directly to the main window
                                                                        ANSWER :== ''')
    if xs=='1':
        master_tbl(name,tpin,price,term,instl,pre)
    elif xs=='0':
        m_ins(name,tpin)
    else:
        print('''
        WRONG INPUT
             Taking you Directly To the main Window
                                                Told You!!!
     ----------------------------------------------''')
    
    

'''//////////////////////////////////-----------------------------------------------------------///////////////////////////////////////////'''    
i=0
def m_ins(na,typ):
    global i
    if typ in ('bike-gen','auto-gen'):
        P=int(input('''
        Enter the price of vehicle
                    ``Enter only Numbers``  :- '''))
    else:
        i+=1
        P=int(input('''
                1) 50,000
                2) 1,00,000
                3) 1,50,000
                4) 2,00,000
                    Enter the plan:- '''))
        if P==1:P=50000
        elif P==2:P=100000
        elif P==3:P=150000
        elif P==4:P=200000
        elif i==3:print('''
               TOO MANY INVALID INPUTS
                       EXITING''');exit
        else :print('''
            INVALID INPUT TRY AGAIN ''');m_ins()
    O=input('''
    Enter the term of the plan
                ``Enter only Numbers``  :-  ''')
    I=input('''
    Enter the premeium type
                Quaterly---qyt
                Halferly ---hyt
                Annually---ayt
                                NOW :- ''')
    qyt,hyt,ayt=4,2,12
    if I=='qyt':
        pre=(int(P)/int(O))/4;ins(na,typ,P,O,qyt,pre)
    elif I=='hyt':pre=(int(P)/int(O))/2;ins(na,typ,P,O,hyt,pre)
    elif I=='ayt':pre=(int(P)/int(O))/1;ins(na,typ,P,O,ayt,pre)
    else :
        print('''
                You have done some  mistake
                                ```` Taking you to the home page ```
                                        For security Reasons
    ----------------------------------------------''')
        welc()
    
'''//////////////////////////////////-----------------------------------------------------------///////////////////////////////////////////'''    
def genin(nam):
    ZS=input('''
OK Mr/Mrs   '''+nam+''',
    The available insurances plans are
    1) Motor insurance
    2) Home insurance
                    Enter the option :-  ''')
    if ZS=='1':
        R=int(input('''
        1) Automobile  insurance
        2) Bike insurane
                     Enter a option :- '''))
        if R==1 :E='auto-gen';m_ins(nam,E)
        elif R==2:E='bike-gen';m_ins(nam,E)
        else :
            print('''
                You have done some  mistake
                                ```` Taking you to the home page ```
                                        For security Reasons
     ----------------------------------------------''')
            welc()
    elif ZS=='2':E='Hous-gen';m_ins(nam,E)
    else:print('''
                You have done some  mistake
                                ```` Taking you to the home page ```
                                        For security Reasons
    ----------------------------------------------''');welc()
    
'''//////////////////////////////////-----------------------------------------------------------///////////////////////////////////////////'''
def liin(nam):
    ZS=input('''
OK Mr/Mrs   '''+nam+''',
    The available insurances plans are
    1) Term insurance
    2) Pensions insurance
                    Enter the option :-  ''')
    if ZS=='1':
        E='term-lif';m_ins(nam,E)
    elif ZS=='2':E='peio-gen';m_ins(nam,E)
    else:print('''
                You have done some  mistake
                                ```` Taking you to the home page ```
                                        For security Reasons
     ----------------------------------------------''');welc()
'''//////////////////////////////////-----------------------------------------------------------///////////////////////////////////////////'''
def exist(name):
    o=int(input('''
        Enter your unique id :-- '''))
    curs.execute("SELECT * FROM INSUR WHERE ID=%d;"%o)
    R=curs.fetchall()
    if R==[]:
            print('''
        Either you donot have any registered insurance plans
                                OR
        You have entered the your wrong id''')
            main(name)
            
    else:
        print(''''
        The below given are your records''')
        lk=['ID :- ','Name :- ','Type :- ','Total money :- ','Term Left :- ','Total installmanets :- ','Premeium :- ']
        for i in R :
            k=0
            for j in i:
                print(lk[k],j)
                k+=1
        main(name)

'''//////////////////////////////////-----------------------------------------------------------///////////////////////////////////////////'''
def main(name):
    print('''
        ----------------------------------------------''')
    print('''
Welcome Mr/Mrs   '''+name+''',
    TYPE OF INSURANCES AVALABLE
    1) General insurance
        (i)  Motor insurance
        (ii) Home insurance
     2) Life insurances
         (i)Term insurance
         (ii)Pension Plans
    3) See your existing insurance files
    4) exit
         ''')
    Q=input('''
        Enter the type of insurance you want to prefer
                 ``example 1 ---General insurance``
                                            ENTER NOW :-  ''')
    if '1'in Q: genin(name)
    elif '2'in Q:liin(name)
    elif Q=='3':exist(name)
    elif Q=='4':
        print('''
        Exiting the promt Safely
    ----------------------------------------------
        ''')
        exit
    else:
        print('''
        The Entered option is incorrect
                                  ```  GOING BACK TO LAST MENU ```
    ----------------------------------------------''')
        login()
    

'''//////////////////////////////////-----------------------------------------------------------///////////////////////////////////////////'''
def sgn():
    print('''
        1) To make a new account _/
        2) Go back To last Menu  _/
        ''')
    a=int(input('''
        Enter the option :~  '''))
    if a==2:
        print('''
        ----------------------------------------------''')
        site()
    elif a==1:
        na=input('''
        Enter your name :- ''')
        us=input('''
        Enter the User name :- ''')
        che=captcha()
        ps=input('''
        Enter the Password :- ''')
        if len(ps)>8 and len(ps)<11:
            print(''' Please enter a password between 8 to 10 characters  ''')
            sgn()
        print('''
            '''+che+'')
        cf=input('''
        Enter the captcha  :- ''')
        time.sleep(2)
        if cf!=che :
            print('''
        The Entered captcha is incorrect
                                  ```  THE PROCESS WILL START AGAIN ```
       ----------------------------------------------''')
            sgn()
        else:
            curs.execute("SELECT ID FROM USERS ;")
            iw=curs.fetchall()
            while True:
                a=random.randint(1002,9999)
                if a in iw:
                    continue
                else:break
            curs.execute("INSERT INTO USERS VALUES(%d,'%s','%s','%s','USER');"%(a,na,us,ps))
            con.commit()
            print('''

        IMPORTANT
            YOUR UNIQUE ID IS ---- ''',a,''' --- REMEMBER THIS''')
            input("enter any key ")
            print('''
           The process is completed SUCCESFUL
                   NOW YOU ARE A PART OF OUR COMMUNITY 
                                   ``` TAKING YOU TO THE HOME PAGE ```
        ----------------------------------------------''')
            welc()
'''//////////////////////////////////-----------------------------------------------------------///////////////////////////////////////////'''        
def dthan():
##    curs.execute("DROP DATABASE IF EXISTS PROJECT;")
##    curs.execute("CREATE DATABASE PROJECT;")
    curs.execute("USE PROJECT;")
##    curs.execute("CREATE TABLE USERS(ID INT(5) PRIMARY KEY ,NAME VARCHAR(25),USERNAME VARCHAR(25) ,PASSWORD VARCHAR(10),TYPE CHAR(5) DEFAULT 'USER');")
##    curs.execute("INSERT INTO USERS VALUES(000,'SAZID','ADMin','ADM','ADMIN');")
##    curs.execute("INSERT INTO USERS VALUES(1001,'GUEST','Guest','JUST','USER');")
##    curs.execute("CREATE TABLE INSUR(ID INT(5),NAME VARCHAR(25),TYPE_INSUR VARCHAR(15),END_MON INT(10),TEM_LEFT VARCHAR(20),INSTALLMENT INT(5),PREMIUM INT);")
##    curs.execute("ALTER TABLE INSUR ADD FOREIGN KEY (ID) REFERENCES USERS(ID);")
    con.commit()

'''//////////////////////////////////-----------------------------------------------------------///////////////////////////////////////////'''
def login():
    A=input('''
  Enter the user name :~  ''')
    curs.execute("SELECT * FROM USERS;")
    x=curs.fetchall()
    for i in x:
        if i[2]==A:
            x=i
            break
    else:
        print('''
        The Entered Username is incorrect
                                  ```  GOING BACK TO LAST MENU  ```
    ----------------------------------------------''')
        site()
    B=input('''
  Enter the password :~  ''')
    while True:
        if x[3]==B:
            break
        else:
            print('''
        The Entered Password is incorrect
                                  ```  GONING BACK TO LAST MENU ```
    ----------------------------------------------''')
            site()
    che=captcha()
    print('''
                '''+che+'''   ''')
    C=input('''
  Enter the captcha :~  ''')
    
    if C!=che:
        print('''
        The Entered captcha is incorrect
                                  ```  GOING BACK TO LAST MENU ```
      ----------------------------------------------''')
        site()
    if x[-1]=='ADMIN':
        SD=input('''
        WELCOME MR SAZID ,
                    WOULD YOU LIKE TO GO IN TO THE WEBSITE(as USER)
                                                OR
                                    TAKE UP AS AN ADMIN

''')
        if SD in ['ADMIN','ADM','admin','adm','min']:
            admin_pow()
    main(name=x[1])
    
'''//////////////////////////////////-----------------------------------------------------------///////////////////////////////////////////'''
    
def site():
    print('''
        ----------------------------------------------
                      ``Insuring Lives of India''
                          ```Welcomes You```
                    
            1) login
            3)New User _/
            4) Go Back _/

``` We can let you enter as an guest into website but there are restrictions init .```
``So make a new users as Possible```
  ##username='Guest'##
###password='JUST'###
    ''')
    
    Z=int(input("Enter the option :- "))
    if Z==1 :login()
    elif Z==3:sgn()
    elif Z==4 :
        print("""
    ----------------------------------------------""")
        welc()
    else:
        print(""""
        The entered option is incorrect
                        Please enter the corrcet option!!!!!!!
     ----------------------------------------------""")
        site()

'''//////////////////////////////////-----------------------------------------------------------///////////////////////////////////////////'''
def welc(i=1):
    print("""
                  ``  Welcome to the  ``
              ``` Insuring  lives  of  india  ```
          `` The no.1 Insurance site in  india ``
          """)
    print("""
          1) Enter the site  _/
          2) About _/
          3)Exit the site  _/

     """)
    Y=int(input("Enter the opt :-  "))
    if Y==1:site()
    elif Y==2:about()
    elif Y==3:exit
    elif i>3:
        print('''

        We Are exitng the site
                        TOLD YOU!!!!''')
        exit
    else:
        print('''

Wrong input please enter the correct one
                    OR the site will exit automatically
    ----------------------------------------------                    ''')
        i+=1
        welc(i)
'''//////////////////////////////////-----------------------------------------------------------///////////////////////////////////////////'''
def captcha():
    Al=[ chr(i) for i in range(65,91)]
    al=[ chr(i) for i in range(97,123)]
    nu=[ str(i) for i in range(10)]
    sp=['!','@','#','$','%','^','&','*','>','<','?','|']
    captcha=''
    for i in range(6):
        a=rd.choice([Al,al,nu,sp])
        b=rd.choice(a)
        captcha+=b
    return captcha

dthan()
welc()
