#  'Real time Login-Register interface' Source Code

#importing modules:
from tkinter import *
import time

#creating GUI window:
root= Tk()
root.geometry('345x400')
root.title('Prashant Records')

f1=Frame(root)  #for heading
f2=Frame(root)  #for register page
f3=Frame(root)  #for login page
f4=Frame(root,bg='white')  #for bio-data

#for loading photos:
image3=PhotoImage(file=r"C:\Users\asus\Documents\01-Prashant\Prashant coder\tkinter(pk)\Prashant_Records\bg for chat interface.gif")
photo3=Label(f1,image=image3)
photo3.place(x=0,y=-500)

image1=PhotoImage(file="C:\\Users\\asus\\Documents\\01-Prashant\\Prashant coder\\tkinter(pk)\\me.png")
photo=Label(f1,image=image1)
image2=PhotoImage(file="C:\\Users\\asus\\Documents\\01-Prashant\\Prashant coder\\tkinter(pk)\\poweroff2.png")
###relief must be flat, groove, raised, ridge, solid, or sunken
##image0=PhotoImage(file="C:\\Users\\asus\\Documents\\01-Prashant\\Prashant coder\\tkinter(pk)\\bg.png")
##photo2=Label(f2,image=image0)
##photo2.grid(row=0)

tcompany=Label(f1,text='Prashant Records', font='bignoodletitling 30 bold underline',fg='purple',bg='lightpink')

#pswd encryption preparation
dict1={'1': 'rr', '2': 'ry', '3': 'ri', '4': 'ryy', '5': 'ro', '6': 'or', '7': 'yr', '8': 'yii', '9': 'ir',
       '0': 'yy', 'q': 'ii', 'w': 'idd', 'e': 'oo', 'r': 'rp', 't': 'rd', 'y': 'rf', 'u': 'ohh', 'i': 'rh', 'o': 'pr',
       'p': 'dr', 'a': 'pff', 's': 'fr', 'd': 'hr', 'f': 'pp', 'g': 'doo', 'h': 'dd', 'j': 'ff', 'k': 'hh', 'l': 'yi',
       'z': 'frr', 'x': 'iy', 'c': 'yo', 'v': 'oy', 'b': 'hpp', 'n': 'yp', 'm': 'py'}

allowed=['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s',
         'd','f','g','h','j','k','l','z','x','c','v','b','n','m']
encrypt=[]#for-storing-encrypted-pswd

#Register Frame Preparation
t1=Label(f1,text='Register below:\n', font='BookAntiqua 15 italic')

t3=Label(f2,text=' Name*', font='BookAntiqua 12')
e1=Entry(f2, textvariable=StringVar(), bg='lightblue', relief='groove')

t4=Label(f2,text=' Phone', font='BookAntiqua 12')
e2=Entry(f2, textvariable=StringVar(), bg='lightblue', relief='groove')
e2.insert(0,'+91 ')

t5=Label(f2,text=' Username*', font='BookAntiqua 12')
e3=Entry(f2, textvariable=StringVar())

t6=Label(f2,text=' Password*', font='BookAntiqua 12')
e4=Entry(f2, textvariable=StringVar(),show='*')

t7=Label(f2,text=' Email', font='BookAntiqua 12')
e5=Entry(f2, textvariable=StringVar())
e5.insert(0,'@gmail.com')

t7a=Label(f2,text=' NOTE:', font='BookAntiqua 12')
e5a=Text(f2,height=3,width=15,wrap=WORD)

f1.grid(row=0)
tcompany.grid(row=0,column=0,padx=10),t1.grid(),photo.grid(row=0,column=1)
z=f2.grid()
t3.grid( row=4,sticky='w'),e1.grid(row=4,column=1)
t4.grid(row=5,sticky='w'),e2.grid(row=5,column=1)
t5.grid(row=6,sticky='w'),e3.grid(row=6,column=1)
t6.grid(row=7,sticky='w'),e4.grid(row=7,column=1)
t7.grid(row=8,sticky='w'),e5.grid(row=8,column=1)
t7a.grid(row=9,pady=20,sticky='w'),e5a.grid(row=9,column=1)
tinfo=Label(f2,text='', font='BookAntiqua 12')
tinfo.grid(row=11,column=1)
        
#opening records to check unique username
try:
    f=open('C:\\Users\\asus\\Documents\\01-Prashant\\Prashant coder\\tkinter(pk)\\records.txt','r')
    text1=f.readlines()   #returns whole document as a list
except:f=open('C:\\Users\\asus\\Documents\\01-Prashant\\Prashant coder\\tkinter(pk)\\records.txt','w')
f.close() 

#func. to return True if keyword('x') exists in List('listname') and False if doesn't:
def check(listname,x):
    if (x+'\n') in listname:
        return True
    else:
        return False
    
def register():
    global tinfo, encrypt, allowed, dict1

    if e1.get()!='' and e3.get()!='' and e4.get()!='' and (not check(text1,'Username: '+e3.get())) and len(e4.get())>=5:
        
        encrypt=list(e4.get() )
        for i in encrypt:
            indx=encrypt.index(i)
            if i in allowed:
                encrypt[indx]=dict1.get(i)
        
        f=open('C:\\Users\\asus\\Documents\\01-Prashant\\Prashant coder\\tkinter(pk)\\records.txt','a+')
        f.write(e1.get()+'\n')
        f.write('Phone: '+str(e2.get())+'\n')
        f.write('Username: '+e3.get()+'\n')
        f.writelines(encrypt )
        f.write('\nEmail: '+e5.get()+'\n')
        f.write('Text : '+e5a.get(0.0,'end')+'\n')
        f.flush()
        f.close()

        
        tinfo.grid_forget()
        tinfo=Label(f2,text=' Success!', font='BookAntiqua 13 bold', fg='lightgreen')
        e1.delete(0,END),e2.delete(0,END),e3.delete(0,END),e5.delete(0,END),
        e4.delete(0,END),e5a.delete(0.0,END),e5.insert(0,'@gmail.com'),e2.insert(0,'+91 ')
        tinfo.grid(row=10,column=1,sticky='e')
    elif e1.get()=='':
        tinfo.grid_forget()
        tinfo=Label(f2,text='Please enter name', font='BookAntiqua 10', fg='red')
        tinfo.grid(row=10,column=1)

    elif e3.get()=='' or e4.get=='':        
        tinfo.grid_forget()
        tinfo=Label(f2,text='Invalid Usern./pswd', font='BookAntiqua 10', fg='red')
        tinfo.grid(row=10,column=1)
        
    elif e1.get()!='' and (check(text1,'Username: '+e3.get()) or len(e4.get())<5) and e3.get()!='' and e4.get!='':
        if check(text1,'Username: '+e3.get()):
            tinfo.grid_forget()
            tinfo=Label(f2,text='Username exists', font='BookAntiqua 12', fg='red')
            tinfo.grid(row=10,column=1)
        elif len(e4.get())<5:
            tinfo.grid_forget()
            tinfo=Label(f2,text='pswd lenght must be 5', font='BookAntiqua 10', fg='red')
            tinfo.grid(row=10,column=1)


def login1():
    global z
    f2.grid_forget()
    t1.grid_forget()
    z=f3.grid()
def back1():
    global z
    f3.grid_forget()
    z=f2.grid()
    t1.grid()
def back2():
    global z
    f4.grid_forget()
    z=f3.grid()
    
#Login  Frame Preparation
t8=Label(f3,text='Login below:\n', font='BookAntiqua 15 italic')

t9=Label(f3,text='Username', font='BookAntiqua 12')
e9=Entry(f3, textvariable=StringVar())

t10=Label(f3,text='Password', font='BookAntiqua 12')
e10=Entry(f3, textvariable=StringVar())

t8.grid(row=1,column=0),t9.grid(row=3,column=0),t10.grid(row=4,column=0)
e9.grid(row=3,column=1),e10.grid(row=4,column=1)

tinfo2=Label(f3,text='')
tinfo2.grid(row=5,column=1)
pswd_index=0
details=['name','phone','username','email','hobby']
def login2():
    global tinfo2, details, encrypt
    f=open('C:\\Users\\asus\\Documents\\01-Prashant\\Prashant coder\\tkinter(pk)\\records.txt','r')
    text1=f.readlines()
    f.close()
    xlist=['\n']
    if check(text1,'Username: '+e9.get()):
        pswd_index=text1.index('Username: '+e9.get()+'\n')+1
        pswd=text1[pswd_index]  #original password
        
        encrypt=list(e10.get() )  
        for i in encrypt:
            indx=encrypt.index(i)
            if i in allowed:
                encrypt[indx]=dict1.get(i)
        encrypt="".join(encrypt+xlist)     #user entered password added \n because original pswd had \n at its end
        
    if check(text1,'Username: '+e9.get()) and (encrypt)==pswd:
        time.sleep(0.1)
        username_index=text1.index('Username: '+e9.get()+'\n')
        details[0]=(text1[ username_index-2 ])
        details[1]=(text1[ username_index-1 ])
        details[2]=(text1[ username_index ])
        details[3]=(text1[ username_index+2 ])
        details[4]=(text1[ username_index+3 ])
        biodata()
        
    elif check(text1,'Username: '+e9.get()) and (e10.get()+'\n')!=pswd:
        tinfo2.grid_forget()
        tinfo2=Label(f3,text='wrong pswd', font='BookAntiqua 12', fg='red')
        tinfo2.grid(row=5,column=1)  

    elif not check(text1,'Username: '+e9.get()) and e9.get()!='':
        tinfo2.grid_forget()
        tinfo2=Label(f3,text='Username not found', font='BookAntiqua 12', fg='red')
        tinfo2.grid(row=5,column=1)
        
    if e9.get()=='' or e10.get()=='':
        tinfo2.grid_forget()
        tinfo2=Label(f3,text='Enter Username/pswd', font='BookAntiqua 11', fg='red')
        tinfo2.grid(row=5,column=1)        
    
    
#bio data page preparation

def biodata():
    global details, z
    f3.grid_forget()
    z=f4.grid()
    root.geometry('357x450')

    t11=Label(f4,text='BIODATA  of  '+details[0], font='bignoodletitling 20 bold',fg='deeppink', bg='white')
    t12=Label(f4,text=details[1]+'    ', font='BookAntiqua 15',borderwidth=6, bg='white')
    t13=Label(f4,text=details[2]+'    ', font='BookAntiqua 15', bg='white')
    t14=Label(f4,text=details[3]+'    ', font='BookAntiqua 14', bg='white')
    t15=Label(f4,text=details[4]+'    ', font='BookAntiqua 15', bg='white')
    t11.grid(row=2), t12.grid(row=3,sticky='w'),t13.grid(row=4,sticky='w'),t14.grid(row=5,sticky='w'),t15.grid(row=6,sticky='w')

#Buttons:
bregister=Button(f2, text='Register', font='BookAntiqua 13',relief=RAISED,
                command=register, fg='lightgreen', bg='white',border=4)
bregister.grid(row=12,column=1)

blogin1=Button(f2, text='Login Page', font='BookAntiqua 12', command=login1)
blogin1.grid(row=12,column=0)

blogin2=Button(f3, text='Login', font='BookAntiqua 13', command=login2,
               fg='lightgreen', bg='white',border=4)
blogin2.grid(row=6,column=1)

bback1=Button(f3, text='Back', font='BookAntiqua 13', command=back1)
bback1.grid(row=6,column=0)

bback2=Button(f4, text='Back', font='BookAntiqua 13', command=back2)
bback2.grid(row=7)
bpower=Button(f3, command=root.destroy, text='Quit',border=0,image=image2)
bpower.grid()

bpower=Button(f4,command=root.destroy, text='Quit',border=0,bg='white',image=image2)
bpower.grid(row=8)

bpower=Button(f2,command=root.destroy, text='Quit',border=0,image=image2)
bpower.grid(sticky='e')

root.mainloop()



