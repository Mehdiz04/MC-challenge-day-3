keypad = [  [ '1' , '2' , '3'] ,
            [ '4' , '5' , '6'] ,
            [ '7' , '8' , '9'] ]

code = ''

#cuz searching for an element in a set is O(1)
set3 = {0 , 1 , 2}

with open(r'C:\Users\zerou\Documents\PythonWS\MC_challenge_3\doc.txt' , 'r') as document:
    doc = document.readlines()
    for line in doc:
        i , j = 1 , 1
        for i in range(len(line)):
            if (line[i] == 'U') and (i+1 in set3):
                i += 1
            elif (line[i] == 'D') and (i-1 in set3):
                i -= 1
            elif (line[i] == 'R') and (j+1 in set3):
                j += 1
            elif (line[i] == 'L') and (j-1 in set3):
                j -= 1
            else:
                code += keypad[i][j]
                break
    
    print(code)