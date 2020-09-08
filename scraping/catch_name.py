# Following Links in Python

# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

# We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html 
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
# Last name in sequence: Anayah
# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Fergal.html 
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: T
# Strategy
# The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.
import urllib.request
from bs4 import BeautifulSoup
import ssl
import re

def go_ahead(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    #retrieve all of the enchor tags
    tags = soup('a')
    i = 0
    for tag in tags:
        i += 1
        tg = tag.get('href', None)
        if i == 18:
            return tg

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
tg = url
i = 0
while i < 7:
    tg = go_ahead(tg)
    i += 1
result = ''
for i in re.findall('_by_(.*).html', tg):
    result = i
print(result)

# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
#retrieve all of the enchor tags
# tags = soup('a')
# i = 0

# for tag in tags:
#     i += 1
#     tg = tag.get('href', None)
#     if i == 3:
#         next_url = tg
#         html = urllib.request.urlopen(next_url, context=ctx).read()
#         soup = BeautifulSoup(html, 'html.parser')
#         next_tag = soup('a')
#         for t in next_tag:
            # print(t)
