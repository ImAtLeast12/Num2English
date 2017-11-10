Ones = ['',' one',' two',' three',' four',' five',' six', ' seven', ' eight', ' nine']
ThroughTwenty =[' ten',' eleven',' twelve',' thirteen',' fourteen',' fifteen',' sixteen',' seventeen',' eighteen',' nineteen']
Tens = ['','',' twenty',' thirty',' fourty',' fifty',' sixty',' seventy',' eighty', ' ninety']
place = ['',' thousand',' million',' billion',' trilion',' quadrillion',' quintillion',' sextillion',' octillion' ' nonillion', ' decillion', ' udecillion', ' duodecillion', ' tredecillion', ' quatturordecillion', ' quindecillion', ' sexdecillion', ' septendecillion', ' octodecillion', ' novemdecillion', ' vigintillion']
def sayTheNumberOnes(number):
    return Ones[int(number)]
def sayTheNumberTens(number):
    if (number == '00'): return ''
    if (number[0] == '1'): return ThroughTwenty[int(number[1])]
    else: return Tens[int(number[0])] + sayTheNumberOnes(number[1])
def sayTheNumberHunds(number):
    output = ''
    if (number == '000'): return output
    if (number[0] == '0'):return sayTheNumberTens(number[1:3]) 
    else: return Ones[int(number[0])] + ' hundred' + sayTheNumberTens(number[1]+number[2])
stn=[sayTheNumberHunds,sayTheNumberTens,sayTheNumberOnes]
def getCardinal(number,output,depth):
    number = str(number)
    if(number == ''):
        return output
    for i in range(3):
        try:
            sh = stn[i](number[-3+i:])
            if(sh==''):
                output += sh
            else:
                output = sh + place[depth] + output
            return getCardinal(number[:-3+i],output,depth+1)
        except:
            pass
for i in range(5):
    print(getCardinal(input(),'',0))
