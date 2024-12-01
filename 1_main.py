#reads input file
file_object = open("1_input.txt", "r")
file_text = file_object.read().splitlines()

#used to store input data
list_1 = []
list_2 = []

#split input data and converts to numbers
for line in file_text:
    values = line.strip().split("   ")
    if len(values) == 2:
        list_1.append(int(values[0]))
        list_2.append(int(values[1]))

list_1.sort()
list_2.sort()

distance = 0
for i in range(0, len(list_1)):
    distance += abs(list_1[i] - list_2[i])

print(distance)

    