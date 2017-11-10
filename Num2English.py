Ones = ['',' one',' two',' three',' four',' five',' six', ' seven', ' eight', ' nine']
ThroughTwenty =[' ten',' eleven',' twelve',' thirteen',' fourteen',' fifteen',' sixteen',' seventeen',' eighteen',' nineteen']
Tens = ['','',' twenty',' thirty',' fourty',' fifty',' sixty',' seventy',' eighty', ' ninety']
place = ['',' thousand',' million',' billion',' trilion',' quadrillion',' quintillion',' sextillion',' octillion' ' nonillion', ' decillion', ' udecillion', ' duodecillion', ' tredecillion', ' quatturordecillion', ' quindecillion', ' sexdecillion', ' septendecillion', ' octodecillion', ' novemdecillion', ' vigintillion']

def commas(number): #This determins the amout of times i need to find the number between a commas splice
    return number//3

def sayTheNumberOnes(number):
    return Ones[int(number)]

def sayTheNumberTens(number):
    output = ''    
    if (number == '00'):
        return output
    number=number[::-1]
    
    if (number[1] == '1'):
        output += ThroughTwenty[int(number[0])]
    else:
        output += Tens[int(number[1])] + sayTheNumberOnes(number[0])
    return output

def sayTheNumberHunds(number):
    output = ''
    if (number == '000'):
        return output
    if (number[0] == '0'):
        return sayTheNumberTens(number[1:3]) 
    else:
        return Ones[int(number[0])] + ' hundred' + sayTheNumberTens(number[1]+number[2])
        
def getCardinal(number,output,depth):
    number = str(number)

    if(number == ''):
        return output
    
    try:
        sh = sayTheNumberHunds(number[-3:])
        if(sh==''):
            output += sh
        else:
            output = sh + place[depth] + output
        return getCardinal(number[:-3],output,depth+1)
    except:
        pass

    try:
        sh = sayTheNumberTens(number[-2:])
        if(sh==''):
            output += sh
        else:
            output = sh + place[depth] + output
        return getCardinal(number[:-2],output,depth+1)
    except:
        pass

    try:
        sh = sayTheNumberOnes(number[-1:])
        if(sh==''):
            output += sh
        else:
            output = sh + place[depth] + output
        return getCardinal(number[:-1],output,depth+1)
    except:
        pass

while True:
    x = input()
    if x == ('n' or 'N'):
        print('ending program')
        break
    if x.isnumeric():
        print(getCardinal(x,'',0))
    else:
        print('Input must be a number! type n to stop')
        


