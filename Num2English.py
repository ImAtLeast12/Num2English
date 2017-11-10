Ones = ['',' one',' two',' three',' four',' five',' six', ' seven', ' eight', ' nine']
ThroughTwenty =[' ten',' eleven',' twelve',' thirteen',' fourteen',' fifteen',' sixteen',' seventeen',' eighteen',' nineteen']
Tens = ['','',' twenty',' thirty',' fourty',' fifty',' sixty',' seventy',' eighty', ' ninety']
place = ['',' thousand',' million',' billion',' trilion',' quadrillion',' quintillion',' sextillion',' octillion' ' nonillion', ' decillion', ' udecillion', ' duodecillion', ' tredecillion', ' quatturordecillion', ' quindecillion', ' sexdecillion', ' septendecillion', ' octodecillion', ' novemdecillion', ' vigintillion']
def sayOnes(seg):
    return Ones[int(seg)]
def sayTens(seg):
    if (seg == '00'): return ''
    if (seg[0] == '1'): return ThroughTwenty[int(seg[1])]
    else: return Tens[int(seg[0])] + sayOnes(seg[1])
def sayHunds(seg):
    output = ''
    if (seg == '000'): return output
    if (seg[0] == '0'):return sayTens(seg[1:3]) 
    else: return Ones[int(seg[0])] + ' hundred' + sayTens(seg[1:3])
stn=[sayHunds,sayTens,sayOnes]
def getCardinal(number,output,depth):
    number = str(number)
    if(number == ''):
        return output
    for i in range(len(stn)):
        try:
            sh = stn[i](number[-len(stn)+i:])
            if(sh==''):
                output += sh
            else:
                output = sh + place[depth] + output
            return getCardinal(number[:-len(stn)+i],output,depth+1)
        except:
            pass
for i in range(5):
    print(getCardinal(input(),'',0))
