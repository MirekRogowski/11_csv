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
    file_path = directory+ '\\'+ file
    # print("file_path", file_path)
    open_file(file_path) if os.path.isfile(file) else list_directory(file, directory)