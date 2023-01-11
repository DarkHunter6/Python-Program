Hello = [1, 2, 3, 4, 5]
Spam = ['Tushar', 'Koushik', 'Anirban', 'Sourav', 'Timir']

print(Hello[2]) # Print Lists

print(Hello[2], Hello[3]) # Print The Perticular List Items

print(20 + Hello[2]) # Addition

print(Hello[-1], Hello[-3]) # Negative Indexes

print(Spam[2 : 3]) # First Value Slices The Starting Values And Second Value Slices The Last Values

print(len(Hello), len(Spam)) # See The Length Of The Total Values In Variables

Spam[1] = 'Sharmistha' # Change The Values Into The The List
print(Spam[0 :])

print([1, 2, 3, 4, 5] + ['Tushar', 'Koushik', 'Anirban', 'Sourav', 'Timir']) #List Concatenation

print(3 * [1, 2, 3, 4, 5]) # Replicate Items

del Spam[1] # Delete Items From Lists
print(Spam[0: ])