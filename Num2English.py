#I just want a program that counts in english from 0 to 100
#Then to 999

Ones = ['','one','two','three','four','five','six', 'seven', 'eight', 'nine']

ThroughTwenty =['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']

Tens = ['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty', 'ninety']


##This is all to find the fixed point form the vsauce video


def sayTheNumber(number):
    stringNum = str(number)
    stringNum = stringNum[::-1]
    output = ''
    
    if(len(stringNum) == 3):
        ones = stringNum[0]
        tens = stringNum[1]
        hundreds = stringNum[2]
        #Then it is going to  be in the hundreds
        output += (Ones[int(hundreds)] + 'hundred')

        if (int(tens)!= 1):
            output += (Tens[int(tens)] )
            output += (Ones[int(ones)])
        else:
            output += (ThroughTwenty[int(ones)])
        return output

    if(len(stringNum) == 2):
        ones = stringNum[0]
        tens = stringNum[1]
        if (int(tens)!= 1):
            output += (Tens[int(tens)])
            output += (Ones[int(ones)])
        else:
            output += (ThroughTwenty[int(ones)])
        return output
    
    if (len(stringNum) == 1):
        ones = stringNum[0]
        output += (Ones[int(ones)])

        if(int(ones) == 0):
            output += ('zero')
        return output

for n in range(0, 1000,2): #This only looks at 0 to 99
    for i in range(0,1000): #adds a bunch of negatives which adds 8 for each one
        x = sayTheNumber(i)
        if(len(x)+(8*n) == i):
            print(('negative' * n) + x)
        
#so this is working quite well the only thing is that I don't want to have to make a case for each of these when they get added it would be better if I could consolidate these somehow
