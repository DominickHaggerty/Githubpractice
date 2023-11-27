import random

def main():
    magic8()

 

def magic8():
    input("Do you have a question?   ")
    num = random.randint(1,10)

    if(num == 1):
        print("yes")
    elif(num == 2):
        print("no")
    elif(num == 3):
        print("defidently")
    elif(num == 4):
        print("probably")
    elif(num == 5):
        print("maybe")
    elif(num == 6):
        print("probably not")
    elif(num == 7):
        print("dont get your hopes up")
    elif(num == 8):
        print("without a doubt")
    elif(num == 9):
        print("cant say for certain right now")
    else:
        print("you may rely on it")    

if __name__ == "__main__":
    main()

    