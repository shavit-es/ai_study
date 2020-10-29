import re
file = input("Enter your file name :")
if len(file) < 1:
    file = "regex_sum_1004771.txt"
handle = open(file)
suml = list()
for line in handle:
    line = line.rstrip()
    y=re.findall('[0-9]+',line)
    if len(y)==0:continue
    suml.extend(y)
#print(suml)
intl = list()
for elements in suml:
    intl.append(int(elements))
#print(intl)
print(sum(intl))
