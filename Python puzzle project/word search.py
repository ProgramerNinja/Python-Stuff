##Cody Dzierzon
##Jared McMahon
##11/16/2018
import random
puzzle = ("LPZQEVGVLRTFPXHYFGGREPYUHFRNDZQAAEIGUITZKVRTTXPRWCVTOZIBNYU"+
                     "VZTCVHHGUVFNRULFFCKPFNAELOOBTPYEOOLFBTANDSTRINGNESRHQAPTLIH"+
                     "AGPJKFQRKRRAHTMEEWOAQVUBRPVVWOUELSEDNRNXMDEPWISURUGWRHPLIJA"+
                     "KCJLPBEDPIAMZHSEWARHTYXIXBELNMWKTVWSHFXJBOFHFFYTICPLEXUENQS"+
                     "NRKRWLZETVFBYXNRBOPSREYDGSGFLDYDCDIWNLTWWAHTTEPXYTSHZNCCPRZ"+
                     "SKKRCRRPKVIVCXRICODFYPJDEOVOBQSXDMFQMDFOWLMUQDXFPHIZMLLDUPA"+
                     "RRSKCDHAHRMOUQZCCZCFOSYXHKNMRYZIGGWKXEDNIJTAHD")
question1 =""
question2 =""
question3 =""
question4 =""
question5 =""
question6 =""
question7 =""
question8 =""
question9 =""
question10 =""
question11 =""
question12 =""
question13 =""
question14 =""
question15 =""
question16 =""
question17 =""
question18 =""
question19 =""
question20 =""

answer1 ="TRUE"
answer2 ="IMPORT"
answer3 ="FOR"
answer4 ="RETURN"
answer5 ="ELSE"
answer6 ="ELIF"
answer7 ="BREAK"
answer8 ="DEF"
answer9 ="ERROR"
answer10 ="SYNTAX"
answer11 ="OPERATOR"
answer12 ="INDEX"
answer13 ="INTERGER"
answer14 ="FLOAT"
answer15 ="STRING"
answer16 ="IF"
answer17 ="WHILE"
answer18 ="BOOLEAN"
answer19 ="FUNCTION"
answer20 ="PYTHON"

    

def display_puzzle():
    ##pre sets up puzzles
    line=" "
    line2=" "
    line3=" "
    line4=" "
    line5=" "
    line6=" "
    line7=" "
    line8=" "
    line9=" "
    line10=" "
    line11=" "
    line12=" "
    line13=" "
    line14=" "
    line15=" "
    line16=" "
    line17=" "
    line18=" "
    line19=" "
    line20=" "

    
    ##sets up puzzle
    for i in range(len(puzzle)):
        if i <= 19:
            line =line + puzzle[i]+" | "
        elif i<=39:
            line2 = line2 + puzzle[i]+" | "
        elif i<=59:
            line3 = line3 + puzzle[i]+" | "
        elif i<=79:
            line4 = line4 + puzzle[i]+" | "
        elif i<=99:
            line5 = line5 + puzzle[i]+" | "
        elif i<=119:
            line6 = line6 + puzzle[i]+" | "
        elif i<=139:
            line7 = line7 + puzzle[i]+" | "
        elif i<=159:
            line8 = line8 + puzzle[i]+" | "
        elif i<=179:
            line9 = line9 + puzzle[i]+" | "
        elif i<=199:
            line10 = line10 + puzzle[i]+" | "
        elif i<=219:
            line11 = line11 + puzzle[i]+" | "
        elif i<=239:
            line12 = line12 + puzzle[i]+" | "
        elif i<=259:
            line13 = line13 + puzzle[i]+" | "
        elif i<=279:
            line14 = line14 + puzzle[i]+" | "
        elif i<=299:
            line15 = line15 + puzzle[i]+" | "
        elif i<=319:
            line16 = line16 + puzzle[i]+" | "
        elif i<=339:
            line17 = line17 + puzzle[i]+" | "
        elif i<=359:
            line18 = line18 + puzzle[i]+" | "
        elif i<=379:
            line19 = line19 + puzzle[i]+" | "
        elif i<=399:
            line20 = line20 + puzzle[i]+" | "

##prints puzzle
    print(line)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
    print(line7)
    print(line8)
    print(line9)
    print(line10)
    print(line11)
    print(line12)
    print(line13)
    print(line14)
    print(line15)
    print(line16)
    print(line17)
    print(line18)
    print(line19)
    print(line20)

def puzzle():
    index_pos=""
    found_word=""
    positions=input("input the index of each letter seperated by commas")

    for i in (positions):
        if i == ",":
            x=int(index_pos)
            found_word = found_word + puzzle[x]
            index_pos = ""
            continue
        index_pos = index_pos+i
    if found_word == answer:
        score=10-attempts
        points+=score
        print("ya you got it")
        break
    else:
        attemps=attemps+1
        print("try again")









    


display_puzzle()

