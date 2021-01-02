import os


def get_files_list_sorted_by_lines_number(files_path):
    """Примет путь к файлам и возвратит отсортированный список кортежей с именем текстовых файлов
    и количеством строк в них."""
    files_dict = {}
    path, dirs, files = next(os.walk(files_path))
    for file in files:
        if file.endswith('.txt'):
            lines_counter = 0
            with open(path + '/' + file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line != '\n':
                        lines_counter += 1
            files_dict[path + '/' + file] = lines_counter
    sorted_files_list = sorted(files_dict.items(), key=lambda x: x[1])
    return sorted_files_list


def read_and_write(files):
    """Примет отсортированный список кортежей с именем текстовых файлов и количеством строк в них,
    прочитает файлы и объединит их в один файл result_task_3.txt"""
    with open('result_task_3.txt', 'w', encoding='utf-8') as document:
        for file in files:
            file_name = file[0][file[0].rfind('/')+1:]
            with open(file[0], 'r', encoding='utf-8') as f:
                lines = f.readlines()
                document.write(file_name + '\n')
                document.write(str(file[1]) + '\n')
                for line in lines:
                    if not line.strip().isspace():
                        document.write(line.strip() + '\n')


f_list = get_files_list_sorted_by_lines_number("./task_3")
read_and_write(f_list)
