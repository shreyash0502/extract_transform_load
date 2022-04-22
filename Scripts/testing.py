import os
from driver import driver

print('****Welcome to ETL!****')
while True:
    ans = input('\nEnter yes to continue, no to exit the program: ')
    if ans == 'yes':
        inpdir = ''
        outdir = ''
        choice = ''
        while True:
            inpdir = input("\nEnter the input directory (must end with a slash): ")
            if os.path.isdir(inpdir):
                break
            print("This directory does not exist. Try again!")

        while True:
            outdir = input("\nEnter the output directory (must end with a slash): ")
            if os.path.isdir(outdir):
                break
            print("This directory does not exist. Try again!")

        while True:
            choice = input("\nEnter the choice of transform [1: Transform1, 2: Transform2]: ")
            choice = int(choice)
            if choice == 1 or choice == 2:
                break
            print("Bad input for choice. Try again!")

        driver(inpdir, outdir, choice)
        print('Transformation done! Check your output directory.\n')

    elif ans == 'no':
        print('Thank you for using ETL! Made with love by Shreyash Vaish')
        break

    else:
        print('Enter your choice correctly!')