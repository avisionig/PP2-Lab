def toDigit(s):
    temp = 0
    for i in range(0, len(s), 3):
        if (s[i:i+3] == 'ONE'): 
            temp = temp * 10 + 1
        if (s[i:i+3] == 'TWO'): 
            temp = temp * 10 + 2
        if (s[i:i+3] == 'THR'): 
            temp = temp * 10 + 3
        if (s[i:i+3] == 'FOU'): 
            temp = temp * 10 + 4
        if (s[i:i+3] == 'FIV'): 
            temp = temp * 10 + 5
        if (s[i:i+3] == 'SIX'): 
            temp = temp * 10 + 6
        if (s[i:i+3] == 'SEV'): 
            temp = temp * 10 + 7
        if (s[i:i+3] == 'EIG'): 
            temp = temp * 10 + 8
        if (s[i:i+3] == 'NIN'): 
            temp = temp * 10 + 9
        if (s[i:i+3] == 'ZER'): 
            temp = temp * 10
    return temp
def toLetter(n):
    temp = ''
    while (n > 0):
        d = n % 10
        if (d == 1): temp = 'ONE' + temp
        if (d == 2): temp = 'TWO' + temp
        if (d == 3): temp = 'THR' + temp
        if (d == 4): temp = 'FOU' + temp
        if (d == 5): temp = 'FIV' + temp
        if (d == 6): temp = 'SIX' + temp
        if (d == 7): temp = 'SEV' + temp
        if (d == 8): temp = 'EIG' + temp
        if (d == 9): temp = 'NIN' + temp
        if (d == 0): temp = 'ZER' + temp
        n //= 10
    return temp
str = input()
x = str[0: str.find('+')]
y = str[str.find('+') + 1: len(str)]
print(toLetter(toDigit(x)+toDigit(y)))