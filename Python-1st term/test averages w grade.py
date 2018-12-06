#test score avereging program

def get_test_average():
    global average
    test1 = input("test 1: ")
    test2 = input("test 2: ")
    test3 = input("test 3: ")
    test4 = input("test 4: ")
    test5 = input("test 5: ")
    test6 = input("test 6: ")
    test7 = input("test 7: ")
    test8 = input("test 8: ")
    test9 = input("test 9: ")
    test10 = input("test 10: ")
    test_sum = float(test1) + float(test2) + float(test3) + float(test4) + float(test5) + float(test6) + float(test7) + float(test8) + float(test9) + float(test10)
    average = test_sum/10 
    print (average)

def  letter_score():
    if average >= 90:
        print("A")
    elif average >= 80:
        print ("B")
    elif average >= 70:
        print ("C")
    elif average >= 60:
        print ("D")
    elif average >= 50:
        print ("F... OOOOOOOOOOf")
    elif average < 50:
        print("You are very dumb!!!")
    else:
        print("Something went wrongl.")

get_test_average()
letter_score()
