def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if  __name__ == "__main__": 
    n = input('enter a number')
    
    print("factorial number is",factorial(int(n)))

  
    