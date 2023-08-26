#Prime number identification

t=int(input()) # read a number
cf=1 # initialise common factor as 1
l=round(t/2)+1 # calculating mid value to reduce number of iterations
for i in range(1,l):
    if t%i==0: # checking whether the number is divisible by i or not if yes update cf value to i
        cf=i

if cf==1: # checking if cf value is 1 or not if yes its a prime number if not its not a prime number
    print("{} is a prime number".format(t))
else:
    print("{} is not a prime number".format(t))
