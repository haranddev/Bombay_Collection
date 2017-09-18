from Tkinter import *
import random
import time
import datetime
import tkMessageBox

root = Tk()
root.geometry("1350x650+0+0")
root.title("Billing Systems")

Tops = Frame(root, width = 1350, height = 100, bd = 8, relief = "raise")
Tops.pack(side = TOP)


f1 = Frame(root, width = 900, height = 650, bd = 8, relief = "raise")
f1.pack(side = LEFT)
f2 = Frame(root, width = 440, height = 650, bd = 8, relief = "raise")
f2.pack(side = RIGHT)

f1a = Frame(f1, width = 900, height = 330, bd = 8, relief = "raise")
f1a.pack(side = TOP)
f2a = Frame(f1, width = 900, height = 320, bd = 8, relief = "raise")
f2a.pack(side = BOTTOM)

f1aa = Frame(f1a, width = 400, height = 430, bd = 8, relief = "raise")
f1aa.pack(side = LEFT)
f1ab = Frame(f1a, width = 400, height = 430, bd = 8, relief = "raise")
f1ab.pack(side = RIGHT)

f2aa = Frame(f2a, width = 450, height = 330, bd = 8, relief = "raise")
f2aa.pack(side = LEFT)
f2ab = Frame(f2a, width = 450, height = 330, bd = 8, relief = "raise")
f2ab.pack(side = LEFT)



lblInfo = Label(Tops, font = ('arial', 60, 'bold'), text ="             Bombay Collection          ",
                bd = 10, anchor = 'w')
lblInfo.grid(row = 0, column = 0)

#------------------------------------------VARIABLES--------------------------------------------------------------------
txt_Input = StringVar()
operator = ""
PaymentRef = StringVar()
Carpets = StringVar()
Blinds = StringVar()
Fabric = StringVar()
HomeDelivery = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCarpet = StringVar()
CostofBlinds = StringVar()
CostofFabric = StringVar()
CostofDelivery = StringVar()
DateofOrder = StringVar()

Carpets.set(0)
Blinds.set(0)
Fabric.set(0)
HomeDelivery.set(0)

DateofOrder.set(time.strftime("%d/%m/%y"))

def CostOrOrder():
    CarpetPrice = float(Carpets.get())
    BlindPrice = float(Blinds.get())
    CarpetFabric = float(Fabric.get())
    DeliveryCost = float(HomeDelivery.get())

    CarpetCost = "INR",str('%.2f'%((CarpetPrice * 15.49)))
    CostofCarpet.set(CarpetCost)

    BlindCost = "INR", str('%.2f' % ((BlindPrice * 7.49)))
    CostofBlinds.set(BlindCost)

    FabricCost = "INR", str('%.2f' % ((CarpetFabric * 21.45)))
    CostofFabric.set(FabricCost)

    DLCost = "INR", str('%.2f' % ((DeliveryCost * 23)))
    CostofDelivery.set(DLCost)

#    Sub = CarpetCost + BlindCost + FabricCost + DLCost

    Toc = "INR", str('%.2f' %((CarpetPrice * 15.49) + (BlindPrice * 7.49) + (CarpetFabric * 21.45) + (DeliveryCost * 23)))
    SubTotal.set(Toc)
    Tax =  "INR", str('%.2f' %(((CarpetPrice * 15.49) + (BlindPrice * 7.49) + (CarpetFabric * 21.45) + (DeliveryCost * 23)) * .18))
    PaidTax.set(Tax)
    TaxPay = (((CarpetPrice * 15.49) + (BlindPrice * 7.49) + (CarpetFabric * 21.45) + (DeliveryCost * 23)) * .18)
    Cost = ((CarpetPrice * 15.49) + (BlindPrice * 7.49) + (CarpetFabric * 21.45) + (DeliveryCost * 23))
    CostOfItems = "INR", str('%.2f' %(TaxPay + Cost))
    TotalCost.set(CostOfItems)

    x = random.randint(10034, 699812)
    randomRef = str(x)
    PaymentRef.set("BILL" + randomRef)



def PayReference():
    x = random.randint(10034, 699812)
    randomRef = str(x)
    PaymentRef.set("BILL"+randomRef)
def iExit():
    qExit = tkMessageBox.askyesno("Billing System", "Do you want to exit the system")
    if qExit > 0:
        root.destroy()
        return
def Reset():
    txt_Input.set("")
    PaymentRef.set("")
    Carpets.set(0)
    Blinds.set(0)
    Fabric.set(0)
    HomeDelivery.set(0)
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofCarpet.set("")
    CostofBlinds.set("")
    CostofFabric.set("")
    CostofDelivery.set("")

#============================================CALCULATOR=================================================================

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    txt_Input.set(operator)

def btnClearDisplay():
    global operator
    operator =""
    txt_Input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    txt_Input.set(sumup)
    operator = sumup

txtDisplay = Entry(f2, font=('arial', 20, 'bold'),
                   textvariable = txt_Input, bd = 40, insertwidth = 6, justify= 'right')
txtDisplay.grid(columnspan = 4)

btn7 = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = '7', command = lambda:btnClick(7)).grid(row = 1, column =0)
btn8 = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = '8', command = lambda:btnClick(8)).grid(row = 1, column =1)
btn9 = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = '9', command = lambda:btnClick(9)).grid(row = 1, column =2)
btnPlus = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
                 text = '+', command = lambda:btnClick("+")).grid(row = 1, column =3)

#----------------------------------------------------------------------------------------------------------------------

btn4 = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = '4', command = lambda:btnClick(4)).grid(row = 3, column =0)
btn5 = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = '5', command = lambda:btnClick(5)).grid(row = 3, column =1)
btn6 = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = '6', command = lambda:btnClick(6)).grid(row = 3, column =2)
btnSub = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
                text = '-', command = lambda:btnClick("-")).grid(row = 3, column =3)

#-----------------------------------------------------------------------------------------------------------------------

btn1 = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = '1', command = lambda:btnClick(1)).grid(row = 4, column =0)
btn2 = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = '2', command = lambda:btnClick(2)).grid(row = 4, column =1)
btn3 = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = '3', command = lambda:btnClick(3)).grid(row = 4, column =2)
btnMult = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
                 text = '*', command = lambda:btnClick("*")).grid(row = 4, column =3)

#-----------------------------------------------------------------------------------------------------------------------

btn0 = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = '0', command = lambda:btnClick(0)). grid(row = 5, column =0)
btnClear = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
                  text = 'C', command = btnClearDisplay). grid(row = 5, column =1)
btnEquals = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
                   text = '=', command = btnEqualsInput). grid(row = 5, column =2)
btnDiv = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
                text = '/', command = lambda:btnClick("/")). grid(row = 5, column =3)


#---------------------------------------------------ORDER INFORMATION--f1aa---------------------------------------------


lblRef = Label(f1aa, font =('arial', 16, 'bold'), text = "Sales Reference", bd = 16, justify = "left")
lblRef.grid(row = 0, column = 0)
txtRef = Entry(f1aa, font =('arial', 16, 'bold'),
               textvariable = PaymentRef, bd = 10, insertwidth = 2, justify = "left")
txtRef.grid(row = 0, column =1)

#-----------------------------------------------------------------------------------------------------------------------
lblCarpets = Label(f1aa, font =('arial', 16, 'bold'), text = "Carpets", bd = 16, justify = "left")
lblCarpets.grid(row = 1, column = 0)
txtCarpets = Entry(f1aa, font =('arial', 16, 'bold'),
               textvariable = Carpets, bd = 10, insertwidth = 2, justify = "left")
txtCarpets.grid(row = 1, column =1)

#-----------------------------------------------------------------------------------------------------------------------
lblFabric = Label(f1aa, font =('arial', 16, 'bold'), text = "Fabric", bd = 16, justify = "left")
lblFabric.grid(row = 2, column = 0)
txtFabric = Entry(f1aa, font =('arial', 16, 'bold'),
               textvariable = Fabric, bd = 10, insertwidth = 2, justify = "left")
txtFabric.grid(row = 2, column =1)

#-----------------------------------------------------------------------------------------------------------------------
lblBlinds = Label(f1aa, font =('arial', 16, 'bold'), text = "Blinds", bd = 16, justify = "left")
lblBlinds.grid(row = 3, column = 0)
txtBlinds = Entry(f1aa, font =('arial', 16, 'bold'),
               textvariable = Blinds, bd = 10, insertwidth = 2, justify = "left")
txtBlinds.grid(row = 3, column =1)

#-----------------------------------------------------------------------------------------------------------------------
lblHomeDelivery = Label(f1aa, font =('arial', 16, 'bold'), text = "Home Delivery", bd = 16, justify = "left")
lblHomeDelivery.grid(row = 4, column = 0)
txtHomeDelivery = Entry(f1aa, font =('arial', 16, 'bold'),
               textvariable = HomeDelivery, bd = 10, insertwidth = 2, justify = "left")
txtHomeDelivery.grid(row = 4, column =1)

#-----------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------ORDER INFORMATION--f1ab---------------------------------------------

lblDateofOrder = Label(f1ab, font =('arial', 16, 'bold'), text = "Date Of Order", bd = 16, justify = "left")
lblDateofOrder.grid(row = 0, column = 0)
txtDateofOrder = Entry(f1ab, font =('arial', 16, 'bold'),
               textvariable = DateofOrder, bd = 10, insertwidth = 2, justify = "left")
txtDateofOrder.grid(row = 0, column =1)

#-----------------------------------------------------------------------------------------------------------------------
lblCostofCarpets = Label(f1ab, font =('arial', 16, 'bold'), text = "Cost of Carpets", bd = 16, justify = "left")
lblCostofCarpets.grid(row = 1, column = 0)
txtCostofCarpets = Entry(f1ab, font =('arial', 16, 'bold'),
               textvariable = CostofCarpet, bd = 10, insertwidth = 2, justify = "left")
txtCostofCarpets.grid(row = 1, column =1)

#-----------------------------------------------------------------------------------------------------------------------
lblCostofFabric = Label(f1ab, font =('arial', 16, 'bold'), text = "Cost of Fabric", bd = 16, justify = "left")
lblCostofFabric.grid(row = 2, column = 0)
txtCostofFabric = Entry(f1ab, font =('arial', 16, 'bold'),
               textvariable = CostofFabric, bd = 10, insertwidth = 2, justify = "left")
txtCostofFabric.grid(row = 2, column =1)

#-----------------------------------------------------------------------------------------------------------------------
lblCostofBlinds = Label(f1ab, font =('arial', 16, 'bold'), text = "Cost of Blinds", bd = 16, justify = "left")
lblCostofBlinds.grid(row = 3, column = 0)
txtCostofBlinds = Entry(f1ab, font =('arial', 16, 'bold'),
               textvariable = CostofBlinds, bd = 10, insertwidth = 2, justify = "left")
txtCostofBlinds.grid(row = 3, column =1)

#-----------------------------------------------------------------------------------------------------------------------
lblCostofDelivery = Label(f1ab, font =('arial', 16, 'bold'), text = "Cost of Delivery", bd = 16, justify = "left")
lblCostofDelivery.grid(row = 4, column = 0)
txtCostofDelivery = Entry(f1ab, font =('arial', 16, 'bold'),
               textvariable = CostofDelivery, bd = 10, insertwidth = 2, justify = "left")
txtCostofDelivery.grid(row = 4, column =1)

#------------------------------------------------ORDER INFORMATION--f2aa------------------------------------------------

lblPaidTax = Label(f2aa, font =('arial', 16, 'bold'), text = "Paid Tax", bd = 16, justify = "left")
lblPaidTax.grid(row = 2, column = 0)
txtPaidTax = Entry(f2aa, font =('arial', 16, 'bold'),
               textvariable = PaidTax, bd = 10, insertwidth = 2, justify = "left")
txtPaidTax.grid(row = 2, column =1)


lblSubTotal = Label(f2aa, font =('arial', 16, 'bold'), text = "Sub Total", bd = 16, justify = "left")
lblSubTotal.grid(row = 3, column = 0)
txtSubTotal = Entry(f2aa, font =('arial', 16, 'bold'),
               textvariable = SubTotal, bd = 10, insertwidth = 2, justify = "left")
txtSubTotal.grid(row = 3, column =1)


lblTotalCost = Label(f2aa, font =('arial', 16, 'bold'), text = "Total Cost", bd = 16, justify = "left")
lblTotalCost.grid(row = 4, column = 0)
txtTotalCost = Entry(f2aa, font =('arial', 16, 'bold'),
               textvariable = TotalCost, bd = 10, insertwidth = 2, justify = "left")
txtTotalCost.grid(row = 4, column =1)

#--------------------------------------------ORDER INFORMATION BUTTONS--------------------------------------------------

btnTotal = Button(f2ab, padx= 16, pady = 16, bd =8, fg= "black",
                  font =('arial', 16, 'bold'),width = 15, text = "Total Cost", command = CostOrOrder).grid(row = 0, column = 0)

btnRef = Button(f2ab, padx= 16, pady = 16, bd =8, fg= "black",
                  font =('arial', 16, 'bold'),width = 15, text = "Sales Refernce", command = PayReference).grid(row = 0, column = 1)

btnReset = Button(f2ab, padx= 16, pady = 16, bd =8, fg= "black",
                  font =('arial', 16, 'bold'),width = 15, text = "Reset", command = Reset).grid(row = 1, column = 0)

btnExit = Button(f2ab, padx= 16, pady = 16, bd =8, fg= "red",
                  font =('arial', 16, 'bold'),width = 15, text = "Exit", command = iExit).grid(row = 1, column = 1)
root.mainloop()