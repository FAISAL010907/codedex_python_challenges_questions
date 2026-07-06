# Question
'''You just got your first credit card! 😅
Each month, the bank adds interest to any unpaid balance. That means your debt can quietly grow...

Let's see how much you’ll owe next month:

balance=balance+(balance×interest rate)

Create two variables:
balance: for how much you owe (e.g. 250.00).
rate: for the interest rate (e.g. 0.02 for 2%).

Calculate how much you owe with interest.
Print the new "balance".'''

# Solution 1 :-
balance = 250
intrest_rate = 0.02

balance = balance+(balance*intrest_rate)

print(balance)                
print("=====================================================================")

#Solution 2 :-

a = float(input("how much is your unpaid balance of this month : "))
rate=float(input("what is your intrest rate per month : "))
balance = a+(a*rate)

print("the amount you owe this month according to your intrest per month : ",balance)
