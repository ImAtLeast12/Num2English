#I just want a program that counts in english from 0 to 100
#Then to 999

Ones = ['',' one',' two',' three',' four',' five',' six', ' seven', ' eight', ' nine']

ThroughTwenty =[' ten',' eleven',' twelve',' thirteen',' fourteen',' fifteen',' sixteen',' seventeen',' eighteen',' nineteen']

Tens = ['','',' twenty',' thirty',' fourty',' fifty',' sixty',' seventy',' eighty', ' ninety']


nX = ['',' thousand',' million',' billion']
#This is all to find the fixed point form the vsauce video




#How I am going to do this is first start by the number
def commas(number): #This determins the amout of times i need to find the number between a commas splice
    return number//3 

def sayTheNumber(x='0',y='0',z='0'):
    return int(z+y+x)

def sayTheNumberOnes(number):
    stringNum = str(number)
    stringNum = stringNum[::-1]
    output = ''
    if (len(stringNum) == 1):
        ones = stringNum[0]
        output += (Ones[int(ones)])

        if(int(ones) == 0):
            output += (' zero')
        return output

def sayTheNumberTens(number):
    stringNum = number
    stringNum = stringNum[::-1]
    output = ''
    if(len(stringNum) == 2):
        ones = stringNum[0]
        tens = stringNum[1]
        if (int(tens)!= 1):
            output += (Tens[int(tens)])
            output += (Ones[int(ones)])
        else:
            output += (ThroughTwenty[int(ones)])
        return output

def sayTheNumberHunds(number):
    stringNum = str(number)
    stringNum = stringNum[::-1]
    output = ''
    stnLen = len(stringNum)

    if(stnLen == 1):    
        return sayTheNumberOnes(number)
    
    if(stnLen==2):
        return sayTheNumberTens(number)

    if(len(stringNum) == 2):
        ones = stringNum[0]
        tens = stringNum[1]
        if (int(tens)!= 1):
            output += (Tens[int(tens)])
            output += (Ones[int(ones)])
        else:
            output += (ThroughTwenty[int(ones)])
        return output

    
    ones = stringNum[0]
    tens = stringNum[1]
    hundreds = stringNum[2]
    #Then it is going to  be in the hundreds
    output += (Ones[int(hundreds)] + ' hundred')

    if (int(tens)!= 1):
        output += (Tens[int(tens)] )
        output += (Ones[int(ones)])
    else:
        output += (ThroughTwenty[int(ones)])
    return output



    

    

def getCardinal(number,output,depth):
    print('num: ' + str(number))
    segment = str(number)[::-1] #this reverse the number
    try:
        output = str(sayTheNumberHunds(str(segment[2])+str(segment[1])+str(segment[0]))) + nX[commas(depth)] + output 
        segment = segment[::-1]
        return getCardinal(segment[:-3],output,depth+3)
    except:
        try:
            output = str(sayTheNumberTens(str(segment[1])+str(segment[0]))) + nX[commas(depth)] + output
            segment = segment[::-1]
            return getCardinal(segment[:-2],output,depth)
        except:
            try:
                output = str(sayTheNumberOnes(segment[0])) + nX[commas(depth)]+ output
                segment = segment[::-1]
                return getCardinal(segment[:-1],output,depth)
            except:
                return output
    return str(output)
    

    
print('output: ' + str(getCardinal(0,'',0)))
print()
print('output: ' + str(getCardinal(1,'',0)))
print()
print('output: ' + str(getCardinal(12,'',0)))
print()
print('output: ' + str(getCardinal(123,'',0)))
print()
print('output: ' + str(getCardinal(12345,'',0)))
print()
print('output: ' + str(getCardinal(123456,'',0)))
print()
print('output: ' + str(getCardinal(1234567,'',0)))
print()
print('output: ' + str(getCardinal(12345678,'',0)))
print()
print('output: ' + str(getCardinal(123456789,'',0)))
print()


'''
for i in range(0,101): #adds a bunch of negatives which adds 8 for each one
    print(getCardinal(i))
'''
    
'''for n in range(0, 1000,2): #This only looks at 0 to 99
    for i in range(0,1000): #adds a bunch of negatives which adds 8 for each one
        x = sayTheNumber(i)
        if(len(x)+(8*n) == i):
            print(('negative x' + str(n) ) + x)'''
        
#so this is working quite well the only thing is that I don't want to have to make a case for each of these when they get added it would be better if I could consolidate these somehow
