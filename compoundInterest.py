def compoundinterest(principal, rate, time):
    amount = principal * (pow((1 + rate / 100), time))
    ci = amount - principal
    return ci
price =int(input("enter your require price  "));
rate=int(input("enter rate of interrest "));
time =int(input("enter time"));
print(f"your rate of interest is {compoundinterest(price,rate,time)}")