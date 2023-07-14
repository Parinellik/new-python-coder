work_h = int(input("Enter hours worked: "))
pay_rate_h = eval(input("Enter hourly pay rate: "))
OT_pay_rate_h = 2

if work_h > 40:
    #if OT pay rate per hour= 2
    OT = (work_h - 40) * OT_pay_rate_h
    gross_p = (40 * pay_rate_h) + OT
    print ("Gross pay = RM %s (RM %s overtime included)" % (gross_p, OT))

else:
    gross_p = work_h * pay_rate_h
    print ("Gross pay = RM ", gross_p)
    
