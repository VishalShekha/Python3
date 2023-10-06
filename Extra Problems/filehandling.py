# open the sample file used
file = open('test.txt')
  
# read the content of the file opened
content = file.readlines()
  
# read 10th line from the file
print("tenth line")
print(content[9])
  
# print first 3 lines of file
print("first three lines")
print(content[0:3])

# importing required package
import linecache
  
# extracting the 5th line
particular_line = linecache.getline('test.txt', 4)
  
# print the particular line
print(particular_line)

# lines to print
specified_lines = [0, 7, 11]
  
# loop over lines in a file
for pos, l_num in enumerate(content):
    # check if the line number is specified in the lines to read array
    if pos in specified_lines:
        # print the required line number
        print(l_num)