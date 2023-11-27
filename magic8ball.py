import random

#def randomnum():
#   question = ("Do you have a question?   ")
    #num = random.randint(1,10)
   # return num

def magic8(num):
    if(num == 1):
        print("yes")
    elif(num == 2):
        print("no")
    elif(num == 3):
        print("defidently")
    return num
    
question = ("Do you have a question?   ")

num = random.randint(1,10)
    

if "__name__" == "__main__":
    print(magic8())
