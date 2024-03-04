from tkinter import *
import sqlite3
import Classes

def closeWindow(window):
    window.destroy()

def edit_personal_info_S3(personalObj,field,window,info_entry,is_admin):
    
    if is_admin:
        cursor.execute(
            """UPDATE Admins SET {} = ? WHERE UserName = ?""".format(field),
            (info_entry.get(),personalObj.UserName)
        )
    else:
        cursor.execute(
            """UPDATE Users SET {} = ? WHERE UserName = ?""".format(field),
            (info_entry.get(),personalObj.UserName)
        )

    connection.commit()

    if field == 'UserName':
        personalObj.UserName = info_entry.get()
    elif field == 'Password':
        personalObj.Password = info_entry.get()
    elif field == 'FirstName':
        personalObj.FirstName = info_entry.get()
    elif field == 'LastName':
        personalObj.LastName = info_entry.get()
    elif field == 'Age':
        personalObj.Age = info_entry.get()
    elif field == 'Adress':
        personalObj.Adress = info_entry.get()
    elif field == 'PhoneNumber':
        personalObj.PhoneNumber = info_entry.get()
    elif field == 'Email':
        personalObj.Email = info_entry.get()
    
    lbl = Label(window,text='Entry Updated Succesfully!',fg='Green')
    lbl.grid(row=13,column=0)


def edit_personal_info_S2(personalObj,field,window,is_admin):

    lbl = Label(window,text=f'enter new {field}')
    lbl.grid(row=9,column=0)

    newInfo_entry = Entry(window)
    newInfo_entry.grid(row=10,column=0)

    confirm_btn = Button(
        window,
        text='Confirm',
        width=4,height=2,
        command=lambda:edit_personal_info_S3(personalObj,field,window,newInfo_entry,is_admin)
    )
    confirm_btn.grid(row=11,column=0)

    if is_admin:
        back_btn = Button(
            window,
            text='Go Back',
            width=4,height=2,
            command=lambda:[closeWindow(window),admin_dashboard(personalObj)]
        )
    else:
        back_btn = Button(
            window,
            text='Go Back',
            width=4,height=2,
            command=lambda:[closeWindow(window),UserDashboard(personalObj)]
        )
    back_btn.grid(row=12,column=0)

def edit_personal_info_S1(personalObj,is_admin=False):

    edit_info_wind = Tk()

    edit_info_wind.title('Edit Personal Info')

    edit_info_wind.geometry('450x500')

    lbl = Label(edit_info_wind,text='What Field Do You Wish to Edit?')
    lbl.config(font=('Bold',20))
    lbl.grid(row=0,column=0)

    username_btn = Button(
        edit_info_wind,
        text='Username',
        command=lambda:edit_personal_info_S2(personalObj,'UserName',edit_info_wind,is_admin)
    )
    username_btn.grid(row=1,column=0)

    password_btn = Button(
        edit_info_wind ,
        text='Password',
        command=lambda:edit_personal_info_S2(personalObj,'Password',edit_info_wind,is_admin)
    )
    password_btn.grid(row=2,column=0)

    FirstName_btn = Button(
        edit_info_wind,
        text='First Name',
        command=lambda:edit_personal_info_S2(personalObj,'FirstName',edit_info_wind,is_admin)
    )
    FirstName_btn.grid(row=3,column=0)

    LastName_btn = Button(
        edit_info_wind,
        text='Last Name',
        command=lambda:edit_personal_info_S2(personalObj,'LastName',edit_info_wind,is_admin)
    )
    LastName_btn.grid(row=4,column=0)

    Age_btn = Button(
        edit_info_wind,
        text='Age',
        command=lambda:edit_personal_info_S2(personalObj,'Age',edit_info_wind,is_admin)
    )
    Age_btn.grid(row=5,column=0)

    Address_btn = Button(
        edit_info_wind,
        text='Address',
        command=lambda:edit_personal_info_S2(personalObj,'Adress',edit_info_wind,is_admin)
    )
    Address_btn.grid(row=6,column=0)

    PhoneNumber_btn = Button(
        edit_info_wind,
        text='Phone Number',
        command=lambda:edit_personal_info_S2(personalObj,'PhoneNumber',edit_info_wind,is_admin)
    )
    PhoneNumber_btn.grid(row=7,column=0)

    Email_btn = Button(
        edit_info_wind,
        text='Email',
        command=lambda:edit_personal_info_S2(personalObj,'Email',edit_info_wind,is_admin)
    )
    Email_btn.grid(row=8,column=0)

def View_Personal_Info(personalObj,is_admin,self_view=True):

    personal_info_wind = Tk()

    personal_info_wind.title('Personal Info')

    personal_info_wind.geometry('250x300')

    personal_info_wind.resizable(width=False,height=False)

    username_lbl = Label(personal_info_wind,text=f'User Name: {personalObj.UserName}')
    username_lbl.pack()

    password_lbl = Label(personal_info_wind,text=f'Password: {personalObj.password}')
    password_lbl.pack()

    FirstName_lbl = Label(personal_info_wind,text=f'First Name: {personalObj.FirstName}')
    FirstName_lbl.pack()

    LastName_lbl = Label(personal_info_wind,text=f'Last Name: {personalObj.LastName}')
    LastName_lbl.pack()

    Age_lbl = Label(personal_info_wind,text=f'Age: {personalObj.Age}')
    Age_lbl.pack()

    Adress_lbl = Label(personal_info_wind,text=f'Adress: {personalObj.Adress}')
    Adress_lbl.pack()

    PhoneNumber_lbl = Label(personal_info_wind,text=f'Phone Number: {personalObj.PhoneNumber}')
    PhoneNumber_lbl.pack()

    Email_lbl = Label(personal_info_wind,text=f'Email: {personalObj.Email}')
    Email_lbl.pack()

    if self_view:

        if is_admin:
            back_btn = Button(
                personal_info_wind,
                text='Go Back',
                width=4,height=2,
                command=lambda:[closeWindow(personal_info_wind),admin_dashboard(personalObj)]
            )
        else:
            back_btn = Button(
                personal_info_wind,
                text='Go Back',
                width=4,height=2,
                command=lambda:[closeWindow(personal_info_wind),UserDashboard(personalObj)]
            )
        back_btn.pack()

def UserDashboard(userObj,action='none'):

    user_wind = Tk()

    user_wind.title('User Dashboard')

    user_wind.geometry('250x300')

    user_wind.resizable(width=False,height=False)

    # if just_registered:
    #     action = 'Registery'
    # else:
    #     action = 'Login'
    if action != 'none':
        #login succesfull or registery succesfull
        lbl = Label(user_wind,text=f'{action} Completed',fg='Green')
        lbl.grid(row=0,column=0)

        lbl2 = Label(user_wind,text=f'welcome {userObj.FirstName} {userObj.LastName}')
        lbl2.grid(row=1,column=0)

    view_info_btn = Button(
        user_wind,
        width=15,height=2,
        text='View Personal Information',
        command=lambda:[closeWindow(user_wind),View_Personal_Info(userObj,False)]
    )
    view_info_btn.grid(row=3,column=0)

    edit_info_btn = Button(
        user_wind,
        width=15,height=2,
        text='Edit Personal Information',
        command=lambda:[closeWindow(user_wind),edit_personal_info_S1(userObj)]
    )
    edit_info_btn.grid(row=4,column=0)

    close_app_btn = Button(
        user_wind,text='Close Application',
        width=15,height=2,
        command=lambda:closeWindow(user_wind)
    )
    close_app_btn.grid(row=5,column=0)

def save_register_info(un,p,fn,ln,a,ad,pn,e,window):

    UserName = un.get()
    Password = p.get()
    FirstName = fn.get()
    Lastname = ln.get()
    Age = a.get()
    Adress = ad.get()
    PhoneNumber = pn.get()
    Email = e.get()

    window.destroy()

    try:

        insert = """INSERT INTO Users VALUES (?,?,?,?,?,?,?,?)"""

        data_tuple = (UserName,Password,FirstName,Lastname,Age,Adress,PhoneNumber,Email)

        cursor.execute(insert,data_tuple)

        connection.commit()

        user = Classes.Users(UserName,Password,FirstName,Lastname,Age,Adress,PhoneNumber,Email)

        UserDashboard(user,'Registery')

    except sqlite3.IntegrityError:

        print('error')

        registery(True,UserName)

def registery(check=False,usnam=''):

    registery_wind = Tk()

    registery_wind.title('Sign Up')

    registery_wind.geometry('350x500')

    registery_wind.resizable(width=False,height=False)

    if check:
        error_lbl = Label(registery_wind,text=f'UserName {usnam} is Already Taken',fg='red')
        error_lbl.pack()

    username_entry = Entry(registery_wind)
    username_lbl = Label(registery_wind,text='enter your username')
    # username_entry.place(x=30,y=50)
    # username_entry.insert(0,'enter your username')
    username_lbl.pack()
    username_entry.pack()
    
    pass_entry = Entry(registery_wind)
    pass_lbl = Label(registery_wind,text='enter your password')
    # pass_entry.insert(0,'enter your password')
    pass_lbl.pack()
    pass_entry.pack()

    FName_entry = Entry(registery_wind)
    FName_lbl = Label(registery_wind,text='enter your first name')
    FName_lbl.pack()
    FName_entry.pack()

    LName_entry = Entry(registery_wind)
    LName_lbl = Label(registery_wind,text='enter your last name')
    LName_lbl.pack()
    LName_entry.pack()

    age_entry = Entry(registery_wind)
    age_lbl = Label(registery_wind,text='enter your age')
    age_lbl.pack()
    age_entry.pack()

    adress_entry = Entry(registery_wind)
    adress_lbl = Label(registery_wind,text='enter your adress')
    adress_lbl.pack()
    adress_entry.pack()

    Pnum_entry = Entry(registery_wind)
    Pnum_lbl = Label(registery_wind,text='enter your phone number')
    Pnum_lbl.pack()
    Pnum_entry.pack()

    email_entry = Entry(registery_wind)
    email_lbl = Label(registery_wind,text='enter your email adress')
    email_lbl.pack()
    email_entry.pack()

    # if check:
    #     username_entry.delete(0,END)
    #     pass_entry.delete(0,END)
    #     FName_entry.delete(0,END)
    #     LName_entry.delete(0,END)
    #     age_entry.delete(0,END)
    #     adress_entry.delete(0,END)
    #     Pnum_entry.delete(0,END)
    #     email_entry.delete(0,END)

    # un = username_entry.get()
    # p = pass_entry.get()
    # fn = FName_entry.get()
    # ln = LName_entry.get()
    # a = age_entry.get()
    # ad = adress_entry.get()
    # pn = Pnum_entry.get()
    # e = email_entry.get()

    # email_entry.delete(0,Tk=END)


    cnfrm = Button(
        registery_wind,
        text='Confirm!',
        fg='Green',
        # font='Italic',
        command=lambda:save_register_info(
            username_entry,
            pass_entry,
            FName_entry,
            LName_entry,
            age_entry,
            adress_entry,
            Pnum_entry,
            email_entry,
            registery_wind
        )
    )
    cnfrm.config(font='Italic')
    cnfrm.pack()

    registery_wind.mainloop()

def User_login_Back(un_entry,pass_entry,previous_window):

    username = un_entry.get()
    password = pass_entry.get()

    previous_window.destroy()

    select_username = """SELECT UserName FROM Users"""

    username_list_tup = connection.execute(select_username)

    username_list = []

    for i in username_list_tup:
        username_list.append(i[0])

    if username in username_list:
        username_check = True
    else:
        username_check = False

    if username_check:

        select_password = """SELECT Password FROM Users"""

        password_list_tup = connection.execute(select_password)

        password_list = []

        for i in password_list_tup:
            password_list.append(i[0])

        if password in password_list:
            password_check = True
        else:
            password_check = False

        if password_check:

            select_user = """SELECT * FROM Users WHERE UserName=?"""

            data_tup = (username,)

            selected_user_loc = cursor.execute(select_user,data_tup)

            selected_user_list_tup = selected_user_loc.fetchall().copy()

            selected_user_tup = selected_user_list_tup[0]

            (un,p,fn,ln,a,ad,pn,e) = selected_user_tup

            user = Classes.Users(un,p,fn,ln,a,ad,pn,e)

            UserDashboard(user,'Login')

        else:
            User_login_Front(username_check,password_check)
    
    else:
        User_login_Front(username_check)

def User_login_Front(username_check=True,password_check=True):

    UserLogin_wind = Tk()

    UserLogin_wind.title('User Log In')

    UserLogin_wind.geometry('300x300')

    if not username_check:
        username_error_lbl = Label(UserLogin_wind,text='Username Not Found',fg='red')
        username_error_lbl.pack()
    elif not password_check:
        password_error_lbl = Label(UserLogin_wind,text='Wrong Password!',fg='red')
        password_error_lbl.pack()

    username_lbl = Label(UserLogin_wind,text='enter your username')
    username_lbl.pack()
    username_entry = Entry(UserLogin_wind)
    username_entry.pack()

    password_lbl = Label(UserLogin_wind,text='enter your password')
    password_lbl.pack()
    password_entry = Entry(UserLogin_wind)
    password_entry.pack()

    confirm_btn = Button(
        UserLogin_wind,
        text='Confirm',
        fg='Green',
        command=lambda:User_login_Back(username_entry,password_entry,UserLogin_wind)
    )
    confirm_btn.pack()

def user_entry():

    UserEntry_wind = Tk()

    UserEntry_wind.title('User Entry')

    UserEntry_wind.geometry('500x300')

    UserEntry_wind.resizable(width=False,height=False)

    lbl = Label(UserEntry_wind,text='Do You Have an Acount...?')
    lbl.config(font=('Bold',40))
    lbl.grid(row=0,column=0)

    lbl2 = Label(UserEntry_wind,text='Login if You Already Have an Acount or Sign UP to Create a New One')
    lbl2.grid(row=1,column=0)

    registry_btn = Button(
        UserEntry_wind,
        text='SIGN UP',
        width=4,height=2,
        command=lambda:[closeWindow(UserEntry_wind),registery()]
    )
    registry_btn.grid(row=3,column=0)

    login_btn = Button(
        UserEntry_wind,
        text='LOG IN',
        width=4,height=2,
        command=lambda:[closeWindow(UserEntry_wind),User_login_Front()]
    )
    login_btn.grid(row=4,column=0)

    UserEntry_wind.mainloop()

def view_users_Back(username):

    select_user = """SELECT * FROM Users WHERE UserName=?"""

    data_tup = (username,)

    selected_user_loc = cursor.execute(select_user,data_tup)

    selected_user_list_tup = selected_user_loc.fetchall().copy()

    selected_user_tup = selected_user_list_tup[0]

    (un,p,fn,ln,a,ad,pn,e) = selected_user_tup

    userObj = Classes.Users(un,p,fn,ln,a,ad,pn,e)

    View_Personal_Info(userObj,True,False)

def view_users_Front(adminObj):

    show_users_wind = Tk()

    show_users_wind.title('View Users')

    # show_users_wind.geometry('250x350')

    show_users_wind.resizable(width=False,height=False)

    lbl = Label(show_users_wind,text='Choose the User to View Personal Info')
    lbl.config(font=('Italic',20))
    lbl.pack()
    
    select_username = """SELECT UserName FROM Users"""

    username_list_tup = connection.execute(select_username)

    username_list = []

    for i in username_list_tup:
        username_list.append(i[0])

    # lbl_list = []

    # for i in range(len(username_list)):
    #     lbl_list.append(Button(show_users_wind
    #                            ,text=username_list[i],
    #                            command=lambda:view_users_Back(i)),)

    for username in username_list:
        btn = Button(
            show_users_wind,
            text=username,
            command=lambda username = username :view_users_Back(username)
        )
        btn.pack()

    # for i in range(len(username_list)):
    #     lbl_list[i].pack()

    back_btn = Button(
        show_users_wind,
        text='Go Back',
        fg='red',
        # width=4,height=2,
        command=lambda:[closeWindow(show_users_wind),admin_dashboard(adminObj)]
    )
    back_btn.pack()

def delete_users_back(username,window,adminObj):

    delete = """DELETE FROM Users WHERE UserName = ?"""

    data_tuple = (username,)

    cursor.execute(delete,data_tuple)

    connection.commit()

    lbl = Label(window,text='User Deleted Succesfully',fg='Green')
    lbl.place(x=130,y=95)

    back_btn = Button(
        window,
        text='Go Back',
        # width=4,height=2,
        command=lambda:[closeWindow(window),admin_dashboard(adminObj)]
    )
    back_btn.place(x=160,y=125)

def delete_users_Front_S2(username,adminObj):

    del_user_cnfrm = Tk()

    del_user_cnfrm.title('Delete User Confirmation')

    del_user_cnfrm.geometry('450x200')

    del_user_cnfrm.resizable(width=False,height=False)

    lbl = Label(del_user_cnfrm,text=f'Are You Sure You want to Delete User {username} ?')
    lbl.config(font=('Bold',20))
    lbl.pack()
    #place(x=50,y=20)

    yes_btn = Button(
        del_user_cnfrm,
        text='Yes',
        fg='Green',
        width=4,height=2,
        command=lambda:delete_users_back(username,del_user_cnfrm,adminObj)
        )
    yes_btn.place(x=130,y=40)

    no_btn = Button(
        del_user_cnfrm,
        text='No',
        fg='red',
        width=4,height=2,
        command=lambda:[closeWindow(del_user_cnfrm),delete_users_Front_S1(adminObj)]
    )
    no_btn.place(x=220,y=40)

def delete_users_Front_S1(adminObj):
    
    del_user_wind = Tk()

    del_user_wind.title('Delete Users')

    del_user_wind.resizable(width=False,height=False)

    lbl = Label(del_user_wind,text='Choose the User You want to Delete')
    lbl.config(font=('Italic',20))
    lbl.pack()
    
    select_username = """SELECT UserName FROM Users"""

    username_list_tup = connection.execute(select_username)

    username_list = []

    for i in username_list_tup:
        username_list.append(i[0])

    for username in username_list:
        btn = Button(
            del_user_wind,
            text=username,
            command=lambda username = username :[closeWindow(del_user_wind),delete_users_Front_S2(username,adminObj)]
        )
        btn.pack()

    back_btn = Button(
        del_user_wind,
        text='Go Back',
        fg='red',
        # width=4,height=2,
        command=lambda:[closeWindow(del_user_wind),admin_dashboard(adminObj)]
    )
    back_btn.pack()

def add_admin_Back(un,p,fn,ln,a,ad,pn,e,window,CurrentAdminObj):

    UserName = un.get()
    Password = p.get()
    FirstName = fn.get()
    Lastname = ln.get()
    Age = a.get()
    Adress = ad.get()
    PhoneNumber = pn.get()
    Email = e.get()

    try:

        insert = """INSERT INTO Admins VALUES (?,?,?,?,?,?,?,?)"""

        data_tuple = (UserName,Password,FirstName,Lastname,Age,Adress,PhoneNumber,Email)

        cursor.execute(insert,data_tuple)

        connection.commit()

        lbl = Label(window,text='Admin Registery Succesfull',fg='Green')
        lbl.pack()

    except sqlite3.IntegrityError:

        print('error')

        add_admin_Front(CurrentAdminObj,True,UserName)

def add_admin_Front(adminObj,check=False,usnam=''):

    admin_registery_wind = Tk()

    admin_registery_wind.title('Admin Registery')

    admin_registery_wind.geometry('350x500')

    admin_registery_wind.resizable(width=False,height=False)

    if check:
        error_lbl = Label(admin_registery_wind,text=f'UserName {usnam} is Already Taken',fg='red')
        error_lbl.pack()

    username_entry = Entry(admin_registery_wind)
    username_lbl = Label(admin_registery_wind,text='enter new admin\'s username')
    username_lbl.pack()
    username_entry.pack()
    
    pass_entry = Entry(admin_registery_wind)
    pass_lbl = Label(admin_registery_wind,text='enter new admin\'s password')
    pass_lbl.pack()
    pass_entry.pack()

    FName_entry = Entry(admin_registery_wind)
    FName_lbl = Label(admin_registery_wind,text='enter new admin\'s first name')
    FName_lbl.pack()
    FName_entry.pack()

    LName_entry = Entry(admin_registery_wind)
    LName_lbl = Label(admin_registery_wind,text='enter new admin\'s last name')
    LName_lbl.pack()
    LName_entry.pack()

    age_entry = Entry(admin_registery_wind)
    age_lbl = Label(admin_registery_wind,text='enter new admin\'s age')
    age_lbl.pack()
    age_entry.pack()

    adress_entry = Entry(admin_registery_wind)
    adress_lbl = Label(admin_registery_wind,text='enter new admin\'s adress')
    adress_lbl.pack()
    adress_entry.pack()

    Pnum_entry = Entry(admin_registery_wind)
    Pnum_lbl = Label(admin_registery_wind,text='enter new admin\'s phone number')
    Pnum_lbl.pack()
    Pnum_entry.pack()

    email_entry = Entry(admin_registery_wind)
    email_lbl = Label(admin_registery_wind,text='enter new admin\'s email adress')
    email_lbl.pack()
    email_entry.pack()

    cnfrm = Button(
        admin_registery_wind,
        text='Confirm!',
        fg='Green',
        command=lambda:add_admin_Back(
            username_entry,
            pass_entry,
            FName_entry,
            LName_entry,
            age_entry,
            adress_entry,
            Pnum_entry,
            email_entry,
            admin_registery_wind,
            adminObj
        )
    )
    cnfrm.pack()

    back_btn = Button(
        admin_registery_wind,
        text='Go Back',
        # width=4,height=2,
        command=lambda:[closeWindow(admin_registery_wind),admin_dashboard(adminObj)]
    )
    back_btn.pack()

def admin_dashboard(adminObj,just_loged_in=False):

    admin_wind = Tk()

    admin_wind.title('Admin Dashboard')

    admin_wind.geometry('350x450')

    admin_wind.resizable(width=False,height=False)

    if just_loged_in:

        lbl = Label(admin_wind,text=f'Login Completed',fg='Green')
        lbl.grid(row=0,column=0)

        lbl2 = Label(admin_wind,text=f'welcome {adminObj.FirstName} {adminObj.LastName}')
        lbl2.grid(row=1,column=0)

    view_users_btn = Button(
        admin_wind,
        text='View Users',
        width=12,height=2,
        command=lambda:[closeWindow(admin_wind),view_users_Front(adminObj)]
    )
    view_users_btn.grid(row=3,column=0)

    delete_users_btn = Button(
        admin_wind,
        text='Delete Users',
        width=12,height=2 ,
        command=lambda:[closeWindow(admin_wind),delete_users_Front_S1(adminObj)]
    )
    delete_users_btn.grid(row=4,column=0)

    add_admin_btn = Button(
        admin_wind,
        text='Add Admin',
        width=12,height=2,
        command=lambda:[closeWindow(admin_wind),add_admin_Front(adminObj)]
    )
    add_admin_btn.grid(row=5,column=0)

    view_info_btn = Button(
        admin_wind,
        text='View Personal Info',
        width=12,height=2,
        command=lambda:[closeWindow(admin_wind),View_Personal_Info(adminObj,True)]
    )
    view_info_btn.grid(row=6,column=0)

    edit_info_btn = Button(
        admin_wind,
        text='Edit Personal Info',
        width=12,height=2,
        command=lambda:[closeWindow(admin_wind),edit_personal_info_S1(adminObj,True)]
    )
    edit_info_btn.grid(row=7,column=0)

    close_app_btn = Button(
        admin_wind,text='Close Application',
        width=12,height=2,
        command=lambda:closeWindow(admin_wind)
    )
    close_app_btn.grid(row=8,column=0)

    #view users
    #delete users
    #add admin
    #view personal info
    #edit personal info

def admin_login_Back(un_entry,pass_entry,previous_window):

    username = un_entry.get()
    password = pass_entry.get()

    previous_window.destroy()

    select_username = """SELECT UserName FROM Admins"""

    username_list_tup = connection.execute(select_username)

    username_list = []

    for i in username_list_tup:
        username_list.append(i[0])

    if username in username_list:
        username_check = True
    else:
        username_check = False

    if username_check:

        select_password = """SELECT Password FROM Admins"""

        password_list_tup = connection.execute(select_password)

        password_list = []

        for i in password_list_tup:
            password_list.append(i[0])

        if password in password_list:
            password_check = True
        else:
            password_check = False

        if password_check:

            select_user = """SELECT * FROM Admins WHERE UserName=?"""

            data_tup = (username,)

            selected_user_loc = cursor.execute(select_user,data_tup)

            selected_user_list_tup = selected_user_loc.fetchall().copy()

            selected_user_tup = selected_user_list_tup[0]

            (un,p,fn,ln,a,ad,pn,e) = selected_user_tup

            admin = Classes.Admins(un,p,fn,ln,a,ad,pn,e)

            admin_dashboard(admin,True)

        else:
            admin_login_Front(username_check,password_check)
    
    else:
        admin_login_Front(username_check)

def admin_login_Front(username_check=True,password_check=True):

    AdminLogin_wind = Tk()

    AdminLogin_wind.title('Admin Log In')

    AdminLogin_wind.geometry('300x300')

    if not username_check:
        username_error_lbl = Label(AdminLogin_wind,text='Username Not Found',fg='red')
        username_error_lbl.pack()
    elif not password_check:
        password_error_lbl = Label(AdminLogin_wind,text='Wrong Password!',fg='red')
        password_error_lbl.pack()

    username_lbl = Label(AdminLogin_wind,text='enter your username')
    username_lbl.pack()
    username_entry = Entry(AdminLogin_wind)
    username_entry.pack()

    password_lbl = Label(AdminLogin_wind,text='enter your password')
    password_lbl.pack()
    password_entry = Entry(AdminLogin_wind)
    password_entry.pack()

    confirm_btn = Button(
        AdminLogin_wind,
        text='Confirm',
        fg='Green',
        command=lambda:admin_login_Back(username_entry,password_entry,AdminLogin_wind)
    )
    confirm_btn.pack()

connection = sqlite3.connect(
    '/Users/karan/Desktop/codes/Python/project graphic and database/MyDataBase.db')

cursor = connection.cursor()

# user_table = """CREATE TABLE Users(
#     UserName TEXT PRIMARY KEY NOT NULL,
#     Password TEXT NOT NULL,
#     FirstName TEXT NOT NULL,
#     Lastname TEXT NOT NULL,
#     Age TEXT NOT NULL,
#     Adress TEXT NOT NULL,
#     PhoneNumber TEXT NOT NULL,
#     Email TEXT NOT NULL
#     );"""

# connection.execute(user_table)

# admin_table = """CREATE TABLE Admins(
#         UserName TEXT PRIMARY KEY NOT NULL,
#         Password TEXT NOT NULL,
#         FirstName TEXT NOT NULL,
#         Lastname TEXT NOT NULL,
#         Age TEXT NOT NULL,
#         Adress TEXT NOT NULL,
#         PhoneNumber TEXT NOT NULL,
#         Email TEXT NOT NULL
#         );"""
    
# connection.execute(admin_table)

opening_window = Tk()

opening_window.title('Project Application')

opening_window.geometry('500x300')

opening_window.resizable(width=False,height=False)

welcome_lbl = Label(opening_window,text='welcome to your application')
welcome_lbl.config(font=('Bold',40))
welcome_lbl.pack()

choice_lbl = Label(opening_window,text='Please Choose whether you want to enter as an admin or a user')
choice_lbl.pack()

admin_btn = Button(
    opening_window,
    text='Admin',
    width=4,height=2,
    command=lambda:[closeWindow(opening_window),admin_login_Front()]
)
admin_btn.pack()

user_btn = Button(
    opening_window,
    text='User',
    width=4,height=2,
    command=lambda:[closeWindow(opening_window),user_entry()]
)
user_btn.pack()


opening_window.mainloop()