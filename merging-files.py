file_contents = []

for file_name in ["1.txt", "2.txt", "3.txt"]:
    with open(file_name, 'r') as file:
        lines = file.readlines()
        file_contents.append((file_name, len(lines), lines))

file_contents.sort(key=lambda x: x[1])

with open("merged.txt", 'w') as result_file:
    for file_info in file_contents:
        file_name, num_lines, lines = file_info
        result_file.write(f"{file_name}\n")
        result_file.write(f"{num_lines}\n")
        result_file.writelines(lines)

print("Файлы объединены. Результат записан в файл merged.txt.")