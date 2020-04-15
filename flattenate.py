# Flattenator contains a bunch of different methods for working with foxdot patterns to understand them and turn them into tidalcycles patterns!!!
# Created by ashlaeblume February 2020

# Original pattern in foxdot
pattern = 'x -{ }{-x {w-x} }w-{x{xo}  }-x --'
"""initial attempt, replaces items in the pattern string one by one
pattern = pattern.replace(' ', '~, ')
pattern = pattern.replace('x', 'bd, ')
pattern = pattern.replace('-', 'hh, ')
pattern = pattern.replace('o', 'sd, ')
"""
# Stores items in foxdot pattern string as a list
pattern = 'x -{ }{-x {w-x} }w-{x{xo}  }-x --'
sounds = ' qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM~!@#$%^&*-+=/?|:;<\\'
brackets = '[](){}'
foxpattern=[]
bracketobj=[]
# Fills foxpattern with all non-bracket sound characters otherwise puts bracket item in its own list
for item in pattern:
    if item in sounds:
        foxpattern.append(item)
    elif item in brackets:
        bracketobj.append(item)
# TESTING printout of foxdot pattern string as list
print('foxpattern:',foxpattern)
# Dictionary translates string pattern syntax from foxdot into tidal
dic = {' ':'~', 'x':'bd', '-':'hh', 'o':'sd'}
tidalpattern=[dic.get(n, n) for n in foxpattern]
# TESTING printout of tidal pattern string as list
print('tidalpattern',tidalpattern)
# For each item in pattern string, checks whether item is a pattern object or a bracket
# Stores sounds & brackets in lists
soundobj=[]
for item in pattern:
    if item in sounds:
        soundobj.append(item)
# TESTING printout of items in bracket & sound lists created from pattern
print('brackets from pattern:',bracketobj)
print('sounds from pattern:',soundobj)
# Creates minimal sound and bracket lists of pattern string's LCD (least common denominator), i.e. stores one of each type of substring from pattern string
min_b_list=[]
for item in bracketobj: #bracketobj is a list of all instances of brackets in pattern string
    if item not in min_b_list:
        min_b_list.append(item)
print('minimal brackets list',min_b_list)
min_s_list=[]
for item in soundobj:#soundobj is a list of all instances of sounds in pattern string
    if item not in min_s_list:
        min_s_list.append(item)
print('minimal sounds list',min_s_list)
# ITWORKS!!!!!!!
# findcurly
# Finds left curly brackets and makes a list of their indices from within pattern string
Lcurl='{';
Rcurl='}';
pattern = 'x -{ }{-x {w-x} }w-{x{xo}  }-x --'
def leftCurly(pattern):
        leftcurls=[]
        for i in range(len(pattern)):
            if pattern[i] is Lcurl:
                leftcurls.append(i)
        return leftcurls
# Same with right curly brackets
def rightCurly(pattern):
        rightcurls=[]
        for i in range(len(pattern)):
            if pattern[i] is Rcurl:
                rightcurls.append(i)
        return rightcurls
x=leftCurly(pattern)
y=rightCurly(pattern)
print(x)
print(y)
# ITWORKS!!!!!!!


# Makes a class called Checker to iterate through numbers (for later use as lookahead method)
class Checker:
    # Iterator that checks for values in patterns
    def __init__(self, begin=0):
        self.thisvalue=begin
    def __iter__(self):
        return self
    def __next__(self):
        thisvalue = self.thisvalue
        self.thisvalue +=1
        return thisvalue
c = Checker()
print(next(c))
indexlist=[]
for i in range(10):
    indexlist.append(next(c))
print(indexlist)
# ITWORKS!!!!!!!

# Makes a generator called plusone for iterating through next values of lists etc; generators can act as an iterator and have access to using next() &.c
nextval = (i+1 for i in range(10))
newlist=[]
for i in range(10):
    try:
        newlist.append(next(nextval))
    except StopIteration:
        print('iteration is finished')
# TESTING!!!
print(newlist)
# ITWORKS!!!!!!!

# Checks total length of pattern. next we want to analyze the "structure" of the pattern itself. need to make sure that brackets, whitespaces, commas, and double-letter-sounds are dealt with properly in the string/sequence...

# Working with original pattern string to check values
plen = len(pattern)
print('pattern length is',plen,'\n')
for i in range(plen):
    if pattern[i] in brackets:
        print('yatta!       ',pattern[i],'index:',i)
    else:
        print('patternvalue:',pattern[i],'index:', i)
    i = i + 1

# Maybe i should do a hybrid intermediary step where the original string is turned into a list of single-character values? Then don't have to deal with double-char objects, and convert afterwads. Brackets are still a problem. Dive deeper into bracket types.
# [] square brackets represent a step
# () round brackets represent an "option/choice"
# {} curly brackets represent "randomness"; also represent one step
# Deal with () since it seems most difficult to understand


# Creates a list of all SynthDefs
synths = []
for item in SynthDefs:
    synths.append(item)
# TESTING
print('random synth is:',random.choice(synths))
# ITWORKS!!!!!!!
# Creates a list from a string of every percussion sample sound
drumstring = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM~!@#$%^&*-+=/?|:;<\\"
percs = []
for item in drumstring:
    percs.append(item)
# TESTING
print('all percussion/sound samples:',percs)
#print(percussion[-1])
# ITWORKS!!!!!!!
# Randomly choosing a percussion sample
print('random percussion sample is:',random.choice(percs))


# Pseudocode for playing random sounds from a curly bracket
# Creates a list out of sound string
x_pattern = '(x--x,xo  ox)([oo],[---])x-x{rg:}'
# Creates an iterator out of sounds string & list
x_iter = iter(x_pattern)
# TESTING
#print(next(x_iter))
x_list = []
for item in x_pattern:
        x_list.append(next(x_iter))
#    try:
#    x_list.append(next(x_iter))
#    except StopIteration:
#        print('all finished')
print(x_list)
# ITWORKS!!!! some comments break the code... also i don't remember why i wanted to make this....

#VERSION
# Creates a list from a string of every percussion sample sound
drumstring = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM~!@#$%^&*-+=/?|:;<\\"
drumlist = []
drum_iter=iter(drumstring)
for item in drum_iter: # throws an error for last item '\\'
    if next(drum_iter) is not '\\':
        drumlist.append(next(drum_iter))
    else:
        print('next item is \\')
# TESTING
print (drumlist)
# ITWORKS... sort of... don't remember what this was trying to do...


#Steps:
# loop until you find {. if no {, then exit
# check next item until you find }. if no } then need to throw an error for incomplete formatting
# go back to loop again, start with {. look to next character and store in rands while next is not }
# if next is }, don't store in rands, and exit loop.
# if possible: check string for all { and all } before looping, count number of occurrences


# Figuring how many curly brackets are in the pattern string, and which ones are matches with each other
#Just to keep track:
#index val 0123456789012345678901234567
pattern = 'x --x {w-x} w-{x{xo}  }-x --'
num_Lbrackets=pattern.count('{')
print('num_Lbrackets=',num_Lbrackets)
num_Rbrackets=pattern.count('}')
print('num_Rbrackets=',num_Rbrackets)
if num_Lbrackets is num_Rbrackets:
    print('even number of curly brackets!')
else:
    print('odd number of curly brackets!')
# Returns starting index within pattern of find's argument
Lcurl1=pattern.find('{')
print('1st Lcurl index=',Lcurl1)
Rcurl1=pattern.find('}')
print('2st Rcurl index=',Rcurl1)
# Finding the next curly brackets
Lcurl2=pattern.find('{', Lcurl1+1,len(pattern))
print('2nd Lcurl index=',Lcurl2)
Rcurl2=pattern.find('}',Rcurl1+1,len(pattern))
print('2nd Rcurl index=',Rcurl2)
"""
check:
is there even or odd number of {}??
if more than one {, find 1st { and look right to find next {...maybe find last using rfind()??
check between the { to see if there's a }
if there are no }, look to the right of the next { to find the first }
maybe make a list storing the indext values of each {} then match them up using the index list
"""
# inbetween is a list of all the items enclosed within first { and last } of pattern string
pattern = 'x --x {w-x} w-{x{xo}  }-x --'
inbetween=[]
Lcurl=pattern.find('{')
Rcurl=pattern.rfind('}')
for i in range(Lcurl+1, Rcurl-1):
    inbetween.append(pattern[i])
#TESTING
print('everything in-between first and last curly brackets:',inbetween)
# ITWORKS!!!!!!!

# Finding curly bracket substrings
pattern = 'x --x {w-x} w-{x{xo}  }-x --'
Lcurl='{'
Rcurl='}'
w=pattern.find(Lcurl) #returns -1 if not found
x=pattern.find(Rcurl) #returns index of first instance of arg
y=pattern.rfind(Lcurl) #rfind returns last instance of arg
z=pattern.rfind(Rcurl) #rfind returns last instance of arg
# TESTING
print('first instance of { is at index:',w)
print('first instance of } is at index:',x)
print('last instance of { is at index:',y)
print('last instance of } is at index:',z)
# ITWORKS!!!!!!!


# For figuring how to handle all bracket types:
# Maybe i should do a hybrid intermediary step where the original string is turned into a list of single-character values? Then don't have to deal with double-char objects, and convert afterwads. Brackets are still a problem. Dive deeper into bracket types.
# [] square brackets represent a step
# () round brackets represent an "option/choice"
# {} curly brackets represent "randomness"; also represent one step
# Deal with () since it seems most difficult to understand
