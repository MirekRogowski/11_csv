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