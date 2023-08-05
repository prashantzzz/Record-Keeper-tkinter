from tkinter import *
import winsound, time, sys,pickle
from datetime import datetime
from win32api import GetSystemMetrics

dict1={'1': 'rr', '2': 'ry', '3': 'ri', '4': 'ryy', '5': 'ro', '6': 'or', '7': 'yr', '8': 'yii', '9': 'ir',
       '0': 'yy', 'q': 'ii', 'w': 'idd', 'e': 'oo', 'r': 'rp', 't': 'rd', 'y': 'rf', 'u': 'ohh', 'i': 'rh', 'o': 'pr',
       'p': 'dr', 'a': 'pff', 's': 'fr', 'd': 'hr', 'f': 'pp', 'g': 'doo', 'h': 'dd', 'j': 'ff', 'k': 'hh', 'l': 'yi',
       'z': 'frr', 'x': 'iy', 'c': 'yo', 'v': 'oy', 'b': 'hpp', 'n': 'yp', 'm': 'py'}
allowed=['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s',
         'd','f','g','h','j','k','l','z','x','c','v','b','n','m']
encrypt=[]

f=open(r"C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\records.txt",'r')
text1=f.readlines()
f.close()

def check(listname,x):
    if (x+'\n') in listname:
        return True
    else:
        return False
    
def bregisterpage_hover(e):
    global bregisterpage_image
    bregisterpage_image=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\b2.2-min.png')
    bregisterpage.config(image=bregisterpage_image)
    #winsound.PlaySound('chord.wav', winsound.SND_ASYNC)

def bregisterpage_leave(e):
    global bregisterpage_image
    bregisterpage_image=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\b2.1-min.png')
    bregisterpage.config(image=bregisterpage_image)

def bloginpage_leave(e):
    global bloginpage_image
    bloginpage_image=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\b3.1-min.png')
    bloginpage.config(image=bloginpage_image)

def bloginpage_hover(e):
    global bloginpage_image
    bloginpage_image=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\b3.2-min.png')
    bloginpage.config(image=bloginpage_image)

def bquit_hover(e):
    global bquit_image
    bquit_image=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\b4.2-min.png')
    bquit.config(image=bquit_image)

def bquit_leave(e):
    global bquit_image
    bquit_image=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\b4.1-min.png')
    bquit.config(image=bquit_image)

def blogin_hover(e):
    global image_login
    image_login=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\b1.2-min.png')
    blogin.config(image=image_login)

def blogin_leave(e):
    global image_login
    image_login=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\b1.1-min.png')
    blogin.config(image=image_login)

def bregisterpage2_hover(e):
    global bregisterpage2
    bregisterpage2.config(font='areal 8 underline',fg='blue')

def bregisterpage2_leave(e):
    global bregisterpage2
    bregisterpage2.config(font='areal 8',fg='black')

def bback2_hover(e):
    global image_bback2
    image_bback2=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\back1.2-min.png')
    bback2.config(image=image_bback2)
    bback2.place(x=10,y=12)

def bback2_leave(e):
    global image_bback2
    image_bback2=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\back1.1-min.png')
    bback2.config(image=image_bback2)
    bback2.place(x=15,y=15)

def bback_hover(e):
    global image_bback
    image_bback=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\back1.2-min.png')
    bback.config(image=image_bback)
    bback.place(x=10,y=12)

def bback_leave(e):
    global image_bback
    image_bback=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\back1.1-min.png')
    bback.config(image=image_bback)
    bback.place(x=15,y=15)

def bregister_hover(e):
    global bregister_image
    bregister_image=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\b5.2-min.png')
    bregister.config(image=bregister_image)

def bregister_leave(e):
    global bregister_image
    bregister_image=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\b5.1-min.png')
    bregister.config(image=bregister_image)

def register_enter(e):
    register()
def login_enter(e):
    login()
        
breg_movex=240
blog_movex=242
bquit_movex=247
inmovex=699
inmovey=0

def bretreat_reg(e):
    global pressed
    pressed='reg'
    bretreat()
def bretreat_login(e):
    global pressed
    pressed='login'
    bretreat()

def bretreat():
    global bregisterpage, bloginpage, bquit,photo1_2,pressed
    breg_movex=240
    blog_movex=242
    bquit_movex=247
    inmovex,inmovey=563,136
    for i in range(40):
        if inmovey<=1100:
            photo1_2.place(x=inmovex,y=inmovey)
            inmovex+=20
            inmovey-=20
        if breg_movex>190:
            bregisterpage.place(x=breg_movex,y=232)
            breg_movex-=30
            bregisterpage.update()
        elif 140<breg_movex<=190:
            bregisterpage.place(x=breg_movex,y=232)
            bloginpage.place(x=blog_movex,y=337)
            breg_movex-=30
            blog_movex-=30
            bregisterpage.update()
            bloginpage.update()
        elif -450<breg_movex<=140:
            bregisterpage.place(x=breg_movex,y=232)
            bloginpage.place(x=blog_movex,y=337)
            bquit.place(x=bquit_movex,y=435)
            breg_movex-=30
            blog_movex-=30
            bquit_movex-=30
            bregisterpage.update()
            bloginpage.update()
            bquit.update()
        root.update()
    if pressed=='reg': register_win()
    elif pressed=='login': login_win()

def fade_quit():
    global close
    close = True
    tp = 1
    while tp >= 0:
        root.attributes('-alpha', tp)
        time.sleep(0.01)
        root.update()
        tp -= 0.03
    root.destroy()

def cur_time():
    global now,dt_str,tm_str,b1,time1
    now = datetime.now()    
    dt_str = now.strftime("%d/%m")
    time1=Label(root)

    while not close:
        time1.config(text='')
        now = datetime.now()

        t=now.strftime('%H')
        if int(t)<=12:
            am_pm='AM'
            H=str(int(t))
        elif int(t)>12:
            am_pm='PM'
            H=str(int(t)-12)

        dt_string = now.strftime(f"%d %B | {H}:%M {am_pm}")
        
        time1=Label(root,text=dt_string,font='arial 12 bold',bg='#f9ffff',fg='purple')
        time1.place(x=820,y=10)
        time1.update()
    try:root.update()
    except:pass

def welcome():
  try:
    global bregisterpage, bloginpage, bregisterpage_image, bloginpage_image,bquit,bquit_image
    global image1_1, image1_2, photo1_2, photo1_1,time1
    #original xcor=240,242,247
    breg_movex=-200
    blog_movex=-200
    bquit_movex=-200
    inmovex,inmovey=699,0 
    image1_1=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\bg2-min.png')
    photo1_1=Label(image=image1_1)
    photo1_1.place(x=0,y=0)
    root.update()

    image1_2=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\in-min.png')
    
    photo1_2=Label(image=image1_2)
    
    
    bregisterpage_image=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\b2.1-min.png')
    bloginpage_image=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\b3.1-min.png')
    bquit_image=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\b4.1-min.png')
    #bg='#f9ffff' , '#2ba6a6' , '#3a0440'
    #cursors= arrow, pencil, circle, clock, cross, dotbox, exchange, fleur, man, mouse, pirate, plus, sizing,
    #              shuttle, spider, spraycanstar,target,tcross,trek,watch,box_spiral, rtl_logo, sailboat, hand1
    bregisterpage=Button(activebackground='#f9ffff',cursor='hand2',image=bregisterpage_image,border=0,command=register_win)
    bloginpage=Button(activebackground='#f9ffff',cursor='hand2',image=bloginpage_image,border=0, command=login_win)
    bquit=Button(activebackground='#f9ffff',cursor='hand2',image=bquit_image,border=0,command=fade_quit)
    
           
    bregisterpage.place(x=breg_movex,y=232),bloginpage.place(x=blog_movex,y=337)
    bquit.place(x=bquit_movex,y=435)
    for i in range (40):
        photo1_2.place(x=inmovex,y=inmovey)
        inmovex-=3.4
        inmovey+=3.4
        
        if breg_movex<40: #413
            bregisterpage.place(x=breg_movex,y=232)
            breg_movex+=25
            bregisterpage.update()
        elif 40<=breg_movex<100:
            bregisterpage.place(x=breg_movex,y=232)
            bloginpage.place(x=blog_movex,y=337)
            breg_movex+=25
            blog_movex+=25
            bregisterpage.update(),bloginpage.update()

        elif 100<=breg_movex:
            bregisterpage.place(x=breg_movex,y=232)
            bloginpage.place(x=blog_movex,y=337)
            bquit.place(x=bquit_movex,y=435)
            if breg_movex<240:
                breg_movex+=25
                blog_movex+=25
                bquit_movex+=25
            elif breg_movex>=240 and blog_movex<240:
                blog_movex+=25
                bquit_movex+=25
            elif breg_movex>=240 and blog_movex>=240 and bquit_movex<240:
                bquit_movex+=25
            bregisterpage.update()
            bloginpage.update()
            bquit.update()
            root.update()
    photo1_2.place(x=563,y=136)
    bregisterpage.place(x=240,y=232),bloginpage.place(x=242,y=337)
    bquit.place(x=247,y=435)
    #event handling:
    bregisterpage.bind('<Enter>',bregisterpage_hover)
    bregisterpage.bind('<1>',bretreat_reg)
    bregisterpage.bind('<Leave>',bregisterpage_leave)
    bloginpage.bind('<Enter>',bloginpage_hover)
    bloginpage.bind('<1>',bretreat_login)
    bloginpage.bind('<Leave>',bloginpage_leave)
    bquit.bind('<Enter>',bquit_hover)
    bquit.bind('<Leave>',bquit_leave)
    cur_time()
    root.update()
  except:
      print("error occured!")
      pass
    
def register_win():
    global tname,ename,ename_image, tuser1,euser1, tpswd1,epswd1, tmail,email, image2_1,photo2_1
    global bregister,bregister_image, encrypt, bback,image_back
  
    image2_1=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\bg1-min.png')
    bregister_image=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\b5.1-min.png')
    photo1_1.config(image=image2_1)
    root.update()
    image_back=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\back1.1-min.png')
    bback=Button(cursor='hand1',activebackground='#0b6f50',bg='#0b6f50',image=image_back,border=0, command=back1)

    bloginpage.place_forget(),bregisterpage.place_forget(),photo1_2.place_forget(),time1.place_forget()
    bquit.place_forget()

    ename=Entry( relief=RIDGE,border=3,width=25,font='BookAntiqua 15',bg='#f9ffff',fg='#3b0440')
    ename.focus_set()
    euser1=Entry( relief=RIDGE,border=3,width=25,font='BookAntiqua 15',bg='#f9ffff',fg='#2ba6a6')
    epswd1=Entry( relief=RIDGE,border=3,width=25,font='BookAntiqua 15',bg='#f9ffff',fg='#2ba6a6', show='*')
    email=Entry( relief=RIDGE,border=3,width=25,font='BookAntiqua 15',bg='#f9ffff',fg='#3b0440')
    email.insert(0,'@gmail.com')
    bregister=Button(activebackground='#f9ffff',cursor='hand2',image=bregister_image,border=0,bg='#f9ffff',command=register)

    ename.place(x=196,y=200),euser1.place(x=196,y=291),epswd1.place(x=196,y=382)
    email.place(x=196,y=471),bregister.place(x=195,y=520), bback.place(x=15,y=15)

    #event handling:
    bback.bind('<Enter>',bback_hover)
    bback.bind('<Leave>',bback_leave)
    bregister.bind('<Enter>',bregister_hover)
    bregister.bind('<Leave>',bregister_leave)
    ename.bind('<Return>', register_enter)
    euser1.bind('<Return>', register_enter)
    epswd1.bind('<Return>', register_enter)
    email.bind('<Return>', register_enter)
    time1.place(x=820,y=10)
    root.update()

def back1():
    for widgets in root.winfo_children():
        widgets.destroy()
    #euser1.place_forget(),epswd1.place_forget(),ename.place_forget(), photo1_1.config(image=image1_1)
    #bback.place_forget(),email.place_forget(),bregister.place_forget(),time1.place_forget()
    welcome()
    
def register():
    global euser1,ename,epswd1
    tinfo=Label(text='', font='BookAntiqua 15 bold', fg='lightgreen',bg='#37075d')
    if email.get()!='@gmail.com' and ename.get()!='' and euser1.get()!=''  and epswd1.get()!='' and (not check(text1,'Username: '+euser1.get())) and len(epswd1.get())>=5:   
        encrypt=list(epswd1.get() )
        for i in encrypt:
            indx=encrypt.index(i)
            if i in allowed: encrypt[indx]=dict1.get(i)
        
        f=open('records.txt','a+')
        f.write('\n')
        f.write(ename.get()+'\n')
        f.write('Username: '+euser1.get()+'\n')
        f.writelines(encrypt )
        f.write('\n'+'Email: '+email.get()+'\n')
        f.flush(), f.close()

        ename.delete(0,END),euser1.delete(0,END),email.delete(0,END),
        epswd1.delete(0,END),email.insert(0,'@gmail.com')
        tinfo=Label(text='Register Success!        ', font='BookAntiqua 15 bold', fg='lightgreen',bg='#37075d')
        tinfo.update()
        tinfo.place(x=530,y=510)
        time.sleep(0.5)
        login_win()

    if ename.get()=='':
        tinfo.config(text='Enter name                      ', font='BookAntiqua 15', fg='red')
        tinfo.place(x=530,y=510)

    elif ename.get()!='' and (check(text1,'Username: '+euser1.get()) or len(epswd1.get())<5) or len(euser1.get())<5:
        if check(text1,'Username: '+euser1.get()):
            tinfo.config(text='Username already exists  ', font='BookAntiqua 15', fg='red')
            tinfo.place(x=530,y=510)

        elif len(epswd1.get())<5 or len(euser1.get())<5:
            tinfo.config(text='Enter User/Pswd. lenght > 5', font='BookAntiqua 14', fg='red')
            tinfo.place(x=530,y=510)
            
    elif email.get()=='@gmail.com' and ename.get()!='' and euser1.get()!=''  and epswd1.get()!='' and (not check(text1,'Username: '+euser1.get())) and len(epswd1.get())>=5:
        tinfo.config(text='Please enter email              ', font='BookAntiqua 15', fg='red')
        tinfo.place(x=530,y=510)
    root.update()

def login_win():
    global euser1,epswd1,blogin,photo1_3,image_login,image1_3,bregisterpage2, tregister, bback2
    global image_back2

    bloginpage.place_forget(),bregisterpage.place_forget(),photo1_2.place_forget(),time1.place_forget()
    bquit.place_forget()

    image1_3=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\bg3-min.png')
    photo1_1.config(image=image1_3)
    root.update()
    image_login=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\b1.1-min.png')
    
    euser1=Entry(relief=RIDGE,border=3,width=20,font='BookAntiqua 18',bg='#f9ffff',fg='#2ba6a6')
    euser1.focus_set()
    epswd1=Entry(relief=RIDGE,border=3,width=20,font='BookAntiqua 18',bg='#f9ffff',fg='#2ba6a6',show='*')

    tregister=Label(text='Not a member ?',font='arial 10',bg='#f9ffff',fg='#9b9b9b')
    bregisterpage2=Button(activebackground='#f9ffff',cursor='hand2',text= 'Register',border=0,font='arial 8',bg='#f9ffff',fg='black',command=register_win)
    blogin=Button(activebackground='#f9ffff',cursor='hand2',image=image_login,border=0,bg='#f9ffff',command=login)
    image_back2=PhotoImage(file=r'C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\back1.1-min.png')
    bback2=Button(cursor='hand1',image=image_back2,activebackground='#0b6f50',bg='#0b6f50',border=0, command=back1)
    
    blogin.bind('<Enter>',blogin_hover)
    blogin.bind('<Leave>',blogin_leave)
    bregisterpage2.bind('<Enter>',bregisterpage2_hover)
    bregisterpage2.bind('<Leave>',bregisterpage2_leave)
    bback2.bind('<Enter>',bback2_hover)
    bback2.bind('<Leave>',bback2_leave)
    euser1.bind('<Return>', login_enter)
    epswd1.bind('<Return>', login_enter)
    
    euser1.place(x=201,y=273),epswd1.place(x=199,y=362),blogin.place(x=188, y=420)
    tregister.place(x=210,y=525),bregisterpage2.place(x=410,y=526), bback2.place(x=15,y=15)
    time1.place(x=820,y=10)
    root.update()
  
def login():
    global details, encrypt, euser1,ename,epswd1,details,pswd_index,xlist,pswd,indx,blogin
    tinfo=Label(text='', font='BookAntiqua 15 bold', fg='lightgreen',bg='#37075d')
    details=['name','username','email']
    f=open('records.txt','r')
    text1=f.readlines()
    f.close()
    xlist=['\n']
    if check(text1,'Username: '+euser1.get()):
        tinfo.place_forget()
        tinfo.config(text='                                              ',font='BookAntiqua 15 bold', fg='red')
        tinfo.place(x=530,y=510)
        pswd_index=text1.index('Username: '+euser1.get()+'\n')+1
        pswd=text1[pswd_index]  #original password
        
        encrypt=list(epswd1.get() )  
        for i in encrypt:
            indx=encrypt.index(i)
            if i in allowed: encrypt[indx]=dict1.get(i)
        encrypt="".join(encrypt+xlist)     #user entered password added \n because original pswd had \n at its end
    if encrypt==pswd:
        tinfo.config(text='Success                             ', font='BookAntiqua 15 bold', fg='green')
        tinfo.place(x=530,y=510)
    else:
        tinfo.config(text='Incorrect or empty details', font='BookAntiqua 15 bold', fg='red')
        tinfo.place(x=530,y=510)
    root.update()
        
root= Tk()
root.protocol("WM_DELETE_WINDOW",fade_quit)
screen_w=GetSystemMetrics(0)
screen_h=GetSystemMetrics(1)
add=50
w=int(0.746*screen_w)+add
h=int(0.84*screen_h)
root.geometry(f'{w}x{h}+5+0')
root.resizable(False, False)
root.title('Prashant Records v2.0')

welcome()
root.mainloop()
