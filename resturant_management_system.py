from tkinter import*
from tkinter import ttk
import random
import time

root = Tk()
root.geometry("1600x700+0+0")
root.title("Restaurant Management System")

Tops = Frame(root,bg="light green",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

#------------------TIME--------------

localtime=time.asctime(time.localtime(time.time()))
time.sleep(1)

#                           ***

lbfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="RESTAURANT MANAGEMENT SYSTEM",fg="dark green",bd=10,anchor='ne')
lbfo.grid(row=0,column=0)
lbfo = Label(Tops, font=( 'aria' ,20,'bold' ),text=localtime,fg="black",anchor=W)
lbfo.grid(row=1,column=0)

#---------------Calculator------------------

text_Input=StringVar()
operator =""

txtdisplay = Entry(f2,font=('ariel' ,20,'bold'), textvariable=text_Input , bd=5 ,insertwidth=7 ,bg="white",justify='right')
txtdisplay.grid(columnspan=4)

def  btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup=str(eval(operator))

    text_Input.set(sumup)
    operator = ""

def Ref():
    a=random.randint()
    randomRef = str(a)
    rand.set(randomRef)


def reset():
    rand.set("")
    Orderrefrence.set("")
    Largefries.set("")
    Burger.set("")
    Vegmeal.set("")
    NonvegMeal.set("")
    Subtotal.set("")
    Total.set("")
    Thakalifood.set("")
    Service_Charge.set("")
    Drinks.set("")
    StateTax.set("")
    Costoffood.set("")

def Exit():
    root.destroy()


#...............................Buttons...................................

btn7=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="7",bg="black", command=lambda: btnclick(7) )
btn7.grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="8",bg="black", command=lambda: btnclick(8) )
btn8.grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="9",bg="black", command=lambda: btnclick(9) )
btn9.grid(row=2,column=2)

Add=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="+",bg="black", command=lambda: btnclick("+") )
Add.grid(row=2,column=3)

#......................................................................................................

btn4=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="4",bg="black", command=lambda: btnclick(4) )
btn4.grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="5",bg="black", command=lambda: btnclick(5) )
btn5.grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="6",bg="black", command=lambda: btnclick(6) )
btn6.grid(row=3,column=2)

Sub=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="-",bg="black", command=lambda: btnclick("-") )
Sub.grid(row=3,column=3)

#.........................................................................................

btn1=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="1",bg="black", command=lambda: btnclick(1) )
btn1.grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="2",bg="black", command=lambda: btnclick(2) )
btn2.grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="3",bg="black", command=lambda: btnclick(3) )
btn3.grid(row=4,column=2)

multi=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="*",bg="black", command=lambda: btnclick("*") )
multi.grid(row=4,column=3)

#.........................................................................................................

btn0=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="0",bg="black", command=lambda: btnclick(0) )
btn0.grid(row=5,column=0)

btnc=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="c",bg="black", command=clrdisplay)
btnc.grid(row=5,column=1)

btnequal=Button(f2,padx=16,pady=16,bd=4,width = 16, fg="white", font=('ariel', 20 ,'bold'),text="=",bg="black",command=eqals)
btnequal.grid(columnspan=4)

Decimal=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text=".",bg="black", command=lambda: btnclick(".") )
Decimal.grid(row=5,column=2)

Div=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="/",bg="black", command=lambda: btnclick("/") )
Div.grid(row=5,column=3)
status = Label(f2,font=('aria', 15, 'bold'),width = 16, text="By Amit Raut",bd=2,relief=SUNKEN)
status.grid(row=7,columnspan=3)

#................................................................................................

rand = StringVar()
Orderrefrence = StringVar()
Largefries = StringVar()
Burger = StringVar()
Vegmeal = StringVar()
Nonvegmeal = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
StateTax = StringVar()
costoffood = StringVar()
Thakalifood = StringVar()


lblRef=Label(f1,font=( 'aria' ,15, 'bold' ),text="Order Refrence",bd=10,anchor='ne')
lblRef.grid(row=0,column=0)
txtRef=Entry(f1,font=('ariel', 15 ,'bold'),insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txtRef.grid(row=0,column=1)

lbllrgfri=Label(f1,font=( 'aria' ,15, 'bold' ),text="Large Fries",bd=10,anchor='w')
lbllrgfri.grid(row=1,column=0)
txtlrgfri=Entry(f1,font=('ariel', 15 ,'bold'),insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txtlrgfri.grid(row=1,column=1)

lblBurger=Label(f1,font=( 'aria' ,15, 'bold' ),text="Burger",bd=10,anchor='w')
lblBurger.grid(row=2,column=0)
txtBurger=Entry(f1,font=('ariel', 15 ,'bold'),insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txtBurger.grid(row=2,column=1)

lblVeg_meal=Label(f1,font=( 'aria' ,15, 'bold' ),text="Veg-Meal",bd=10,anchor='w')
lblVeg_meal.grid(row=3,column=0)
txtVeg_meal=Entry(f1,font=('ariel', 15 ,'bold'),insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txtVeg_meal.grid(row=3,column=1)

lblNon_Veg_meal=Label(f1,font=( 'aria' ,15, 'bold' ),text="Non-Veg Meal",bd=10,anchor='w')
lblNon_Veg_meal.grid(row=4,column=0)
txtNon_Veg_meal=Entry(f1,font=('ariel', 15 ,'bold'),insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txtNon_Veg_meal.grid(row=4,column=1)

lblThakali=Label(f1,font=( 'aria' ,15, 'bold' ),text="Thakali food",bd=10,anchor='w')
lblThakali.grid(row=5,column=0)
txtThakali=Entry(f1,font=('ariel', 15 ,'bold'),insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txtThakali.grid(row=5,column=1)

lblDrinks=Label(f1,font=( 'aria' ,15, 'bold' ),text="Drinks",bd=10,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks=Entry(f1,font=('ariel', 15 ,'bold'),insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txtDrinks.grid(row=0,column=3)

lblcost=Label(f1,font=( 'aria' ,15, 'bold' ),text="Cost of Food",bd=10,anchor='w')
lblcost.grid(row=1,column=2)
txtcost=Entry(f1,font=('ariel', 15 ,'bold'),insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txtcost.grid(row=1,column=3)

lblservice=Label(f1,font=( 'aria' ,15, 'bold' ),text="Services Charge",bd=10,anchor='w')
lblservice.grid(row=2,column=2)
txtservice=Entry(f1,font=('ariel', 15 ,'bold'),insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txtservice.grid(row=2,column=3)

lblstate=Label(f1,font=( 'aria' ,15, 'bold' ),text="State Tax",bd=10,anchor='w')
lblstate.grid(row=3,column=2)
txtstate=Entry(f1,font=('ariel', 15 ,'bold'),insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txtstate.grid(row=3,column=3)

lblsubtotal=Label(f1,font=( 'aria' ,15, 'bold' ),text="Sub Total",bd=10,anchor='w')
lblsubtotal.grid(row=4,column=2)
txtsubtotal=Entry(f1,font=('ariel', 15 ,'bold'),insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txtsubtotal.grid(row=4,column=3)

lbltotalcost=Label(f1,font=( 'aria' ,15, 'bold' ),text="TOTAL",bd=10,anchor='w')
lbltotalcost.grid(row=5,column=2)
txttotalcost=Entry(f1,font=('ariel', 15 ,'bold'),insertwidth=4,fg="blue", bg="light pink",bd=10,justify='right')
txttotalcost.grid(row=5,column=3)


#..............................Buttons..........................................................

lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=6,columnspan=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="powder blue",command=Ref)
btnTotal.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=Exit)
btnexit.grid(row=7, column=3)

root.mainloop()