#!python3
 
"""
##### Task 1
The bank calculates the amount of interest you earn using the simple interest formula:
interest = principal * rate * #days in the month / 365

Ask the user to enter the amount of their principal, the number of days in the month the rate of interest expressed as a percentage.  Calculate the amount of interest they would be paid.

example:
Enter your amount: 100
Enter the rate: 2.5
Enter the # of days in the month: 30
You earned $0.2 interest. 
(2 points) 
"""
principal = input("Enter principal:")
rate = input("Enter rate in percentage:")
time = input("Enter the amount of days in months:")

principal = float(principal)
rate = float(rate)
time = int(time)

rate = rate/100
intrest = principal * rate * time/365 

intrest = round(intrest, 2)

print(f"Your intrest is {intrest}")