from driver import driver

print('****Welcome to ETL!****')
print('Here we will run the output of the transformations on the 10 pretested inputs.')

for i in range(6):
    print('****Pretest ' + str(i+1) + '****')
    print('INPUT:')
    inp = open("Input/input" + str(i+1) + ".txt")
    for line in inp:
        print(line)
    print("\n")
    driver("Input/", "Output/", 1, i + 1, str(i + 1) + 'A')
    print('OUTPUT FOR TRANSFORMATION 1:')
    out = open("Output/output" + str(i+1) + "A.txt")
    for line in out:
        print(line)
    print("\n")
    driver("Input/", "Output/", 2, i + 1, str(i + 1) + 'B')
    print('OUTPUT FOR TRANSFORMATION 2:')
    out = open("Output/output" + str(i + 1) + "B.txt")
    for line in out:
        print(line)
    print("\n")

print("All the presets have been completed and saved. You can check them in the output directory!")
print("Thank you for using ETL! Made with love by Shreyash Vaish")
