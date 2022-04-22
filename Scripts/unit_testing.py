from extractor import extractor
from loader import loader
from trans1 import transform1
from trans2 import transform2


def unit_test_extractor():
    inp = extractor("UnitTests/", "", "extractor")
    for line in inp:
        print(line)


def unit_test_loader():
    output = "Loader is working fine!"
    loader("UnitTests/", output, "", "loader")
    loaded = extractor("UnitTests/", "", "loader")
    for line in loaded:
        print(line)


def unit_test_trans1():
    inp = extractor("UnitTests/", "", "firstTransformation")
    print("Before transformation: ")
    for line in inp:
        print(line)
    inp.seek(0)
    output = transform1(inp)
    print("After transformation: ")
    loader("UnitTests/", output, "", "firstTransformationOutput")
    loaded = extractor("UnitTests/", "", "firstTransformationOutput")
    for line in loaded:
        print(line)


def unit_test_trans2():
    inp = extractor("UnitTests/", "", "secondTransformation")
    print("Before transformation: ")
    for line in inp:
        print(line)
    inp.seek(0)
    print("After transformation: ")
    output = transform2(inp)
    loader("UnitTests/", output, "", "secondTransformationOutput")
    loaded = extractor("UnitTests/", "", "secondTransformationOutput")
    for line in loaded:
        print(line)


print("***Welcome to unit testing module for ETL system!***")
while True:
    print("Enter yes to continue, no to exit the module.")
    ans = input()
    if ans == "no":
        print('Thank you for using ETL! Made with love by Shreyash Vaish')
        break
    elif ans == "yes":
        while True:
            print("Which component you want to test? Enter 1 for extractor, 2 for loader, 3 for first transformation"
                  " and 4 for second transformation.")
            choice = int(input())
            if choice not in (1, 2, 3, 4):
                print('Please enter your choice correctly!')
                continue
            else:
                break
        if choice == 1:
            unit_test_extractor()
        elif choice == 2:
            unit_test_loader()
        elif choice == 3:
            unit_test_trans1()
        else:
            unit_test_trans2()
    else:
        print('Enter your choice correctly!')
