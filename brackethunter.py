import itertools
pattern = 'x -{ }{-x {w-x} }w-{x{xo}  }-x --'
bracket_types=['{','}','(',')','<','>','[',']']
def isBracket(this_char): # maybe this is a bad name...?
    if this_char in pattern:
        print(this_char,'is in pattern')
        if this_char in bracket_types:
            pass
            print(this_char,'is a bracket')
isBracket('}')
def allBrackets(): # maybe this is a bad name...?
    allbrackets=[]
    for item in pattern:
        if item in bracket_types:
            allbrackets.append(item)
    print('allbrackets:',allbrackets)
    return allbrackets
allBrackets()
def bracketCount(this_bracket):
    numbrackets=0
    for item in pattern:
        if item is this_bracket:
            numbrackets+=1
    print('# of',this_bracket,'brackets:',numbrackets)
bracketCount('{')
def lCurls():
    leftcurls=[]
    for i in range(len(pattern)):
        if pattern[i] is '{':
            leftcurls.append(i)
    print('lCurls:',leftcurls)
    return leftcurls
lindex=lCurls()
# rCurls returns list of indices of all '}' found in pattern
def rCurls():
    rightcurls=[]
    for i in range(len(pattern)):
        if pattern[i] is '}':
            rightcurls.append(i)
    print('rCurls:',rightcurls)
    return rightcurls
rindex=rCurls()
# Generates a list of names for left bracket items [L0,L1,L2...]
def lNames():
    leftitems=[]
    for i in range(len(lindex)):
        'L'+str(i)==lindex[i]
        leftitems.append('L'+str(i))
    print('lNames:',leftitems)
    return leftitems
    #return leftitems
#lNames()
# Generates a list of names for right bracket items [R0,R1,R2...]
def rNames():
    rightitems=[]
    for i in range(len(rindex)):
        'R'+str(i)==rindex[i]
        rightitems.append('R'+str(i))
    print('rNames:',rightitems)
    return rightitems
#rNames()
lnames=lNames()
rnames=rNames()
#Create a dictionary to talk between bracket indices and names
# OPTION3: creates a list and a  dictinary of the tuple pairs linking the bracket names to their indices
"""
def positionDict():
    # lcpd is 'left curl position dict', a list of tuples which groups bracket names with their indices
    lcpd={i:j for (i,j) in zip(lnames, lindex)}
    return lcpd
    print('leftcurl position dict',lcpd)
    # rcpd is 'right curl position dict', a list of tuples which groups bracket names with their indices
    rcpd={i:j for (i,j) in zip(rnames, rindex)}
    return rcpd
    print('rightcurl position dict',rcpd)
#NEED TO figure out how to get 'L0' to yield the value from lindex[0]
positionDict()
"""
lcpd={i:j for (i,j) in zip(lnames, lindex)}
rcpd={i:j for (i,j) in zip(rnames, rindex)}
print(' ')
print('     EXAMPLES:')
#print('     L0:',lcpd['L0'])
print('lcpd keys:',lcpd.keys())
print('lcpd values:',lcpd.values())
print('lcpd items:',lcpd.items())
print(' ')
def keyValues():
    for key,value in lcpd.items():
        print('key',key,'->','value',value)
    for key,value in rcpd.items():
        print('key',key,'->','value',value)
def pairList():
    # lcpl is left curl pairs list, a list of tuples which group bracket names with their indices
    lcpl=list(zip(lnames,lindex))
    # rcpl is right curl pairs list, a list of tuples which group bracket names with their indices
    rcpl=list(zip(rnames,rindex))
    pairlist=lcpl+rcpl
    return pairlist
    print(pairlist)
def merge(dict1, dict2):
    result = {**dict1, **dict2}
    print('dict merge result:',result)
    return result
pairs=merge(lcpd,rcpd)
#print(pairs['L0'])
#for key,value in pairs.items():
#    print(key)
#    print(value)
#    key=value
b_pairs=[]
if len(lindex) == len(rindex):
    num_bpairs = len(lindex)
# Need to come up with a way to define L0, L1, etc... in a recursive way and not just explicitly...
le0=pairs['L0']
le1=pairs['L1']
le2=pairs['L2']
ri0=pairs['R0']
ri1=pairs['R1']
ri2=pairs['R2']
print('values for inequivalences:',le0,le1,le2,ri0,ri1,ri2)
# build bracket pairs by determining which are the pairs that close first/faster than others, that is how the pair dictionary will be built
#pairWise()
"""
warning: the following is only for the case where there are THREE(3) paors of brackets...need to generalize!!!
"""
"""
if le0<ri0<le1:
    if le1<ri1<le2:
        b_pairs=[(le0,ri0),(le1,ri1),(le2,ri2)]
        print('a/1:',b_pairs)
    elif le1<le2<ri1:
        b_pairs=[(le0,ri0),(le2,ri1),(le1,ri2)]
        print('a/2:',b_pairs)
elif le1<ri0<le2:
    if ri0<ri1<le2:
        b_pairs=[(le1,ri0),(le0,ri1),(le2,ri2)]
        print('b/3:',b_pairs)
    elif ri0<le2<ri1:
        b_pairs=[(le1,ri0),(le2,ri1),(le0,ri2)]
        print('b/4:',b_pairs)
elif le2<ri0:
    b_pairs=[(le2,ri0),(le1,ri1),(le0,ri2)]
    print('c/5:',b_pairs)
"""
"""
something like:
for all brackets in patternstring:
    find leftmost bracket, find rightmost bracket
    bracket total is B
    remaining brackets is B-2
    while num_leftB < B/2 & num_rightB < B/2:
        for next bracket object:
            if right:
                add +1 to the left/right bracket counter
                close the bracket pair
            if left:
                add +1 to the left/right bracket counter
                move to next bracket
                if right:
                    add +1 to the left/right bracket counter
                    close the bracket pair
                if left:
                    add +1 to the left/right bracket counter
                    move to next bracket
"""
lC=lCurls()
rC=rCurls()
def findLeftmost():
    return lC[0]
def findRightmost():
    return rC[0]
#
lTot=len(lC)
rTot=len(rC)
B = lTot + rTot
remaining = lTot - 1
#
leftmost=findLeftmost()
rightmost=findRightmost()
#
def findNextBracket(pattern):
    for bracket in pattern:
        for i in range(leftmost,rightmost):
            pass
findNextBracket(pattern)





for '{', '}' in pattern:

    #bracket total is B
    #remaining brackets is B-2
    while lTot < B/2 & rTot < B/2:
        for next bracket object:
            if right:
                add +1 to the left/right bracket counter
                close the bracket pair
            if left:
                add +1 to the left/right bracket counter
                move to next bracket
                if right:
                    add +1 to the left/right bracket counter
                    close the bracket pair
                if left:
                    add +1 to the left/right bracket counter
                    move to next bracket
