#python version = 3.11
""" Basic arithmetic Operations include
  1. Addition ( + )
  2. Subtraction ( - )
  3. Multiplication ( * )
  4. Division ( / )
  """
# we use input() method to read input or values from user.
#input by default reads the input as a string/charecter so we typecast the input into our desired input datatype
A= int(input("Enter a number"))

B= int(input("Enter a number"))

sum = A+B
print("Sum of {} and {} is {}".format(A,B,sum))

difference = A - B
print("Difference between {} and {} is {}".format(A,B,difference))

mul = A * B
print("Multiplication of  {} times {} is {}".format(A,B,mul))

rem = A/B
print("Division of {} and {} is {}".format(A,B,rem))
