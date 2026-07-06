# Question
'''Moore’s Law states that the number of transistors on a computer chip doubles around every 2 years.
That means growth isn’t linear – it’s exponential.

Create two variables:

transistors; for the number of transistors on your computer right now (e.g. 25000000000).
years; for the time into the future (e.g. 10).

To calculate the future number of transistors:
transistors = transistors.2**(years/2)
​
Print the new transistors.'''

print("=====================================================================")

transistors=25000000000
years=10

transistors=transistors*2**(years/2)
print(transistors)

print("=====================================================================")

a = float(input("enter the current number of transistor : "))
b = float(input("enter the number of future years after which you want to know the number of transistor : "))

transistors=a*2**(b/2)

print(transistors)
