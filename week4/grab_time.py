# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours = dict()
time = ''
for line in handle:
    line = line.strip()
    words = line.split()
    if len(words) < 2 or words[0] != 'From' : continue
    for word in words:
        for i in word:
            if i == ':':
                first = word[0]
                second = word[1]
                time = first + second
                # print(time)
                hours[time] = hours.get(time, 0) + 1
                break
sort_time = sorted(hours.items())
for k, v in sort_time:
    print(k, v)
