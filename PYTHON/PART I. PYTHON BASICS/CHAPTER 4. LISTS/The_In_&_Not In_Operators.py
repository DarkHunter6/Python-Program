Cars = ['BUGATTI', 'NISSAN', 'PAGANI', 'LYKAN HYPERSPORT', 'LAMBORGHINI'] 
print('NISSAN' in Cars) # In Operator
print('NISSAN' not in Cars) # Not In Operator

# ---------- To Check The Item Is In The List Or Not ----------- 

Cars = ['BUGATTI', 'NISSAN', 'PAGANI', 'LYKAN HYPERSPORT', 'LAMBORGHINI'] 
print('Enter The Car Name :')
Car = input()
if Car not in Cars:
    print('Your Car Is Not In The List Sir')
else:
    print('Your Car Is In The List...!')