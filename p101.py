import random
response=input("Would you like to roll a dice, y for yes n for no? ")
print('\n')
response='y'
while response=='y':
    number=random.randint(1,6)
    if number==1:
        print("⚀")
    elif number==2:
        print("⚁")
    elif number==3:
        print("⚂")
    elif number==4:
        print("⚃")
    elif number==5:
        print("⚄")
    elif number==6:
        print("⚅")
    response=input("Would you like to roll a dice, y for yes n for no? ")
    print('\n')
