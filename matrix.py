
# 2D array
two = [[1, 2], [3, 4]]

two[0][0] = 7

if two == [[7, 2], [3,4]]:
    print ("2D array works as expected")
else:
    print ("2D array doesn't work as expected")
    print (two)

#three = [ [[0, 0], [0, 0]], [[0, 0], [0, 0]]]
rows = 5
cols = 5
three = []
for r in range(rows):
    two = []
    for c in range(cols):
        two.append([0, 0])
    three.append(two)

print (three)

print (three[0][0][0])
three[0][0][0] = 10

if three == [[[10, 2], [3,4]], [[7, 2], [3,4]]]:
    print ("3D array works as expected")
else:
    print ("3D array doesn't work as expected")
    print (three)

