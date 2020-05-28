simbol = '#'
one = "  "+simbol
two = simbol*3
three = simbol+" "+simbol
four = simbol+"  "

def Display(number):
    line1 = line2 = line3 = line4 = line5 = ""
    try:
        #number=int(number)
        number=str(number)
        assert number.isdigit()
        for idx, i in enumerate(number): #line 1
            if int(i) == 1:
                if idx == 0:
                    line1 = one
                else:
                    line1 = line1 + " " + one
            elif int(i) == 4:
                if idx == 0:
                    line1 = three
                else:
                    line1 = line1 + " " + three
            else:
                if idx == 0:
                    line1 = two
                else:
                    line1 = line1 + " " + two                

        print(line1)

        for idx,i in enumerate(number): #line 2
            if int(i) == 1 or int(i) == 2 or int(i) == 3 or int(i) == 7:
                if idx == 0:
                    line2 = one
                else:
                    line2 = line2 + " " + one                
            elif int(i) == 5 or int(i) == 6:
                if idx == 0:
                    line2 = four
                else:
                    line2 = line2 + " " + four                  
            else:
                if idx == 0:
                    line2 = three
                else:
                    line2 = line2 + " " + three  
                     
        print(line2)

        for idx,i in enumerate(number): #line 3
            if int(i) == 0:
                if idx == 0:
                    line3 = three
                else:
                    line3 = line3 + " " + three
            elif int(i) == 1 or int(i) == 7:
                if idx == 0:
                    line3 = one
                else:
                    line3 = line3 + " " + one
            else:
                if idx == 0:
                    line3 = two
                else:
                    line3 = line3 + " " + two       
        
        print(line3)
        
        for idx,i in enumerate(number): #line 4
            if int(i) == 2:
                if idx == 0:
                    line4 = four
                else:
                    line4 = line4 + " " + four
            elif int(i) == 0 or int(i) == 6 or int(i) == 8:
                if idx == 0:
                    line4 = three
                else:
                    line4 = line4 + " " + three
            else:
                if idx == 0:
                    line4 = one
                else:
                    line4 = line4 + " " + one
        
        print(line4)

        for idx,i in enumerate(number): #line 5
            if int(i) == 1 or int(i) == 4 or int(i) == 7:
                if idx == 0:
                    line5 = one
                else:
                    line5 = line5 + " " + one
            else:
                if idx == 0:
                    line5 = two
                else:
                    line5 = line5 + " " + two
        print(line5)
            
    except AssertionError:
        print('Error: wrong input.')
        return None
    return 1

def Test(num):
    Display('1'*num)
    print("\n")
    Display('2'*num)
    print("\n")
    Display('3'*num)
    print("\n")
    Display('4'*num)
    print("\n")
    Display('5'*num)
    print("\n")
    Display('6'*num)
    print("\n")
    Display('7'*num)
    print("\n")
    Display('8'*num)
    print("\n")
    Display('9'*num)
    print("\n")
    Display('0'*num)
    print("\n")



#Test(30)
Display("1982")