#GCD or HCF program in python

#defining GCD function to calculate GCD 
def gcd(m,n):
  for i in range(1,min(m,n)+1):
    if m%i==0 and n%i==0:
      cf=i
  return(cf)
#read M,N values and assign them to two variables
a=int(input("enter m value"))
b=int(input("enter n value"))

#printing GCD value of a,b by calling GCD function
print("GCD of {} and {} is {}".format(a,b,gcd(a,b)))
