#Python program to return N number of Common Factors
# here i hyave used modified Gcd method and added a list to store common factors
def gcd(m,n,n):
  cf=[] # List to store common factors
  for i in range(1,min(m,n)+1):
    if m%i==0 and n%i==0:
      cf.append(i)
  return(cf[-n:]) #returns n number of common factors

a=int(input("enter m value"))
b=int(input("enter n value"))
c=int(input("enter no of common factors required"))

print("GCD of {} and {} is {}".format(a,b,gcd(a,b,n)))
