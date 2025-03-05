from tkinter import *
from tkinter import messagebox
import random
import turtle
import sqlite3
con = sqlite3.connect('c:/Users/89parham/Documents/database rps.db')
cur = con.cursor()

def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS result (id integer PRIMARY KEY,fname text, win real,lose real)')
    con.commit()
def insert_record(name,lost,won):
    cur.execute('insert into result values (NULL,?,?,?)' ,(name,won,lost))
    con.commit()
def search(name):
    cur.execute('select * from result where fname =?',(name,))
    return cur.fetchall()

create_table()

win=Tk()
win.title('rock paper scissors')
win.geometry('500x500')
win.config(bg='#091039')
ffname=()
llaps=()
b=0
n=0
def start():
    global ffname
    global llaps
    fname=ent_fname.get()
    laps=ent_round.get()
    ffname=fname
    llaps=laps
    if fname=='' or laps=='' or fname.isdigit() or not laps.isdigit():
        messagebox.showerror('error','enter name and lap completly and right')
    if int(laps)>15:
        messagebox.showerror('error','laps must be lower than 15')
    else:
        game()
def game():
    win.destroy()
    def paper():
        global ffname
        global llaps
        global b
        global n
        choose=(['rock','si','paper'])
        right=random.choice(choose)
        if int(n)!=int(llaps) and int(b)!=int(llaps):
            lbl_shape.config(text='✋')
            if right=='rock':
                lbl_resalt.config(text='score is for you')
                n+=1
                lbl_bot.config(text='👊')
                lbl_laps.config(text=f'{n}/{llaps}')
            if right=='si':
                lbl_resalt.config(text='score is for Bot')
                b+=1
                lbl_bot.config(text='✌')
                lbl_blaps.config(text=f'{b}/{llaps}')
            if right=='paper':
                lbl_resalt.config(text='draw')
                lbl_bot.config(text='✋')
        if int(n)==int(llaps):
            insert_record(ffname,0,1)
            s=messagebox.askquestion('you won','do you want to play again')

            if s =='yes':
                lbl_resalt.config(text='')
                n=0
                b=0
                lbl_blaps.config(text=f'{b}/{llaps}')
                lbl_laps.config(text=f'{b}/{llaps}')
                lbl_shape.config(text='')
                lbl_bot.config(text='')
            if s=='no':
                root.destroy()
        if int(b)==int(llaps):
            s=messagebox.askquestion('you lose','do you want to play again')
            insert_record(ffname,1,0)
            if s =='yes':
                lbl_resalt.config(text='')
                n=0
                b=0
                lbl_blaps.config(text=f'{b}/{llaps}')
                lbl_laps.config(text=f'{b}/{llaps}')
                lbl_shape.config(text='')
                lbl_bot.config(text='')
            if s=='no':
                root.destroy()
    def si ():
        global llaps
        global b
        global n
        choose=(['rock','si','paper'])
        right=random.choice(choose)
        if int(n)!=int(llaps) and int(b)!=int(llaps):        
            lbl_shape.config(text='✌')
            if right=='rock':
                lbl_resalt.config(text='score is for Bot')
                b+=1
                lbl_bot.config(text='👊')
                lbl_blaps.config(text=f'{b}/{llaps}')
            if right=='si':
                lbl_bot.config(text='✌')
                lbl_resalt.config(text='draw')
            if right=='paper':
                lbl_resalt.config(text='score is for you')
                n+=1
                lbl_bot.config(text='✋')
                lbl_laps.config(text=f'{n}/{llaps}')
        if int(n)==int(llaps):
            s=messagebox.askquestion('you won','do you want to play again')

            insert_record(ffname,0,1)
            if s =='yes':
                lbl_resalt.config(text='')
                n=0
                b=0
                lbl_blaps.config(text=f'{b}/{llaps}')
                lbl_laps.config(text=f'{b}/{llaps}')
                lbl_shape.config(text='')
                lbl_bot.config(text='')
            if s=='no':
                root.destroy()
        if int(b)==int(llaps):
            s=messagebox.askquestion('you lose','do you want to play again')
            insert_record(ffname,1,0)
            if s =='yes':
                lbl_resalt.config(text='')
                n=0
                b=0
                lbl_blaps.config(text=f'{b}/{llaps}')
                lbl_laps.config(text=f'{b}/{llaps}')
                lbl_shape.config(text='')
                lbl_bot.config(text='')
            if s=='no':
                root.destroy()
    def rock ():
        global llaps
        global b
        global n
        choose=(['rock','si','paper'])
        right=random.choice(choose)
        if int(n)!=int(llaps):
            lbl_shape.config(text='👊')
            if right=='rock':
                lbl_resalt.config(text='draw')
                lbl_bot.config(text='👊')
            if right=='si':
                lbl_resalt.config(text='score is for you')
                n+=1
                lbl_bot.config(text='✌')
                lbl_laps.config(text=f'{n}/{llaps}')
            if right=='paper':
                lbl_resalt.config(text='score is for Bot')
                b+=1
                lbl_bot.config(text='✋')
                lbl_blaps.config(text=f'{b}/{llaps}')
        if int(n)==int(llaps):
            s=messagebox.askquestion('you won','do you want to play again')
            insert_record(ffname,0,1)
            if s =='yes':
                lbl_resalt.config(text='')
                n=0
                b=0
                lbl_blaps.config(text=f'{b}/{llaps}')
                lbl_laps.config(text=f'{b}/{llaps}')
                lbl_shape.config(text='')
                lbl_bot.config(text='')
            if s=='no':
                root.destroy()
        if int(b)==int(llaps):
            s=messagebox.askquestion('you lose','do you want to play again')
            insert_record(ffname,1,0)
            if s =='yes':
                lbl_resalt.config(text='')
                n=0
                b=0
                lbl_blaps.config(text=f'{b}/{llaps}')
                lbl_laps.config(text=f'{b}/{llaps}')
                lbl_shape.config(text='')
                lbl_bot.config(text='')
            if s=='no':
                root.destroy()
    root=Tk()
    root.title('rock paper scissors')
    root.geometry('1590x820+0+0')
    root.config(bg='#091039')
    #player
    lbl_name=Label(text=ffname,font='bold 30',bg='#278b10')
    lbl_name.place(x=300,y=50)

    lbl_laps=Label(text=f'0/{llaps}',font='bold 38',bg='#278b10')
    lbl_laps.place(x=300,y=120)

    lbl_blaps=Label(text=f'0/{llaps}',font='bold 38',bg='#278b10')
    lbl_blaps.place(x=1200,y=120)

    btn_paper=Button(text='✋',font='bold 50',bg='#feff11',command=paper)
    btn_paper.place(x=100,y=600)

    btn_rock=Button(text='👊',fg='black',font='bold 50',bg='#feff11',command=rock)
    btn_rock.place(x=300,y=600)

    btn_si=Button(text='✌',font='bold 50',bg='#feff11',command=si)
    btn_si.place(x=500,y=600)

    lbl_shape=Label(text='',font='bold 90',bg='red')
    lbl_shape.place(x=300,y=300)

    lbl_bot=Label(text='',font='bold 90',bg='red')
    lbl_bot.place(x=1200,y=300)

    lbl_name=Label(text='Bot',font='bold 30',bg='#278b10')
    lbl_name.place(x=1200,y=50)

    lbl_resalt=Label(text=f'',font='bold 30',bg='orange')
    lbl_resalt.place(x=630,y=200)
    root.mainloop()
def show():
    e=ent_fname.get()
    result=search(e)
    if e =='':
        messagebox.showerror('error','for showing result you must enter your name')
    elif result ==[]:
        messagebox.showerror('error','your name is not in players list')
    else: 
        w=float()
        l=float()
        for i in result :
            w+=(i[2])
            l+=(i[3])
        messagebox.showinfo('result',f'{e} , you have lost for {int(l)} times and won for {int(w)} times')
lbl_fname=Label(text='your first name :',bg='#278b10',font='bold 15').place(x=20,y=30)

lbl_round=Label(text='number of laps :',bg='#278b10',font='bold 15').place(x=20,y=80)

ent_fname=Entry(win,width=12,font='bold 15')
ent_fname.place(x=200,y=32)

ent_round=Entry(win,width=12,font='bold 15')
ent_round.place(x=200,y=82)

btn_start=Button(text='Start',font='bold 25',bg='#278b10',width=10,command=start)
btn_start.place(x=150,y=200)

btn_result=Button(text='Show result',font='bold 25',bg='#278b10',width=10,command=show)
btn_result.place(x=150,y=280)

win.mainloop()