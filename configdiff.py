

import difflib
import os
import csv
import time
# change this if you dont want the terminal to clear before running.
# I just like starting from a blank slate
os.system('clear')


# since you're forgetful, add this note to each script tellling what it does bruh
print("        ******                --> USAGE  NOTE <--                     ******\n"
      "        *  This script will take (as input) 2 config files and perform a   *\n"
      "        *                   diff, and export to a csv.                     *\n"
      "        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * **\n")

time.sleep(2)

# read file and return in lines
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

# Function to compare two files and generate a side-by-side difference
def compare_files(file1_path, file2_path):
    file1_lines = read_file(file1_path)
    file2_lines = read_file(file2_path)

    differ = difflib.Differ()
    diff = list(differ.compare(file1_lines, file2_lines))

    return diff

def export_diff_to_csv(diff, csv_file_path):
    with open(csv_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Line Number', 'File 1', 'File 2'])
        
        for line_number, line in enumerate(diff, 1):
            if line.startswith(' '):
                continue
            elif line.startswith('- '):
                csv_writer.writerow([line_number, line[2:], ''])
            elif line.startswith('+ '):
                csv_writer.writerow([line_number, '', line[2:]])
                
def main():
    while True:
        file1_path = input("Enter the name of the first file for compare:  ")  # first log file
        file2_path = input("Enter the name of the second file for compare:  ")  #  second log file
        csv_file_path = input("Enter the name of the output file: ") #diff output file to csv
        diff = compare_files(file1_path, file2_path)
        
        export_diff_to_csv(diff, csv_file_path)

        print(f'Your config diff file has been saved as {csv_file_path}.')
        print()
        another = input("Do you want to run another diff?")
        if another != 'yes':
            break
    

if __name__ == "__main__":
    main()        