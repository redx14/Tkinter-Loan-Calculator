from datetime import date
import math
class functions:
    def __init__(self,file_object):
        self.file_object = file_object

    def header(self,user):
        self.file_object.write(user + "'s loan plan\r\n")
        date_today = date.today()
        today = date_today.strftime("Date: %m/%d/%Y\r\n\r\n")
        self.file_object.write("Advisor: Andrey Ilkiv\r\n")
        self.file_object.write(today)

    #Calculates Student loan | writes to file
    def calcLoan(self, amount, interest, monthlypay, loan, loanType):
        r = float(interest)/100
        p = float(amount)
        m = float(monthlypay)
        n = 0
        t = 12
        months = 0
        if (p > 0 and r > 0 and m > 0):
            n = -1*((math.log(1-((p/m)*(r/t))))/(t*(math.log(1+(r/t)))))
            n = round(n , 3)
            self.file_object.write(loan + "\r\n")
            self.file_object.write(loanType + "\r\n")
            self.file_object.write(f"Loan Balance: ${p:,.2f}\r\n")
            total = round(n*12*m,2)
            self.file_object.write(f"Total Loan Balance: ${total:,.2f}\r\n")
            self.file_object.write("Rate: " + str(round(r*100,2)) + "%\r\n")
            self.file_object.write(f"Monthly Payment: ${m:,.2f}\r\n")
            self.file_object.write("It will take you " + str(round(n,2)) + " years to pay of the loan\r\n")
            accinterest = total - p
            self.file_object.write("Total Interest to be paid over " + str(round(n*12,2)) + f" month(s): ${accinterest:,.2f}\r\n\r\n")
            while (total - m > 0):
                total = total - m
                months = months + 1
                self.file_object.write("Amount Remaining after " + str(months) + f" month(s): ${total:,.2f}\r\n")
            if (total - m <= 0):
                months = months + 1
                self.file_object.write("Amount Remaining after " + str(months) + " month(s): $" + str(0.00)+"\r\n\r\n")
        
    #Remaining money after loan
    def getBudget(self, Mincome, Yincome, monthlypay, expenses):
        self.file_object.write("------BUDGET------\r\n")
        budget = float(Mincome) + (float(Yincome)/12) - (monthlypay + expenses)
        weeklyb = budget/4
        self.file_object.write(f"Monthly budget after expenses: ${budget:,.2f}\r\n")
        self.file_object.write(f"Weekly Budget: ${weeklyb:,.2f}\r\n")

