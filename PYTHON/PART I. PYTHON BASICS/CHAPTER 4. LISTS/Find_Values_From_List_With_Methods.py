# --------------- Find Value With Index() ------------------- #

Call_Of_Duty = ['Captain Price', 'John Mactavish', 'Sandman', 'Ghost', 'Roach', 'Sgt.Foley']
COD_1 = Call_Of_Duty.index('Sandman')
print(COD_1)

# -------------- Insert Value With Append() And Insert() ---------------- #

Call_Of_Duty = ['Captain Price', 'John Mactavish', 'Sandman', 'Ghost', 'Roach', 'Sgt.Foley']
Call_Of_Duty.append('Sgt.Griggs') # Append() 
print(Call_Of_Duty)

Call_Of_Duty.insert(2, 'Sgt.Griggs') # Insert()
print(Call_Of_Duty)

# ------------- Removing Values From List With Remove() ----------------- #

Call_Of_Duty = ['Captain Price', 'John Mactavish', 'Sandman', 'Ghost', 'Roach', 'Sgt.Foley']
Call_Of_Duty.remove('Sgt.Foley')
print(Call_Of_Duty)

# --------------- Sorting Values With Sort() -------------------- #

Call_Of_Duty = ['E', 'd', 'C', 'b', 'A'] # Sorting List By Their First Alphabet Like A, B Or C
Call_Of_Duty.sort(key = str.lower)
print(Call_Of_Duty)
