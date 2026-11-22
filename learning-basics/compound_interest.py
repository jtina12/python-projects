
#Python Program for Compound Interest
#A = P(1 + R/100) t 


#Compound Interest = A – P 


#Where, 


#A is amount 
#P is the principal amount 
#R is the rate and 
#T is the time span

# Python3 program to find compound
# interest for given values.
 
 
def compound_interest(principal, rate, time):
 
    # Calculates compound interest
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)
 
 
# Driver Code
compound_interest(100, 5, 1)




# Python3 program to find compound
# interest for input taking from user.
 
 
def compound_interest(principal, rate, time):
 
    # Calculates compound interest
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)
 
 
# Driver Code
#Taking input from user.
principal = int(input("Enter the principal amount: "))
rate = int(input("Enter rate of interest: "))
time = int(input("Enter time in years: " ))
#Function Call
compound_interest(principal,rate,time)


#Finding compound interest of given values without using pow() function.
# inputs 
p= 1200   # principal amount 
t= 2      # time 
r= 5.4    # rate 
# calculates the compound interest
a=p*(1+(r/100))**t  # formula for calculating amount 
ci=a-p  # compound interest = amount - principal amount
# printing compound interest value
print(ci)

#Compound Interest using for loop

def compound_interest(principal, rate, time):
    Amount = principal
    for i in range(time):
        Amount = Amount * (1 + rate/100)
    CI = Amount - principal
    print("Compound interest is", CI)
# Driver Code
compound_interest(100, 5,1)



