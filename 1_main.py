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

#calculates the distance in between the lists
distance = 0
for i in range(0, len(list_1)):
    distance += abs(list_1[i] - list_2[i])

print("Distance:", distance)

#dict used to keep track of how much times a number in list_1 appears in list_2
similarity_tracker = {}

for i in range(0, len(list_1)):
    similarity_tracker[list_1[i]] = 0
    for j in range(0, len(list_2)):
        if list_2[j] == list_1[i]:
            similarity_tracker[list_1[i]] += 1

similarity_score = 0
for key, value in similarity_tracker.items():
    similarity_score += key * value

print("Similairty score: ", similarity_score)
