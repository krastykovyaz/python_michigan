# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
l = ''
for line in fh:
    l += line
lst = l.split()
new_lst = list()
lst.sort()
i = 0
while i < len(lst):
    try:
        while lst[i] == lst[i + 1]:
            i += 1
    except:
        new_lst.append(lst[i])
        break
    new_lst.append(lst[i])    
    i += 1
print(new_lst)
