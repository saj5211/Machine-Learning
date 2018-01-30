import random as random

question_1 = []
question_2 = []
question_3 = []
question_4 = []
question_5 = []
question_6 = []
question_7 = []
population = random.randint(100,120)
for i in range (0,108):
    question_1.append(random.randrange(0, 3))
    question_2.append(random.randrange(0, 2))
    question_3.append(random.randrange(0, 2))
    question_4.append(random.randrange(0, 10))
    question_5.append(random.randrange(0, 10))
    question_6.append(random.randrange(0, 3))
    question_7.append(random.randrange(0, 3))

def yesnomay(question):
    yes= 0
    no =0
    may = 0
    for i in question:
        if question[i] == 2:
            yes +=1
        elif question[i]==1:
            may += 1
        else:
            no+=1
    print str(yes) +  ", " +str(may) + ", " + str(no)

def yesno(question):
    yes= 0
    no =0

    for i in question:
        if question[i] == 1:
            yes +=1
        else:
            no+=1
    print str(yes) +  ", " + str(no)

def oneToTen(question):
    one=0
    two=0
    three=0
    four=0
    five=0
    six=0
    seven=0
    eight=0
    nine=0
    ten=0
    for i in question:
        if question[i] == 0:
            one +=1
        elif question[i]==1:
            two += 1
        elif question[i] == 2:
            three += 1
        elif question[i] == 3:
            four += 1
        elif question[i] == 4:
            five += 1
        elif question[i] == 5:
            six += 1
        elif question[i] == 6:
            seven += 1
        elif question[i] == 7:
            eight += 1
        elif question[i] == 8:
            nine += 1
        else:
            ten+=1
    print str(one) +  ", " +str(two) + ", " + str(three) + ", " + str(four) + ", " + str(five) + ", "+ str(six) + ", " + str(seven) +", " +str(eight) + ", " + str(nine) + ", " + str(ten)
print population
yesnomay(question_1)
print ""
yesno(question_2)
print ""
yesno(question_3)
print ""
oneToTen(question_4)
print ""
oneToTen(question_5)
print ""
yesnomay(question_6)

yesnomay(question_7)
