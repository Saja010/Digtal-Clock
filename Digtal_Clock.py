# import tkinter 
from tkinter import *
import time


clk=Tk()
clk.geometry("1350x700+0+0")
clk.title("Clock")
clk.config(bg="#0C1E28") 


#----Clock Function----#
def Clock():
    Hours=str(time.strftime("%H"))
    Minutes=str(time.strftime("%M"))
    Seconds=str(time.strftime("%S"))

    print(Hours,Minutes,Seconds)
    if int(Hours)>12 and int(Minutes)>0 : # to convert AM to PM
        label1_dn.config(text="PM")

    if int(Hours) > 12 :
        Hours=str(int(int(Hours)-12))

    label1_Hours.config(text=Hours)
    label2_Minutes.config(text=Minutes)  
    label1_Seconds.config(text=Seconds)


    label1_Hours.after(200,Clock)   # To Update Evrey Second   


#-----Hours-----#
label1_Hours=Label(clk,text="12",font=("Times 20,",75, "bold" ),bg="#0875B7",fg="white")
label1_Hours.place(x=350,y=200,width=150,height=150)

label1_Hours_text=Label(clk,text="HOUR",font=("Times 20,",20, "bold"),bg="#0875B7",fg="white")
label1_Hours_text.place(x=350,y=360,width=150,height=50)



#----Minutes----#


label2_Minutes=Label(clk,text="12",font=("Times 20,",75, "bold" ),bg="#008EA4",fg="white")
label2_Minutes.place(x=520,y=200,width=150,height=150)

label2_Minutes_text=Label(clk,text="Minutes",font=("Times 20,",20, "bold"),bg="#008EA4",fg="white")
label2_Minutes_text.place(x=520,y=360,width=150,height=50)


#----Seconds----#

label1_Seconds=Label(clk,text="12",font=("Times 20,",75, "bold" ),bg="#06B4B8",fg="white")
label1_Seconds.place(x=690,y=200,width=150,height=150)

label1_Seconds_text=Label(clk,text="Seconds",font=("Times 20,",20, "bold"),bg="#06B4B8",fg="white")
label1_Seconds_text.place(x=690,y=360,width=150,height=50)


#--------#
label1_dn=Label(clk,text="AM",font=("Times 20,",70, "bold" ),bg="#9F0646",fg="white")
label1_dn.place(x=860,y=200,width=150,height=150)

label1_dn_text=Label(clk,text="NOON",font=("Times 20,",20, "bold"),bg="#9F0646",fg="white")
label1_dn_text.place(x=860,y=360,width=150,height=50)






Clock()
clk.mainloop()
