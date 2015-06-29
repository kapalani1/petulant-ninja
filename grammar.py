def getRewriteRules(grammar,symbol):
    rules = []
    for (s,rule) in grammar:
        if symbol==s:
            rules.append((s,rule))
    return rules

def replaceAllOccurrences(character,rule,string):
    newString = []
    for i in xrange(len(string)):
        if string[i] == character:
            newString.extend(rule[1])
        else:
            newString.append(string[i])
    return newString

def isambigHelper(grammar,start,utterance,string):
    stack = [start]
    ct = 0
    while stack:
        string = stack.pop(0)
        if string==utterance:
            ct+=1
        if(ct>1):
            return True
        for char in string:
            rules = getRewriteRules(grammar,char)
            for rule in rules:
                stack.append(replaceAllOccurrences(char,rule,string))
    return ct>1

def isambig(grammar, start, utterance):
    return isambigHelper(grammar,start,utterance,[start])

grammar1 = [ 
       ("S", [ "P", ]),
       ("S", [ "a", "Q", ]) ,
       ("P", [ "a", "T"]),
       ("P", [ "c" ]),
       ("Q", [ "b" ]),
       ("T", [ "b" ]),
       ] 
print isambig(grammar1, "S", ["a", "b"]) 
print isambig(grammar1, "S", ["c"]) == False

grammar2 = [ 
       ("A", [ "B", ]),
       ("B", [ "C", ]),
       ("C", [ "D", ]),
       ("D", [ "E", ]),
       ("E", [ "F", ]),
       ("E", [ "G", ]),
       ("E", [ "x", "H", ]),
       ("F", [ "x", "H"]),
       ("G", [ "x", "H"]),
       ("H", [ "y", ]),
       ] 
print isambig(grammar2, "A", ["x", "y"]) == True
print isambig(grammar2, "E", ["y"]) == False

grammar3 = [ # Rivers in Kenya
       ("A", [ "B", "C"]),
       ("A", [ "D", ]),
       ("B", [ "Dawa", ]),
       ("C", [ "Gucha", ]),
       ("D", [ "B", "Gucha"]),
       ("A", [ "E", "Mbagathi"]),
       ("A", [ "F", "Nairobi"]),
       ("E", [ "Tsavo" ]),
       ("F", [ "Dawa", "Gucha" ])
       ] 
print isambig(grammar3, "A", ["Dawa", "Gucha"]) == True
print isambig(grammar3, "A", ["Dawa", "Gucha", "Nairobi"]) == False
print isambig(grammar3, "A", ["Tsavo"]) == False
