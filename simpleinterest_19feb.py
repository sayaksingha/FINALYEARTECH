def rateOfInterest(p,t,r):
    return (p*t*r)/100;
price =int(input("enter your require price  "));
rate=int(input("enter rate of interrest "));
time =int(input("enter time"));
print(f"your rate of interest is {rateOfInterest(price,rate,time)}")

