keypad = [  [ '1' , '2' , '3'] ,
            [ '4' , '5' , '6'] ,
            [ '7' , '8' , '9'] ]

code = ''

#cuz searching for an element in a set is O(1)
set3 = {0 , 1 , 2}

with open(r'C:\Users\zerou\Documents\PythonWS\MC_challenge_3\doc.txt' , 'r') as document:
    doc = document.readlines()
    for line in doc:
        r , c = 1 , 1
        for i in range(len(line)):
            if (line[i] == 'U') and (r+1 in set3):
                r += 1
            elif (line[i] == 'D') and (r-1 in set3):
                r -= 1
            elif (line[i] == 'R') and (c+1 in set3):
                c += 1
            elif (line[i] == 'L') and (c-1 in set3):
                c -= 1
            else:
                code += keypad[r][c]
                break
    
    print(code)
