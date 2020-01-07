def romanToInt(s):
    total = 0
    i = 0
    while i < len(s):
        if(i+1<len(s) and s[i]=='I' and s[i+1]=='V'):
            total+=4
            i+=1
        elif(i+1<len(s) and s[i]=='I' and s[i+1]=='X'):
            total+=9
            i+=1
        elif(i+1<len(s) and s[i]=='X' and s[i+1]=='L'):
            total+=40
            i+=1
        elif(i+1<len(s) and s[i]=='X' and s[i+1]=='C'):
            total+=90
            i+=1
        elif(i+1<len(s) and s[i]=='C' and s[i+1]=='D'):
            total+=400
            i+=1
        elif(i+1<len(s) and s[i]=='C' and s[i+1]=='M'):
            total+=900
            i+=1
        elif(s[i] == 'I'): total+=1
        elif(s[i] == 'V'): total+=5
        elif(s[i] == 'X'): total+=10
        elif(s[i] == 'L'): total+=50
        elif(s[i] == 'C'): total+=100
        elif(s[i] == 'D'): total+=500
        elif(s[i] == 'M'): total+=1000
        i+=1
    return total