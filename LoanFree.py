from tkinter.font import BOLD
from LoanFreeFunc import functions
import tkinter as tk
from tkinter.constants import END, FALSE, GROOVE, LEFT, RIDGE, RIGHT, SUNKEN
TK_SILENCE_DEPRECATION=1

window=tk.Tk()
window.geometry("810x540")
window.resizable(False,False)
window.title("DEBT DEFENDER")

#######################
#      MAIN FRAMES    #
#######################
frame0 = tk.Frame(master=window, width=805, height=27)
frame1 = tk.Frame(master=window, width=805, height=95)
frame2 = tk.Frame(master=window, width=805, height=115)
frame3 = tk.Frame(master=window, width=805, height=95)
frame4 = tk.Frame(master=window, width=805, height=45)
frame5 = tk.Frame(master=window, width=805, height=117)
frame6 = tk.Frame(master=window, width=805, height=60)

#DIVIDERS
frame0_1 = tk.Frame(master=window, height=2, bg="black")
frame1_2 = tk.Frame(master=window, height=2, bg="black")
frame2_3 = tk.Frame(master=window, height=2, bg="black")
frame3_4 = tk.Frame(master=window, height=2, bg="black")
frame4_5 = tk.Frame(master=window, height=2, bg="black")
frame5_6 = tk.Frame(master=window, height=2, bg="black")
frame6_7 = tk.Frame(master=window, height=2, bg="black")

#MONTHLY NET INCOME (CASH)
mnetincL = tk.Label(master=frame0, text="MONTHLY NET INCOME(CASH) $")
mnetincE = tk.Entry(master=frame0, relief=GROOVE)

#YEARLY NET INCOME (CASH)
ynetincL = tk.Label(master=frame0, text="YEARLY NET INCOME(CASH) $")
ynetincE = tk.Entry(master=frame0, relief=GROOVE)

#CLIENT NAME
cnameL = tk.Label(master=frame0, text="CLIENT NAME:")
cnameE = tk.Entry(master=frame0, relief=GROOVE)

#DEFAULT VALUES
mnetincE.insert(0 , "0")
ynetincE.insert(0 , "0")
cnameE.insert(0, "Enter Name")

#PLACEMENT
cnameL.place(x=0,y=3)
cnameE.place(x=92,y=0, width=90)
mnetincL.place(x=210,y=3)
mnetincE.place(x=420,y=0, width=70)
ynetincL.place(x=545,y=3)
ynetincE.place(x=739,y=0, width=70)

##########################
#------STUDENT LOAN------#
##########################
sdntloanL = tk.Label(master=frame1, text="STUDENT LOAN")

#LOAN LABLES
sdntloan1L = tk.Label(master=frame1, text="Loan 1 $")
sdntloan2L = tk.Label(master=frame1, text="Loan 2 $")
sdntloan3L = tk.Label(master=frame1, text="Loan 3 $")
sdntloan4L = tk.Label(master=frame1, text="Loan 4 $")

#INTEREST LABELS
sintrate1L = tk.Label(master=frame1, text="Loan Interest Rate %")
sintrate2L = tk.Label(master=frame1, text="Loan Interest Rate %")
sintrate3L = tk.Label(master=frame1, text="Loan Interest Rate %")
sintrate4L = tk.Label(master=frame1, text="Loan Interest Rate %")

#PAYMENT LABELS
smonthly1L = tk.Label(master=frame1, text="Monthly Payment $")
smonthly2L = tk.Label(master=frame1, text="Monthly Payment $")
smonthly3L = tk.Label(master=frame1, text="Monthly Payment $")
smonthly4L = tk.Label(master=frame1, text="Monthly Payment $")

#LOAN ENTERIES
sdntloan1E = tk.Entry(master=frame1, relief=GROOVE)
sdntloan2E = tk.Entry(master=frame1, relief=GROOVE)
sdntloan3E = tk.Entry(master=frame1, relief=GROOVE)
sdntloan4E = tk.Entry(master=frame1, relief=GROOVE)

#INTEREST ENTERIES
sintrate1E = tk.Entry(master=frame1, relief=GROOVE)
sintrate2E = tk.Entry(master=frame1, relief=GROOVE)
sintrate3E = tk.Entry(master=frame1, relief=GROOVE)
sintrate4E = tk.Entry(master=frame1, relief=GROOVE)

#PAYMENT ENTERIES
smonthly1E = tk.Entry(master=frame1, relief=GROOVE)
smonthly2E = tk.Entry(master=frame1, relief=GROOVE)
smonthly3E = tk.Entry(master=frame1, relief=GROOVE)
smonthly4E = tk.Entry(master=frame1, relief=GROOVE)

#DEFAULT VALUES
sdntloan1E.insert(0 , "0")
sdntloan2E.insert(0 , "0")
sdntloan3E.insert(0 , "0")
sdntloan4E.insert(0 , "0")
sintrate1E.insert(0 , "0")
sintrate2E.insert(0 , "0")
sintrate3E.insert(0 , "0")
sintrate4E.insert(0 , "0")
smonthly1E.insert(0 , "0")
smonthly2E.insert(0 , "0")
smonthly3E.insert(0 , "0")
smonthly4E.insert(0 , "0")

#-----PLACEMENT-----#
#TITLE
sdntloanL.place(x=357,y=0)
#COLUMN 1
sdntloan1L.place(x=0,y=20)
sdntloan1E.place(x=55,y=18,width=124)
sintrate1L.place(x=0,y=44)
sintrate1E.place(x=130,y=42,width=48)
smonthly1L.place(x=0,y=68)
smonthly1E.place(x=120,y=66,width=58)
#COLUMN 2
sdntloan2L.place(x=210,y=20)
sdntloan2E.place(x=265,y=18,width=123)
sintrate2L.place(x=210,y=44)
sintrate2E.place(x=340,y=42,width=48)
smonthly2L.place(x=210,y=68)
smonthly2E.place(x=330,y=66,width=58)
#COLUMN 3
sdntloan3L.place(x=420,y=20)
sdntloan3E.place(x=475,y=18,width=123)
sintrate3L.place(x=420,y=44)
sintrate3E.place(x=550,y=42,width=48)
smonthly3L.place(x=420,y=68)
smonthly3E.place(x=540,y=66,width=58)
#CLOUMN 4
sdntloan4L.place(x=630,y=20)
sdntloan4E.place(x=685,y=18,width=123)
sintrate4L.place(x=630,y=44)
sintrate4E.place(x=760,y=42,width=48)
smonthly4L.place(x=630,y=68)
smonthly4E.place(x=750,y=66,width=58)

#######################
#------AUTO LOAN------#
#######################
autoloanL = tk.Label(master=frame2, text="AUTO LOAN")

#LOAN LABELS
autoloan1L = tk.Label(master=frame2, text="Loan 1 $")
autoloan2L = tk.Label(master=frame2, text="Loan 2 $")
autoloan3L = tk.Label(master=frame2, text="Loan 3 $")

#INTEREST LABELS
aintrate1L = tk.Label(master=frame2, text="Loan Interest Rate %")
aintrate2L = tk.Label(master=frame2, text="Loan Interest Rate %")
aintrate3L = tk.Label(master=frame2, text="Loan Interest Rate %")

#PAYMENT LABELS
amonthly1L = tk.Label(master=frame2, text="Monthly Payment $")
amonthly2L = tk.Label(master=frame2, text="Monthly Payment $")
amonthly3L = tk.Label(master=frame2, text="Monthly Payment $")

#YEARS LABELS
ayears1L = tk.Label(master=frame2, text="Years")
ayears2L = tk.Label(master=frame2, text="Years")
ayears3L = tk.Label(master=frame2, text="Years")

#LOAN ENTERIES
autoloan1E = tk.Entry(master=frame2, relief=GROOVE)
autoloan2E = tk.Entry(master=frame2, relief=GROOVE)
autoloan3E = tk.Entry(master=frame2, relief=GROOVE)

#DOWN PAYMENT ENTERIES
adownloan1E = tk.Entry(master=frame2, relief=GROOVE)
adownloan2E = tk.Entry(master=frame2, relief=GROOVE)
adownloan3E = tk.Entry(master=frame2, relief=GROOVE)

#INTEREST ENTERIES
aintrate1E = tk.Entry(master=frame2, relief=GROOVE)
aintrate2E = tk.Entry(master=frame2, relief=GROOVE)
aintrate3E = tk.Entry(master=frame2, relief=GROOVE)

#PAYMENT ENTERIES
amonthly1E = tk.Entry(master=frame2, relief=GROOVE)
amonthly2E = tk.Entry(master=frame2, relief=GROOVE)
amonthly3E = tk.Entry(master=frame2, relief=GROOVE)

#YEARS ENTERIES
ayears1E = tk.Entry(master=frame2, relief=GROOVE)
ayears2E = tk.Entry(master=frame2, relief=GROOVE)
ayears3E = tk.Entry(master=frame2, relief=GROOVE)

#CHECK BOX
cb1 = tk.BooleanVar()
cb2 = tk.BooleanVar()
cb3 = tk.BooleanVar()
acheckbox1 = tk.Checkbutton(master=frame2,text="LEASE", variable=cb1, onvalue=True, offvalue=False)
acheckbox2 = tk.Checkbutton(master=frame2,text="LEASE", variable=cb2, onvalue=True, offvalue=False)
acheckbox3 = tk.Checkbutton(master=frame2,text="LEASE", variable=cb3, onvalue=True, offvalue=False)

#DEFAULT VALUES
autoloan1E.insert(0 , "0")
autoloan2E.insert(0 , "0")
autoloan3E.insert(0 , "0")
aintrate1E.insert(0 , "0")
aintrate2E.insert(0 , "0")
aintrate3E.insert(0 , "0")
amonthly1E.insert(0 , "0")
amonthly2E.insert(0 , "0")
amonthly3E.insert(0 , "0")
ayears1E.insert(0 , "0")
ayears2E.insert(0 , "0")
ayears3E.insert(0 , "0")

#-----PLACEMENT-----#
autoloanL.place(x=357,y=0)
#COLUMN 1
autoloan1L.place(x=0,y=20)
autoloan1E.place(x=55,y=18,width=123)
aintrate1L.place(x=0,y=44)
aintrate1E.place(x=130,y=42,width=48)
amonthly1L.place(x=0,y=68)
amonthly1E.place(x=120,y=66, width=58)
ayears1L.place(x=0,y=90)
ayears1E.place(x=40,y=88, width = 50)
acheckbox1.place(x=105,y=90)
#COLUMN 2
autoloan2L.place(x=315,y=20)
autoloan2E.place(x=370,y=18,width=123)
aintrate2L.place(x=315,y=44)
aintrate2E.place(x=445,y=42,width=48)
amonthly2L.place(x=315,y=68)
amonthly2E.place(x=435,y=66, width=58)
ayears2L.place(x=315,y=90)
ayears2E.place(x=355,y=88, width = 50)
acheckbox2.place(x=420,y=90)
#COLUMN 3
autoloan3L.place(x=630,y=20)
autoloan3E.place(x=685,y=18,width=123)
aintrate3L.place(x=630,y=44)
aintrate3E.place(x=760,y=42,width=48)
amonthly3L.place(x=630,y=68)
amonthly3E.place(x=750,y=66, width=58)
ayears3L.place(x=630,y=90)
ayears3E.place(x=670,y=88, width = 50)
acheckbox3.place(x=735,y=90)

###########################
#------PERSONAL LOAN------#
###########################
perloanL = tk.Label(master=frame3, text="PERSONAL LOAN")

#LOAN LABELS
perloan1L = tk.Label(master=frame3, text="Loan 1 $")
perloan2L = tk.Label(master=frame3, text="Loan 2 $")
perloan3L = tk.Label(master=frame3, text="Loan 3 $")

#INTEREST LABELS
pintrate1L = tk.Label(master=frame3, text="Loan Interest Rate %")
pintrate2L = tk.Label(master=frame3, text="Loan Interest Rate %")
pintrate3L = tk.Label(master=frame3, text="Loan Interest Rate %")

#LOAN ENTERIES
perloan1E = tk.Entry(master=frame3, relief=GROOVE)
perloan2E = tk.Entry(master=frame3, relief=GROOVE)
perloan3E = tk.Entry(master=frame3, relief=GROOVE)

#INTEREST ENTERIES
pintrate1E = tk.Entry(master=frame3, relief=GROOVE)
pintrate2E = tk.Entry(master=frame3, relief=GROOVE)
pintrate3E = tk.Entry(master=frame3, relief=GROOVE)

#PAYMENT LABELS
pmonthly1L = tk.Label(master=frame3, text="Monthly Payment $")
pmonthly2L = tk.Label(master=frame3, text="Monthly Payment $")
pmonthly3L = tk.Label(master=frame3, text="Monthly Payment $")

#PAYMENT ENTERIES
pmonthly1E = tk.Entry(master=frame3, relief=GROOVE)
pmonthly2E = tk.Entry(master=frame3, relief=GROOVE)
pmonthly3E = tk.Entry(master=frame3, relief=GROOVE)

#DEFAULT VALUES
perloan1E.insert(0 , "0")
perloan2E.insert(0 , "0")
perloan3E.insert(0 , "0")
pintrate1E.insert(0 , "0")
pintrate2E.insert(0 , "0")
pintrate3E.insert(0 , "0")
pmonthly1E.insert(0 , "0")
pmonthly2E.insert(0 , "0")
pmonthly3E.insert(0 , "0")


#-----PLACEMENT-----#
perloanL.place(x=357,y=0)

#COLUMN 1
perloan1L.place(x=0,y=20)
perloan1E.place(x=55,y=18,width=123)
pintrate1L.place(x=0,y=44)
pintrate1E.place(x=130,y=42,width=48)
pmonthly1L.place(x=0,y=68)
pmonthly1E.place(x=120,y=67,width=58)
#COLUMN 2
perloan2L.place(x=315,y=20)
perloan2E.place(x=370,y=18,width=123)
pintrate2L.place(x=315,y=44)
pintrate2E.place(x=445,y=42,width=48)
pmonthly2L.place(x=315,y=68)
pmonthly2E.place(x=435,y=67,width=58)
#COLUMN 3
perloan3L.place(x=630,y=20)
perloan3E.place(x=685,y=18,width=123)
pintrate3L.place(x=630,y=44)
pintrate3E.place(x=760,y=42,width=48)
pmonthly3L.place(x=630,y=68)
pmonthly3E.place(x=750,y=67,width=58)

#####################
#------MORTGAGE------#
#####################
mortloanL = tk.Label(master=frame4, text="MORTAGE LOAN")

#LOAN LABELS
morloan1L = tk.Label(master=frame4, text="Loan 1 $")

#YEAR DURATION LABELS
mduration1L = tk.Label(master=frame4, text="Years:")

#PAYMENT LABELS
mmonthly1L = tk.Label(master=frame4, text="Monthly Payment $")

#INTEREST LABELS
mintrate1L = tk.Label(master=frame4, text="Loan Interest Rate %")

#LOAN ENTERIES
morloan1E = tk.Entry(master=frame4, relief=GROOVE)

#YEAR DURATION ENTERIES
mduration1E = tk.Entry(master=frame4, relief=GROOVE)

#INTEREST ENTERIES
mintrate1E = tk.Entry(master=frame4, relief=GROOVE)

#PAYMENT ENTERIES
mmonthly1E = tk.Entry(master=frame4, relief=GROOVE)

#DEFAULT VALUES
morloan1E.insert(0 , "0")
mduration1E.insert(0 , "0")
mintrate1E.insert(0 , "0")
mmonthly1E.insert(0 , "0")

#-----PLACEMENT-----#
mortloanL.place(x=357,y=0)

morloan1L.place(x=0,y=20)
morloan1E.place(x=55,y=18,width=123)
mmonthly1L.place(x=210,y=20)
mmonthly1E.place(x=330,y=18,width=58)
mintrate1L.place(x=420,y=20)
mintrate1E.place(x=550,y=18,width=48)
mduration1L.place(x=630,y=20)
mduration1E.place(x=670,y=18,width=48)

######################
#------EXPENSES------#
######################
#Gas, food, utilities + tax, subscriptions/memberships,
#home insurance 1, car insurance 3, medication,
#insurance deductible, downpayment
expensesL = tk.Label(master=frame5, text="MONTHLY EXPENSES")

#EXPENSE LABELS
gasL = tk.Label(master=frame5, text="Monthly Gas: $")
foodL = tk.Label(master=frame5, text="Monthly Food: $")
utilL = tk.Label(master=frame5, text="Monthly Utilities: $")
subL = tk.Label(master=frame5, text="Monthly Subscriptions: $")
homeinsL = tk.Label(master=frame5, text="Monthly Home Insurance: $")
carinsL = tk.Label(master=frame5, text="Monthly Car Insurance: $")
medsL = tk.Label(master=frame5, text="Monthly Meds: $")
dctblL = tk.Label(master=frame5, text="Insurance Premium: $")
downpayL = tk.Label(master=frame5, text="Down Pay: $")
prepaypenL = tk.Label(master=frame5, text="Pre-Pay Penalty: $")

#EXPENSE ENTERIES
gasE = tk.Entry(master=frame5, relief=GROOVE)
foodE = tk.Entry(master=frame5, relief=GROOVE)
utilE = tk.Entry(master=frame5, relief=GROOVE)
subE = tk.Entry(master=frame5, relief=GROOVE)
homeinsE = tk.Entry(master=frame5, relief=GROOVE)
carinsE = tk.Entry(master=frame5, relief=GROOVE)
medsE = tk.Entry(master=frame5, relief=GROOVE)
dctblE = tk.Entry(master=frame5, relief=GROOVE)
downpayE = tk.Entry(master=frame5, relief=GROOVE)
prepaypenE = tk.Entry(master=frame5, relief=GROOVE)

#DEFAULT VALUES
gasE.insert(0, "0")
foodE.insert(0, "0")
utilE.insert(0, "0")
subE.insert(0, "0")
homeinsE.insert(0, "0")
carinsE.insert(0, "0")
medsE.insert(0, "0")
dctblE.insert(0, "0")
downpayE.insert(0, "0")
prepaypenE.insert(0, "0")


##-----PLACEMENT-----#
expensesL.place(x=352,y=0)
#COLOUMN 1
gasL.place(x=0,y=20)
foodL.place(x=0,y=44)
utilL.place(x=0,y=68)
gasE.place(x=93,y=18,width=48)
foodE.place(x=100,y=42,width=48)
utilE.place(x=115,y=66,width=48)
#COLOUMN 2
subL.place(x=315,y=20)
homeinsL.place(x=315,y=44)
carinsL.place(x=315,y=68)
prepaypenL.place(x=315,y=92)
subE.place(x=470,y=18,width=48)
homeinsE.place(x=485,y=42,width=48)
carinsE.place(x=470,y=66,width=48)
prepaypenE.place(x=430,y=90,width=70)
#COLOUMN 3
medsL.place(x=625,y=20)
dctblL.place(x=625,y=44)
downpayL.place(x=625,y=68)
medsE.place(x=730,y=18,width=48)
dctblE.place(x=760,y=42,width=48)
downpayE.place(x=705,y=66,width=48)

#FRAME PACKING
frame0_1.pack(fill=tk.X)
frame0.pack()
frame1_2.pack(fill=tk.X)
frame1.pack()
frame2_3.pack(fill=tk.X)
frame2.pack()
frame3_4.pack(fill=tk.X)
frame3.pack()
frame4_5.pack(fill=tk.X)
frame4.pack()
frame5_6.pack(fill=tk.X)
frame5.pack()
frame6_7.pack(fill=tk.X)
frame6.pack()

#---------------VARIABLES---------------#
def getValues():
#*****STUDENT LOAN INPUTS*****#
    slbals = [sdntloan1E.get(), sdntloan2E.get(), sdntloan3E.get(), sdntloan4E.get()]
    slrates = [sintrate1E.get(), sintrate2E.get(), sintrate3E.get(), sintrate4E.get()]
    slmonths = [smonthly1E.get(), smonthly2E.get(), smonthly3E.get(), smonthly4E.get()]
#*****AUTO LOAN INPUTS*****#
    albals = [autoloan1E.get(), autoloan2E.get(), autoloan3E.get()]
    alrates = [aintrate1E.get(), aintrate2E.get(), aintrate3E.get()]
    almonths = [amonthly1E.get(), amonthly2E.get(), amonthly3E.get()]
    aleases = [cb1.get(), cb2.get(), cb3.get()]
#*****PERSONAL LOAN INPUTS*****#
    plbals = [perloan1E.get(), perloan2E.get(), perloan3E.get()]
    plrates = [pintrate1E.get(), pintrate2E.get(), pintrate3E.get()]
    plmonths = [pmonthly1E.get(), pmonthly2E.get(), pmonthly3E.get()]
#*****MORTAGE LOAN INPUTS*****#
    ml1bal = morloan1E.get()
    ml1rate = mintrate1E.get()
    ml1dur = mduration1E.get()
    ml1month = mmonthly1E.get()
#*****MONTHLY EXPENSE INPUTS*****#
    gas = int(gasE.get())
    food = int(foodE.get())
    util_tax = int(utilE.get())
    subscrp = int(subE.get())
    hins = int(homeinsE.get())
    carins = int(carinsE.get())
    meds = int(medsE.get())
    dctbl = int(dctblE.get())
    dpay = int(downpayE.get())
    prepaypenalty = int(prepaypenE.get())
    expenses = gas+food+util_tax+subscrp+hins+carins+meds+dctbl+dpay+prepaypenalty
#*****LOAN # and LOAN TYPE*****#
    loans = ["UN-SUBSIDIZED", "SUBSIDIZED", "PRIVATE-LOAN 1", "PRIVATE-LOAN 2"]
    loana = ["AUTO-LOAN 1", "AUTO-LOAN 2", "AUTO-LOAN 3"]
    loanp = ["PERSONAL LOAN 1", "PERSONAL LOAN 2", "PERSONAL LOAN 3", "PERSONAL LOAN 4"]
    loanm = ["MORTGAGE LOAN 1"]
    loant = ["------STUDENT LOAN(S)------", "------AUTO LOAN(S)------", "------PERSONAL LOAN(S)------", "------MORTGAGE LOAN(S)------"]
    return slbals, slrates, slmonths, albals, alrates, almonths, aleases, plbals, plrates, plmonths, ml1bal, ml1rate, ml1dur, ml1month, expenses, loans, loana, loanp, loanm, loant
#APPARANTLY I WANTED A LIST
#expensesList = [smonthly1E.get(), smonthly2E.get(), smonthly3E.get(), amonthly1E.get(), amonthly2E.get(), amonthly3E.get(), pmonthly1E.get(), pmonthly2E.get(), pmonthly3E.get(), mmonthly1E.get()]

def printFile():
    slbals, slrates, slmonths, albals, alrates, almonths, aleases, plbals, plrates, plmonths, ml1bal, ml1rate, ml1dur, ml1month, expenses, loans, loana, loanp, loanm, loant = getValues()
    ################################
    monthlypay = float((smonthly1E.get())) + float(smonthly2E.get()) + float(smonthly3E.get()) + float(amonthly1E.get()) + float(amonthly2E.get()) + float(amonthly3E.get()) + float(pmonthly1E.get()) + float(pmonthly2E.get()) + float(pmonthly3E.get()) + float(mmonthly1E.get())
    # test value #
    ################################
    # create program to choose the best monthly pay
    # amount for the clients income.
    # use their budget,
    # 15% savings if they dont have 2k saved up,
    # use their wants
    file_object = open(cnameE.get() + "'s" + " loan plan","w")
    user_file = functions(file_object)
    user_file.header(cnameE.get())
    for i in range(3):
        user_file.calcLoan(slbals[i], slrates[i], slmonths[i], loant[0], loans[i])
    for i in range(2):
        user_file.calcLoan(albals[i], alrates[i], almonths[i], loant[1], loana[i])
    for i in range (2):
        user_file.calcLoan(plbals[i], plrates[i], plmonths[i], loant[2], loanp[i])
    user_file.calcLoan(ml1bal, ml1rate, ml1month, loant[3], loanm)
    file_object.write("\r\n")
    user_file.getBudget(mnetincE.get(), ynetincE.get(), monthlypay, expenses)
    file_object.close()

def clearValues():
    mnetincE.delete(0, END)
    mnetincE.insert(0 , "0")
    ynetincE.delete(0, END)
    ynetincE.insert(0 , "0")
    cnameE.delete(0, END)
    cnameE.insert(0, "Enter Name")
    sdntloan1E.delete(0, END)
    sdntloan1E.insert(0 , "0")
    sdntloan2E.delete(0, END)
    sdntloan2E.insert(0 , "0")
    sdntloan3E.delete(0, END)
    sdntloan3E.insert(0 , "0")
    sdntloan4E.delete(0, END)
    sdntloan4E.insert(0 , "0")
    sintrate1E.delete(0, END)
    sintrate1E.insert(0 , "0")
    sintrate2E.delete(0, END)
    sintrate2E.insert(0 , "0")
    sintrate3E.delete(0, END)
    sintrate3E.insert(0 , "0")
    sintrate4E.delete(0, END)
    sintrate4E.insert(0 , "0")
    smonthly1E.delete(0, END)
    smonthly1E.insert(0 , "0")
    smonthly2E.delete(0, END)
    smonthly2E.insert(0 , "0")
    smonthly3E.delete(0, END)
    smonthly3E.insert(0 , "0")
    smonthly4E.delete(0, END)
    smonthly4E.insert(0 , "0")
    autoloan1E.delete(0, END)
    autoloan1E.insert(0 , "0")
    autoloan2E.delete(0, END)
    autoloan2E.insert(0 , "0")
    autoloan3E.delete(0, END)
    autoloan3E.insert(0 , "0")
    aintrate1E.delete(0, END)
    aintrate1E.insert(0 , "0")
    aintrate2E.delete(0, END)
    aintrate2E.insert(0 , "0")
    aintrate3E.delete(0, END)
    aintrate3E.insert(0 , "0")
    amonthly1E.delete(0, END)
    amonthly1E.insert(0 , "0")
    amonthly2E.delete(0, END)
    amonthly2E.insert(0 , "0")
    amonthly3E.delete(0, END)
    amonthly3E.insert(0 , "0")
    ayears1E.delete(0, END)
    ayears1E.insert(0 , "0")
    ayears2E.delete(0, END)
    ayears2E.insert(0 , "0")
    ayears3E.delete(0, END)
    ayears3E.insert(0 , "0")
    perloan1E.delete(0, END)
    perloan1E.insert(0 , "0")
    perloan2E.delete(0, END)
    perloan2E.insert(0 , "0")
    perloan3E.delete(0, END)
    perloan3E.insert(0 , "0")
    pintrate1E.delete(0, END)
    pintrate1E.insert(0 , "0")
    pintrate2E.delete(0, END)
    pintrate2E.insert(0 , "0")
    pintrate3E.delete(0, END)
    pintrate3E.insert(0 , "0")
    pmonthly1E.delete(0, END)
    pmonthly1E.insert(0 , "0")
    pmonthly2E.delete(0, END)
    pmonthly2E.insert(0 , "0")
    pmonthly3E.delete(0, END)
    pmonthly3E.insert(0 , "0")
    morloan1E.delete(0, END)
    morloan1E.insert(0 , "0")
    mduration1E.delete(0, END)
    mduration1E.insert(0 , "0")
    mintrate1E.delete(0, END)
    mintrate1E.insert(0 , "0")
    mmonthly1E.delete(0, END)
    mmonthly1E.insert(0 , "0")
    gasE.delete(0, END)
    gasE.insert(0, "0")
    foodE.delete(0, END)
    foodE.insert(0, "0")
    utilE.delete(0, END)
    utilE.insert(0, "0")
    subE.delete(0, END)
    subE.insert(0, "0")
    homeinsE.delete(0, END)
    homeinsE.insert(0, "0")
    carinsE.delete(0, END)
    carinsE.insert(0, "0")
    medsE.delete(0, END)
    medsE.insert(0, "0")
    dctblE.delete(0, END)
    dctblE.insert(0, "0")
    downpayE.delete(0, END)
    downpayE.insert(0, "0")
    acheckbox1.deselect()
    acheckbox2.deselect()
    acheckbox3.deselect()



#CALCULATE/PRINT BUTTON PRESS
calbutton = tk.Button(master=frame6,bd=10,relief=GROOVE, text="EXPORT FILE",padx=30,pady=20, command = lambda: printFile())
calbutton.pack(side=LEFT)
#CLEAR BUTTON PRESS
clrbutton = tk.Button(master=frame6,bd=6,relief="raised",text="CLEAR ALL",padx=30,pady=20, command = clearValues,)
clrbutton.pack(side=RIGHT)
window.mainloop()