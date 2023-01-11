Name = {'Tushar Paul' : {'Roll' : 177580759, 'Age' : 23, 'Address' : 'Kholta'},
        'Koushik Saha' : {'Roll' : 177580597, 'Age' : 25, 'Address' : 'Khagrabari'},
        'Anirban Panja' : {'Roll' : 177580976, 'Age' : 23, 'Address' : 'Alipurduar'}}

def StudentDetails(Student, Details):
    AllDetails = 0
    for K, V in Name.items():
        AllDetails = V.get(Details, 0)
    return AllDetails
print('* * * * * All Student Details * * * * *')
print('1. Tushar Paul '  +  str(StudentDetails(Name, 'Roll')))
print('2. Koushik Saha '  +  str(StudentDetails(Name, 'Roll')))
print('3. Anirban Panja '  +  str(StudentDetails(Name, 'Roll')))