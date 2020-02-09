from tkinter import *
from datetime import datetime,date
from PIL import Image,ImageTk
import pandas as pd
from tkinter import messagebox as mb
import speech_recognition as sr
from selenium import webdriver
import requests
import bs4
import time
from gtts import gTTS
import os


def login(root):
        t1 = StringVar()
        t2 = StringVar()
        t3 = IntVar()
        t4 = IntVar()
        t5=IntVar()
        t6=IntVar()
        t7 = IntVar()
        t8=StringVar()
        t9=StringVar()
        t10=StringVar()
        t11=StringVar()

        def register_user():

                def add_new_user():
                        name = t1.get()
                        user_name = t2.get()
                        user_id = t3.get()
                        admin_code = t4.get()
                        password = t9.get()
                        data1 = [[name, user_name, password, user_id]]
                        if admin_code == 1234:
                                if (user_id < 100000 or user_id > 999999):
                                        mb.showerror('ERROR', 'ID CAN BE ONLY A SIX DIGIT NUMBER')
                                else:
                                        df = pd.read_csv('admins.csv')
                                        df1 = pd.DataFrame(data1, columns=['NAME', 'USERNAME', 'PASSWORD', 'ID'])
                                        df = df.append(df1, ignore_index=True)
                                        df.to_csv('admins.csv', index=False)
                                        print(df)
                                        mb.showinfo('SUCCESSFUL', '    REGISTRATION SUCCESSFUL!   ')
                                        top.grab_release()
                                        top.destroy()
                        else:
                                mb.showerror('ERROR', 'INVALID ADMIN CODE')


                top=Toplevel()
                top.title('New Register')
                top.geometry('600x500')
                top.maxsize(600, 500)
                top.minsize(600, 500)
                top.grab_set()

                photos = []
                photo = Image.open("booki1.png")
                photo = photo.resize((600, 500), Image.ANTIALIAS)
                photos.append((ImageTk.PhotoImage(photo)))
                Label(top, image=photos[0]).place(x=0, y=0, relwidth=1, relheight=1)

                Label(top, text='Name          :', font='arial 15 bold', bg='white').place(x=50, y=80)
                Entry(top, textvariable=t1, width=15, font='arial 15').place(x=200, y=80)
                Label(top, text='User Name  :', font='arial 15 bold', bg='white').place(x=50, y=140)
                Entry(top, textvariable=t2, width=15, font='arial 15').place(x=200, y=140)
                Label(top, text='User Id        :', font='arial 15 bold', bg='white').place(x=50, y=200)
                Entry(top, textvariable=t3, width=15, font='arial 15').place(x=200, y=200)
                Label(top, text='Admin Code:', font='arial 15 bold', bg='white').place(x=50, y=260)
                Entry(top, textvariable=t4, width=15, font='arial 15').place(x=200, y=260)
                Label(top, text='Password    :', font='arial 15 bold', bg='white').place(x=50, y=320)
                Entry(top, textvariable=t9, width=15, font='arial 15').place(x=200, y=320)

                Button(top, text='Register', font='arial 17 bold', relief=SOLID, bg='skyblue',activebackground='#FFA500',command=add_new_user).place(x=255, y=390)
                t3.set('')
                t4.set('')
                # Button(root, text='Login Page', font='arial 15', bg='yellow', activebackground='#FFA500').place(x=0, y=0)
                top.mainloop()


        def login_user():

                def logout():
                        s1.set('')
                        s2.set('')
                        toplo = Toplevel()
                        x = toplo.winfo_screenwidth()
                        y = toplo.winfo_screenwidth()
                        toplo.title('Login')
                        toplo.geometry('%dx%d' % (x, y))
                        top2.destroy()
                        t = 0
                        while t < 6:
                                toplo.rowconfigure(t, weight=1)
                                toplo.columnconfigure(t, weight=1)
                                t += 1

                        l2 = Label(toplo, text="Andaman College Library Management System", font='arial 40 bold',fg='black',bg='#3BFF00')
                        l2.pack(fill=X)
                        lf1 = LabelFrame(toplo, text="Login", font='comic-sans 30 bold', fg='black', bg='yellow',borderwidth=4,relief=SOLID)
                        l1 = Label(lf1, text='USERNAME :', fg='black', bg='yellow', height=3, font='comic-sans 20 bold')
                        l1.grid(row=3, column=1, padx=20)
                        l1 = Label(lf1, text='PASSWORD :', bg='yellow', fg='black', height=3, font='comic-sans 20 bold')
                        l1.grid(row=5, column=1)
                        username = Entry(lf1, font='arial 20', relief=RAISED, borderwidth=3, textvariable=s1).grid(row=2,column=3,columnspan=6,rowspan=2)
                        password = Entry(lf1, show="*", font='arial 20', relief=RAISED, borderwidth=3,textvariable=s2).grid(row=5, column=3, columnspan=6, rowspan=3, padx=20)
                        b1 = Button(lf1, text='LOGIN', width=10, font='arial 20', relief=RAISED, borderwidth=6,activebackground="#0082FF", command=login_user).grid(row=9, column=1, columnspan=3,rowspan=6, pady=10)
                        b1 = Button(lf1, text='REGISTER', width=15, font='arial 20', relief=RAISED, borderwidth=6,activebackground="#0082FF", command=register_user).grid(row=9, column=4,columnspan=3,rowspan=6, pady=10, padx=10)
                        lf1.place(x=500, y=200)
                        today = date.today()
                        d2 = today.strftime("%B %d, %Y")
                        l4 = Label(toplo, text=d2, font='arial 25 bold', fg='black')
                        l4.place(x=100, y=600)
                        toplo.mainloop()

                log=False
                username = s1.get()
                password = s2.get()
                df = pd.read_csv('admins.csv')
                for i in df['USERNAME']:
                        if username == i:
                                for j in df['PASSWORD']:
                                        if password == j:
                                                log = True
                                                break
                                        else:
                                                log = False
                if log == False:
                        mb.showerror('ERROR', 'USERNAME/PASSWORD IS INVALID')
                else:
                        top2=Toplevel()
                        top2.title("Home")
                        x = top2.winfo_screenwidth()
                        y = top2.winfo_screenwidth()
                        top2.geometry('%dx%d' % (x, y))
                        topl.destroy()
                        t = 0
                        while t < 100:
                                top2.rowconfigure(t, weight=600)
                                top2.columnconfigure(t, weight=600)
                                t += 1

                        photos = []
                        photo = Image.open('booki1.png')
                        photo = photo.resize((1600, 850), Image.ANTIALIAS)
                        photos.append(ImageTk.PhotoImage(photo))
                        Label(top2, image=photos[0]).place(x=0, y=0, relwidth=1, relheight=1)

                        # f=Frame(root,bg='#177ce2',width=2000,height=1000)
                        Label(top2, text='ANDAMAN  COLLEGE  LIBRARY', font='gabriola 40 bold', bg='white',fg='black').place(x=220, y=0)

                        Button(top2, text='Logout', font='comic-sans 20 bold', bg='white', activebackground='#6ba2f4',borderwidth=5,command=logout).place(x=0, y=740)

                        # f0 = Frame(root, width = 1000, height = 100)
                        Button(top2, text='ISSUE BOOK', font='comic-sans 20 bold', height=2, width=15, bg='white',fg='black', activebackground='#6ba2f4', command=issue_book, borderwidth=5).place(x=140,y=150)  # grid(pady = 20, padx = 200)
                        Button(top2, text='RETURN BOOK', font='comic-sans 20 bold', height=2, width=15, bg='white',activebackground='#6ba2f4', command=return_book, fg='black', borderwidth=5).place(x=140,y=320)  # grid(row = 1, column = 0, pady = 20, padx =200)
                        Button(top2, text='SEARCH BOOK IN\n LIBRARY', font='comic-sans 20 bold', height=3, width=15,bg='white', activebackground='#6ba2f4', command=search_lib, fg='black', borderwidth=5).place(x=140, y=490)  # grid(row = 2, column = 0,pady = 20, padx = 200)
                        Button(top2, text='SEARCH BOOK\n ONLINE', font='comic-sans 20 bold', height=3, width=15,bg='white', activebackground='#6ba2f4', command=searchon, fg='black', borderwidth=5).place(x=600, y=490)  # grid(row = 2, column = 1,pady = 20, padx = 200)
                        Button(top2, text='STUDENT RECORD', font='comic-sans 20 bold', height=2, width=15, bg='white',activebackground='#6ba2f4', fg='black', borderwidth=5).place(x=600,y=320)  # grid(row = 1, column = 1,pady = 20, padx = 200)
                        Button(top2, text='INVENTORY', font='comic-sans 20 bold', height=2, width=15, bg='white',activebackground='#6ba2f4', fg='black', borderwidth=5).place(x=600,y=150)  # grid(row = 0, column = 1,pady = 20, padx = 200)
                        # f0.place(x = 100, y = 150)
                        # f.place(x=0,y=0)

                        top2.mainloop()


        def issue_book():

                def issue():
                        book_id = t5.get()
                        student_id = t6.get()
                        student_name = t10.get()
                        today = date.today()
                        d2 = today.strftime("%d/%m/%Y")
                        data1 = [[book_id, student_id, d2]]
                        df3 = pd.read_csv('issue_book.csv')
                        df4 = pd.DataFrame(data1, columns=['Book_ID', 'Student_Name', 'Student_ID', 'Issue_Date'])
                        df3 = df3.append(df4, ignore_index=True)
                        df3.to_csv('issue_book.csv', index=False)
                        mb.showinfo('SUCCESSFUL', '    BOOK ISSUED SUCCESSFULLY!   ')
                        top3.grab_release()


                top3=Toplevel()

                top3.title('Issue Book')
                top3.geometry('600x400')
                top3.maxsize(600, 400)
                top3.minsize(600, 400)
                top3.grab_set()

                photos = []
                photo = Image.open("booki1.png")
                photo = photo.resize((600, 500), Image.ANTIALIAS)
                photos.append((ImageTk.PhotoImage(photo)))
                Label(top3, image=photos[0]).place(x=0, y=0, relwidth=1, relheight=1)

                Label(top3, text='Book ID :', font='arial 15 bold').place(x=50, y=110)
                Entry(top3, textvariable=t5, width=15, font='arial 15').place(x=210, y=110)
                Label(top3, text='Student Name :', font='arial 15 bold').place(x=50, y=150)
                Entry(top3, textvariable=t10, width=15, font='arial 15').place(x=210, y=150)
                Label(top3, text='Student ID :', font='arial 15 bold').place(x=50, y=190)
                Entry(top3, textvariable=t6, width=15, font='arial 15').place(x=210, y=190)
                Button(top3, text='Issue', font='arial 17 bold', bg='skyblue', activebackground='#FFA500',command=issue).place(x=300,y=240)
                Button(top3, text='Home', font='arial 15', bg='skyblue', activebackground='#FFA500').place(x=0, y=0)
                t5.set('')
                t6.set('')
                top3.mainloop()




        def return_book():

                def returnbook():
                        book_id = t7.get()
                        c = -1
                        d = 0

                        df = pd.read_csv('issue_book.csv')
                        print(len(df.index))
                        for i in df['Book_ID']:
                                c = c + 1

                                if book_id == i:
                                        df.drop(c, inplace=True)
                                        print(df)
                                        df.to_csv('issue_book.csv', index=False)
                                        mb.showinfo('SUCCESSFUL', '    BOOK RETURNED SUCCESSFULLY!   ')
                                        top4.grab_release()
                                        top4.destroy()
                                        d = 1
                                        break
                                elif d == 0 and c+1 == len(df.index):
                                        mb.showerror('ERROR', "THIS BOOK WAS NOT ISSUED")
                                        top4.grab_release()
                                        top4.destroy()

                top4=Toplevel()
                top4.title('Return Book')
                top4.geometry('600x400')
                top4.maxsize(600, 400)
                top4.minsize(600, 400)
                top4.grab_set()

                photos = []
                photo = Image.open("booki1.png")
                photo = photo.resize((600, 500), Image.ANTIALIAS)
                photos.append((ImageTk.PhotoImage(photo)))
                Label(top4, image=photos[0]).place(x=0, y=0, relwidth=1, relheight=1)

                # Label(root, text='Search Book Online',font = 'Arial-Narrow 30 italic').place(x=80,y=0)
                Label(top4, text='Book Id :', font='arial 15 bold', bg='white').place(x=80, y=120)
                Entry(top4, textvariable=t7, width=15, font='arial 15').place(x=210, y=120)
                Button(top4, text='Return', font='arial 17 bold', relief=SOLID, bg='skyblue',activebackground='#FFA500',command=returnbook).place(x=280, y=220)
                Button(top4, text='Home', font='arial 15', bg='skyblue', activebackground='#FFA500').place(x=0, y=0)
                t7.set('')
                top4.mainloop()









        def search_lib():

                def searchlibonvoice():
                        # The text that you want to convert to audio
                        mytext = 'Which book do you want to search'

                        # Language in which you want to convert
                        language = 'en'

                        myobj = gTTS(text=mytext, lang=language, slow=False)
                        myobj.save("hi.m4a")
                        os.system("hi.m4a")

                        time.sleep(5)
                        st=''
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                                r.adjust_for_ambient_noise(source)
                                print('Say something')
                                audio = r.listen(source)
                                st=st+r.recognize_google(audio)
                                print('TEXT:' + st)
                                t8.set(st)
                                searchlib()


                def searchlib():
                        c = -1
                        bookname = t8.get()
                        bookname = bookname.lower()
                        df = pd.read_csv('SIHbooks.csv')
                        for i in df['Title']:
                                c += 1
                                st = i.lower()

                                if (st == bookname):
                                        print(df.iloc[c])
                                        bookdata = Toplevel()
                                        bookdata.title('BOOK DATA')
                                        bookdata.geometry('400x400')
                                        bookdata.maxsize(400, 400)
                                        bookdata.minsize(400, 400)
                                        Label(bookdata, text=df.iloc[c], font='arial 15', fg='black').place(x=50, y=50)
                                        top5.grab_release()
                                        top5.destroy()
                                        bookdata.mainloop()

                                        break
                                elif c+1 == len(df.index):
                                        mb.showerror('ERROR', "THIS BOOK IS NOT FOUND IN THE LIBRARY")
                                        top5.grab_release()
                                        top5.destroy()

                top5=Toplevel()
                top5.title('Search Book in Library')
                top5.geometry('600x400')
                top5.maxsize(600, 400)
                top5.minsize(600, 400)
                top5.grab_set()

                photos = []
                photo = Image.open("booki1.png")
                photo = photo.resize((600, 500), Image.ANTIALIAS)
                photos.append((ImageTk.PhotoImage(photo)))
                photo = Image.open("12.png")
                photo = photo.resize((32, 40), Image.ANTIALIAS)
                photos.append((ImageTk.PhotoImage(photo)))
                Label(top5, image=photos[0]).place(x=0, y=0, relwidth=1, relheight=1)

                Label(top5, text='Book Name :', font='arial 15 bold').place(x=50, y=130)
                Entry(top5, textvariable=t8, width=15, font='arial 15').place(x=210, y=130)
                Button(top5, text='Search', font='arial 17 bold', bg='skyblue', activebackground='#FFA500',command=searchlib).place(x=280,y=190)
                Button(top5, text='Home', font='arial 15', bg='skyblue', activebackground='#FFA500').place(x=0, y=0)
                Button(top5, image=photos[1],command=searchlibonvoice).place(x=210, y=190)

                top5.mainloop()







        def searchon():


                def searchnetonvoice():

                        # The text that you want to convert to audio
                        mytext = 'Which book do you want to search'

                        # Language in which you want to convert
                        language = 'en'

                        myobj = gTTS(text=mytext, lang=language, slow=False)
                        myobj.save("hi.m4a")
                        os.system("hi.m4a")

                        time.sleep(5)
                        st=''
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                                r.adjust_for_ambient_noise(source)
                                print('Say something')
                                audio = r.listen(source)
                                st=st+r.recognize_google(audio)
                                print('TEXT:' + st)
                                t11.set(st)
                                searchnet()


                def searchnet():
                        st = t11.get()
                        c = 0

                        driver = webdriver.Chrome("C:\\Users\Asus\PycharmProjects\SIH\\venv\chromedriver.exe")
                        driver.get('https://books.google.co.in/')
                        time.sleep(3)

                        search_box = driver.find_element_by_xpath('//*[@id="oc-search-input"]')
                        search_box.send_keys(st)
                        time.sleep(1)

                        # To Automate the process of searching
                        search_button = driver.find_element_by_xpath('//*[@id="oc-search-button"]/input')
                        time.sleep(2)
                        search_button.click()

                        # to extract the url of a link

                        urls = driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[1]/div/div/div[1]/a/h3')
                        urls.click()
                        url1 = driver.current_url
                        try:
                                button1 = driver.find_element_by_xpath('//*[@id="sidebar-atb-link"]/span')
                                button1.click()
                        except:
                                pass

                        url = driver.current_url

                        # web scraping continues
                        res = requests.get(url)
                        soup = bs4.BeautifulSoup(res.text, 'lxml')
                        soup.select('.metadata_value')

                        for i in soup.select('.metadata_value'):
                                print(i.text)
                                st = st + i.text + '\n'
                        time.sleep(5)
                        driver.quit()
                        top6.grab_release()
                        top6.destroy()
                        bookdata = Toplevel()
                        bookdata.title('BOOK DATA')
                        x = bookdata.winfo_screenwidth()
                        y = bookdata.winfo_screenwidth()
                        bookdata.geometry('%dx%d' % (x, y))
                        Label(bookdata, text=st, font='arial 15', fg='black').place(x=50, y=50)
                        bookdata.mainloop()


                top6=Toplevel()
                top6.title('Search Book Online')
                top6.geometry('600x400')
                top6.maxsize(600, 400)
                top6.minsize(600, 400)
                top6.grab_set()

                photos = []
                photo = Image.open("booki1.png")
                photo = photo.resize((600, 500), Image.ANTIALIAS)
                photos.append((ImageTk.PhotoImage(photo)))
                photo = Image.open("12.png")
                photo = photo.resize((32, 40), Image.ANTIALIAS)
                photos.append((ImageTk.PhotoImage(photo)))
                Label(top6, image=photos[0]).place(x=0, y=0, relwidth=1, relheight=1)

                # Label(root, text='Search Book Online',font = 'Arial-Narrow 30 italic').place(x=80,y=0)
                Label(top6, text='Book Name :', font='arial 15 bold').place(x=50, y=160)
                Entry(top6, textvariable=t11, width=15, font='arial 15').place(x=210, y=160)
                Button(top6, text='Search', font='arial 17 bold', bg='skyblue', activebackground='#FFA500',command=searchnet).place(x=280,y=220)
                Button(top6, text='Home', font='arial 15', bg='skyblue', activebackground='#FFA500').place(x=0, y=0)
                Button(top6, image=photos[1],command=searchnetonvoice).place(x=210, y=220)
                top6.mainloop()








        root.withdraw()
        topl=Toplevel()
        x = topl.winfo_screenwidth()
        y = topl.winfo_screenwidth()
        topl.title('Login')
        topl.geometry('%dx%d' % (x, y))
        t = 0
        while t<6:
                topl.rowconfigure(t, weight=1)
                topl.columnconfigure(t, weight=1)
                t+=1

        l2=Label(topl,text="Andaman College Library Management System",font='arial 40 bold',fg='black',bg='#3BFF00')
        l2.pack(fill=X)
        lf1=LabelFrame(topl,text="Login",font='comic-sans 30 bold',fg='black',bg='yellow',borderwidth=4,relief=SOLID)
        l1=Label(lf1,text='USERNAME :',fg='black',bg='yellow',height=3,font='comic-sans 20 bold')
        l1.grid(row=3,column=1,padx=20)
        l1=Label(lf1,text='PASSWORD :',bg='yellow', fg='black',height=3,font='comic-sans 20 bold')
        l1.grid(row=5,column=1)
        username=Entry(lf1,font='arial 20',relief=RAISED,borderwidth=3,textvariable=s1).grid(row=2,column=3,columnspan=6,rowspan=2)
        password=Entry(lf1,show="*",font='arial 20',relief=RAISED,borderwidth=3,textvariable=s2).grid(row=5,column=3,columnspan=6,rowspan=3,padx=20)
        b1=Button(lf1,text='LOGIN',width=10,font='arial 20',relief=RAISED,borderwidth=6,activebackground="#0082FF",command=login_user).grid(row=9,column=1,columnspan=3,rowspan=6,pady=10)
        b1=Button(lf1,text='REGISTER',width=15,font='arial 20',relief=RAISED,borderwidth=6,activebackground="#0082FF",command=register_user).grid(row=9,column=4,columnspan=3,rowspan=6,pady=10,padx=10)
        lf1.place(x=500,y=200)
        today = date.today()
        d2 = today.strftime("%B %d, %Y")
        l4=Label(topl,text=d2,font='arial 25 bold',fg='black')
        l4.place(x=100,y=600)
        topl.mainloop()

root=Tk()
root.title('SYSTEM')
x = root.winfo_screenwidth()
y = root.winfo_screenwidth()
root.geometry('%dx%d' % (x, y))
s1=StringVar()
s2=StringVar()
login(root)
