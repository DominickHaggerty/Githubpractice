passage = '''I remember sittin' at that house
Thinkin' no way them boys wouldn't win
Between them, big three pitchers
Andrew and chipper
It was gonna be hard to keep up with the Jones
But as fate would have it
That Atlanta magic
Got putout by them Padres'''

newPara = ""

def madlibsJoiner(passage,prompt,start,end):
    return(passage[start:end]+input(prompt))

newPara += madlibsJoiner(passage,"enter an ing verb:",0,11)
newPara += madlibsJoiner(passage,"entert a location:",18,27)
newPara += madlibsJoiner(passage,"enter an ing verb:",32,33)
newPara += madlibsJoiner(passage,"enter a person",41,49)
newPara += madlibsJoiner(passage,"enter a verb",58,68)
newPara += madlibsJoiner(passage,"enter an adjective",71,86)
newPara += madlibsJoiner(passage,"enter a number greater than 1",89,90)
newPara += madlibsJoiner(passage,"enter a noun",95,96)
newPara += madlibsJoiner(passage,"enter a person",104,105)
newPara += madlibsJoiner(passage,"enter another person",111,116)
newPara += madlibsJoiner(passage,"enter a pronoun",124,124)
newPara += madlibsJoiner(passage,"enter an adjective",126,140)
newPara += madlibsJoiner(passage,"enter someone",144,165)
newPara += madlibsJoiner(passage,"enter a noun",170,178)
newPara += madlibsJoiner(passage,"enter a pronoun",182,194)
newPara += madlibsJoiner(passage,"enter a city",196,202)
newPara += madlibsJoiner(passage,"enter a noun",209,210)
newPara += madlibsJoiner(passage,"enter a past tense verb",215,216)
newPara += madlibsJoiner(passage,"enter a group verb",219,220)
newPara += madlibsJoiner(passage,"enter a noun",226,235)

def madlibsEnd(passage,start):
    return(passage[start:])

newPara += madlibsEnd(passage,248)


print(newPara)                                                                


