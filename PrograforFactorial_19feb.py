def findFactorial(a):
    ans=1
    for i in range(a):
        ans*=(i+1)
    return ans   
    
first =int(input("enter first number "));
print(findFactorial(first))

