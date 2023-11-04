
print("CALCULATOR")
x=input("enter a first number ")
y=input("enter a second number ")
operation=input("enter any operation ")


def calculator(num1,num2,operation):
   
    if(num1.isnumeric() & num2.isnumeric()):
        a=float(num1)
        b=float(num2)
        
        if operation=="+":
            result=a+b
        
        elif operation=="-":
            result=a-b
        
        elif operation=="*":
            result=a*b
        
        elif operation=="/":
            result=a/b
       
        else:
            print("choose the operation from + ,-,*,/")
    
    else:
        print("enter a valid number")
    
    
    return result


print(calculator(x,y,operation))


