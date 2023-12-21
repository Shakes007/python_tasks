import math

print("Welcome to the Financial Calculator!")
print("")

user = input("""You may select from either a Bond Repayment Calculator or an Investment Calculator:
             Bond - to calculate the amount you'll have to repay on a home loan.
             Investment - to calculate the amount of interest you'll earn on your investment.
             Enter either 'Bond' or 'investment' to proceed:  """)

print("")

# Gets the information from the user in order to calculate the bond repayment.
if user.lower() == "bond":
    p = float(input("Please enter the present value of the house (in R):  "))
    rate1 = float(input("Please enter the interest rate (%):   "))
    n = int(input("Please enter the number of months you'll take to repay the loan: "))

# In 'i': i must first be / by 100 to convert to a percentage then / 12 to get the monthly intertest rate.
    i = (rate1 / 100) / 12
    repayment = (i * p)/(1 - (1 + i)**(-n))

    print("")
    print(f"Your total repayment amount per month is: R {round(repayment,2)}")

else:
    p = float(input("Please enter the amount you will be investing: R "))
    rate2 = float (input("Please enter the interest rate(%): "))
    t = float(input("Please enter the number of years you are going to invest for: "))

    print("")
# Get users input on which interest type the user would like to use.
    interest = input("""which type of interest would you prefer: Simple or Compound interest.
                     Enter 'simple' or 'compound': """) 
    print("")
    
    r = rate2 / 100
# If the user selects the 'simple' interest the computer will execute this program.
    if interest.lower() == "simple":
        a = p * (1 + (r*t))

        print(f"Your invesment return after {math.trunc(t)} years is R {round(a,2)}.")
        
# if the user selects 'compound' interest the computer will execute this program. 
    else: 
        a = p * math.pow((1 + r),t)
        print(f"Your investment return after {math.trunc(t)} years is R {round(a,2)}.")

