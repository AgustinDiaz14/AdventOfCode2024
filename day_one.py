def get_data(filepath):
    file = open(filepath, "r")
    first_col = []
    second_col = []
    for x in file:
        line = x
        columns = line.split("   ")
        first_col.append(int(columns[0]))
        second_col.append(int(columns[1].replace("\n", "")))

    sorted_first = sorted(first_col)
    sorted_second = sorted(second_col)

    file.close()

    return [sorted_first, sorted_second]

def calculate_distances(filepath):
    total_sum = 0
    data = get_data(filepath)
    for i in range(len(data[0])):
        partial_diff = abs(data[0][i] - data[1][i])
        total_sum += partial_diff

    return total_sum

def calculate_occurrences(filepath):
    total_sum = 0
    data = get_data(filepath)
    for i in range(len(data[0])):
        occurrences = data[1].count(data[0][i])
        total_sum += occurrences * data[0][i]
    return total_sum

if __name__ == '__main__':
    print(calculate_distances("./inputs/day_one/historian_hysteria.txt"))
    print(calculate_occurrences("./inputs/day_one/historian_hysteria.txt"))