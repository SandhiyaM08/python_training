def count_lines(filename):
    with open(filename, 'r') as file:
        return sum(1 for _ in file)
print("Total lines:", count_lines("story.txt"))


