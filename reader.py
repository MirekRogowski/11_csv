import os
import sys
import csv
file_csv_line = []


def list_directory(file, path):
    print(f"Brak pliku: {file} w katalogu: {path}")
    for line in os.listdir(path):
        # if os.path.isfile(line):
        #     print(f"file -> {line}")
        # elif os.path.isdir(line):
        #     print(f"DIR - > {line}")
        print(f"file -> {line}") if os.path.isfile(line) else print(f"DIR - > {line}")
    exit()


def open_file(file):
    with open(file, "r", newline="\n") as fr_csv:
        for line in csv.reader(fr_csv):
            file_csv_line.append(line)


def check_file(file, directory):
    # print("check diretory",directory)
    # print("check file ",file)
    # file_path1 = directory+ '\\'+ file
    # print(f"file_path 1 {file_path1}")
    # file_path = os.path.join(directory,file)
    # print("file_path", file_path)
    open_file(os.path.join(directory,file)) if os.path.isfile(file) else list_directory(file, directory)


def new_values(values):
    for lista in values:
        item = lista.split(",")
        y = int(item[0].strip())
        x = int(item[1].strip())
        value = item[2].strip()
        file_csv_line[y][x] = value


def write_new_value_csv(file):
    t = input("\nZapisac dane do pliku: (T/N)? ")
    if t.lower() == "t":
        with open(file, "w", newline="") as fw_csv:
            csv_writer = csv.writer(fw_csv)
            for line in file_csv_line:
                csv_writer.writerow(line)
        print(f"\nDane zapisane w pliku: {file}")
    else:
        print("\nNie zapisano zmian")
        exit()


def split_file_path(split_sys_argv):
    file_path = split_sys_argv[::-1].strip()
    if '\\' in file_path:
        file_name = file_path[:file_path.index('\\')]
        directory = file_path[file_path.index('\\') + 1:]
        file_name = file_name[::-1]
        path_directory = directory[::-1]
        # print("Test 1 file ", file_name)
        # print("Test 2 path", path_directory)
        if os.path.exists(path_directory):
            return file_name, path_directory
        else:
            return file_name, path_directory
    else:
        # file = split_sys_argv
        # path = os.getcwd()
        # print("Test 3 file ", file)
        # print("Test 4 path", path)
        return split_sys_argv,os.getcwd()


# ____________________________________________
# check_file(sys.argv[1])
# new_values(sys.argv[3:])
# print(file_csv_line)
# write_new_value_csv(sys.argv[2])
# _____________________________________________


file_read, directory_read = split_file_path(os.path.normpath(sys.argv[1]))
file_write, directory_write = split_file_path(os.path.normpath(sys.argv[2]))
if os.path.isdir(directory_read):
    check_file(file_read, directory_read)
    print(f"\nDane odczytane z pliku {directory_read}\{file_read}\n", file_csv_line)
    new_values(sys.argv[3:])
    print(f"\nDane do zapisania w pliku {directory_write}\{file_write}\n", file_csv_line)
    if os.path.isdir(directory_write):
        write_new_value_csv(sys.argv[2])
    else:
        print(f"Nie można zapisać. Brak katalogu: {directory_write}")
else:
    print(f"Brak katalogu: {directory_read}")