# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
spl_txt = list()
count = dict()
for line in handle:
	line.rstrip()
	spl_txt = line.split()
	if len(spl_txt) < 1 or spl_txt[0] != 'From':
		continue
	for mail in spl_txt:
		for i in mail:
			if i == '@':
				count[mail] = count.get(mail, 0) + 1
email = list()
amount = 0
for keys in count:
	if amount < count[keys]:
		amount = count[keys]
		email = keys
print(email, amount) 	
