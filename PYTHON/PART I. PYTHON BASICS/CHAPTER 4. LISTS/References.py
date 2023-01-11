Number = [0, 1, 2, 3, 4, 5, 6]
Number_1 = Number # A Reference Of The The Number variable Is Copied To The Number_1 Variable, Not Copy The List...

print('Number : ' + str(Number) + ' || ' + 'Number_1 : ' + str(Number_1)) # You Can Understand With This Code Line

Number_1[2] = 'Hello' # Replace The Values In The List


print('Number : ' + str(Number) + ' || ' + 'Number_1 : ' + str(Number_1))