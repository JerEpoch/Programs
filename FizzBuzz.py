#Print Fizzbuzz if divisible by 3 and 5
#Fuzz if divisiable by 3, Buzz if by 5
#Else just the number
i = 1

while i < 100:
    if(i % 3==0 and i % 5 == 0):
        print('FizzBuzz')
    elif(i % 3 == 0):
        print('Fuzz')
    elif(i % 5 == 0):
        print('Buzz')
    else:
        print(i)

    i+=1
    
        
        
    
