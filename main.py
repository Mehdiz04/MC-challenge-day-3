#fixed
keypad = [  [ '1' , '2' , '3'] ,
            [ '4' , '5' , '6'] ,
            [ '7' , '8' , '9'] ]

code = ''

#cuz searching for an element in a set is O(1)
set3 = {0 , 1 , 2}

movements = {'U':[1 , 0] , 'D':[-1 , 0] , 'R':[0 , 1] , 'L':[0 , -1]}

with open(r'C:\Users\zerou\Documents\PythonWS\MC_challenge_3\doc.txt' , 'r') as document:
    doc = document.readlines()
    for line in doc:
        r , c = 1 , 1
        for l in line[:-1]:
            if (r + movements[l][0] in set3) and (c + movements[l][1] in set3):
                r += movements[l][0]
                c += movements[l][1]
            else:
                continue

        code += keypad[r][c]

    print(code)
