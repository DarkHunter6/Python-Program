import sys
from sys import*
Student_Record = {'Name' : ' ', 'Roll' : ' ', 'Address' : ' ', 'Dist' : ' '}

def Std_Record():
    print('Enter Your Details : ')
print('Enter Your Name : ')
Name = input()
print('Enter Your Roll : ')
Roll = input()
print('Enter Your Address : ')
Address = input()
print('Enter Your Dist : ')
Dist = input()

Student_Record = {'Name' : Name, 'Roll' : Roll, 'Address' : Address, 'Dist' : Dist}

print('Enter The Student Name To See Details : ')
Name = input()
for Name in Student_Record.items():
    print(Student_Record)
    break
    # for K, V in Student_Record.items():
        # print('Key : ' + K + 'Value : ' + str(V))
# if Name in Student_Record:
#     print('The Student Record Is In The Database', Student_Record)
# else:
print('Do You Want To Insert The New Record Into The Database ? Y / N')
ab = input()
if ab == 'Y':
    Std_Record()
else:
    sys.exit()