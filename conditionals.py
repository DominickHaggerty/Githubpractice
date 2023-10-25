def main():
    test1("Monday")
    
def test1(today):
    if(today == "Monday"):
        print("Today is Monday")
    elif(today == "Wednesday"):
        print("today is Wednesday")
    elif(today == "Thursday"):
        print("today is Thursday")
    elif(today == "Friday"):
        print("Today is Friday")
    else:
        print("Today is Tuesday")


isRaining=False
rainisLikely=False

if(isRaining or rainisLikely):
    print("bring an umbrella")
else:
    print("it is not going to rain")

if __name__ == '__main__':
    main()