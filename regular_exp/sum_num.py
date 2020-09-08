import re
name = input("Enter file:")
if len(name) < 1 : name = "test.txt"
handle = open(name)
total = 0
for line in handle:
    line = line.rstrip()
    numbers = re.findall('\d+', line)
    for number in numbers:
        if len(number) > 0:
            total += int(number)
print(total)
