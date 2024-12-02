file = open("./inputs/day_one/historian_hysteria.txt", "r")
total_sum = 0
for x in file:
    partial_sum = 0
    line = file.readline()
    columns = line.split("   ")
    columns[1].replace("\n", "")
    for i in range(len(columns[0])):
        partial_sum += abs(int(columns[0][i]) - int(columns[1][i]))
    print(partial_sum)
    total_sum += partial_sum
print(total_sum)