import sys
import csv
import random


def read(data):
    dic = {}
    with open(data) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Colum names ar {",".join(row)}')
                line_count += 1
            else:
                print(row)
                line_count += 1
    print(f'Processed { line_count } lines')









def main():
    dic = read('Test.csv')   


if __name__ == "__main__":
    main()