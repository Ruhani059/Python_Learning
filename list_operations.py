numbers = [i for i in range (1,10)]
print numbers
numbers = [1,3,2,5,9,4,2]
numbers.sort()
print numbers
numbers.append(10)
for i in range (0,len(numbers)):
    for j in range(i, len(numbers)):
        if(numbers[i] > numbers[j]):
            numbers[i],numbers[j] = numbers[j],numbers[i]
print numbers

