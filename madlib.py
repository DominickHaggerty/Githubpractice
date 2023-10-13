passage = '''I remember sittin' at that house 
Thinkin' no way them boys wouldn't win 
Between them, big three pitchers 
Andrew and chipper 
It was gonna be hard to keep up with the Jones 
But as fate would have it 
That Atlanta magic 
Got put out by them Padres'''

newPara = ""

start = 0
end = 11

newPara += passage[start:end]
newText1 = input('''enter an "i n g" verb: ''')
newPara += newText1

start = end + 7
end = start + 9


newPara += passage[start:end]
newText1 = input("enter a location: ")
newPara += newText1

start = end + 5
end = start + 2

newPara += passage[start:end]
newText1 = input('''enter an "i n g" verb: ''')
newPara += newText1

start = end + 8
end = start + 8

newPara += passage[start:end]
newText1 = input("enter a person/people: ")
newPara += newText1

start = end + 9
end = start + 10

newPara += passage[start:end]
newText1 = input("enter a verb: ")
newPara += newText1

start = end + 4
end = start + 17

newPara += passage[start:end]
newText1 = input("enter an adjective: ")
newPara += newText1

start = end + 5
end = start + 1

newPara += passage[start:end]
newText1 = input("enter a number: ")
newPara += newText1

start = end + 1
end = start + 8

newPara += passage[start:end]
newText1 = input("enter person, place, or thing: ")
newPara += newText1

start = end + 1
end = start + 1

print(newPara)                                                                


