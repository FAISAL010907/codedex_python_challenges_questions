#Question 

'''Even numbers (2, 4, 6, 8) and odd numbers (1, 3, 5, 7) pop up a lot in programming. 
   Knowing them is key to solving many coding problems.

  An even number is divisible by 2 and An odd number leaves a remainder of 1 when divided by 2.
  So how can we program this? We can use the % modulo operator to find the remainder:

   Even → n % 2 == 0
   Odd → n % 2 == 1
   Create a num variable and give it any number.

   Use a print() and % modulo operator to see if it's divisible by 2.'''

print("============================================================================")

#Solution 1:-

num = 250
print(num%2)

print("============================================================================")
#Solution 2:-

num = float(input("enter the number : "))
print("the remainder is ", num%2)

if num%2 == 0:
     print("since the remainder is zero its is an EVEN ")

else :
     print("since the remainder is not zero its is an ODD ")