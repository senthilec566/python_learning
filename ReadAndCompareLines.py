import sys
import os


def main():
    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    src_list = []
    file = open(filepath, 'r')
    lines = file.readlines()[1:5]
    for index, line in enumerate(lines):
        src_list.append(line.strip())
    file.close()
    read_compare_lines(src_list)

def read_compare_lines(src_list):
    filepath = sys.argv[2]
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    line_number = 0
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            line = fp.readline()
            line_number += 1
            if src_list[0].lower() == line.strip().lower():
                print("match found for the first line : {} from the target file line number: {} and value: {}".format(
                    src_list[0], line_number, line.strip()))
                check_target_lines(fp, src_list)
    fp.close()

def check_target_lines(fp, src_list):
    lines_to_be_verified = int(sys.argv[3])
    count = 1;
    while count < lines_to_be_verified:
        line = fp.readline()
        if src_list[count].lower() == line.strip().lower():
            print("match found for the line : {} from the target file value: {}".format(src_list[count], line.strip()))
        else:
            print("the line {} is not found in the target. ".format(src_list[count]))
        count += 1

if __name__ == '__main__':
    main()
