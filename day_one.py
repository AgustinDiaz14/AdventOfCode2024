def calculate_distances(filepath):
    file = open(filepath, "r")
    total_sum = 0
    first_col = []
    second_col = []
    for x in file:
        line = x
        columns = line.split("   ")
        first_col.append(int(columns[0]))
        second_col.append(int(columns[1].replace("\n", "")))

    sorted_first = sorted(first_col)
    sorted_second = sorted(second_col)

    for i in range(len(first_col)):
        partial_diff = abs(sorted_first[i] - sorted_second[i])
        total_sum += partial_diff
    file.close()
    return total_sum

if __name__ == '__main__':
    print(calculate_distances("./inputs/day_one/historian_hysteria.txt"))