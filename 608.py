matrix = []

for i in range(3):
    matrix.append([])
    for j in range(3):
        matrix[i].append(eval(input()))

largestList = [max(matrix[0]), max(matrix[1]), max(matrix[2])]
smallestList = [min(matrix[0]), min(matrix[1]), min(matrix[2])]

largest = max(largestList)
smallest = min(smallestList)

largestIndex1 = largestList.index(largest)
smallestIndex1 = smallestList.index(smallest)

largestIndex2 = matrix[largestIndex1].index(largest)
smallestIndex2 = matrix[smallestIndex1].index(smallest)

print('Index of the largest number %d is: (%d, %d)' %
      (largest, largestIndex1, largestIndex2))
print('Index of the smallest number %d is: (%d, %d)' %
      (smallest, smallestIndex1, smallestIndex2))
