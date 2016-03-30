#compound interest
import math

def calcInterest(p, r, n, t):
#p, principle. r, interest rate
#n, number of times compouned a year
#t number of years
    total=p*((1+r/n)**(n*t))
    newTotal=round(total,2)
    print(newTotal)

    
def get_input():
    principle = int(input("Enter the principle amount: "))
    rate = float(input("Enter the interest rate: "))
    numberTimes = int(input("Enter how often the rate is compounded per year: "))
    years = int(input("Enter how many years you wish to calculate for: "))
    
    calcInterest(principle, rate/100, numberTimes, years)


get_input()

