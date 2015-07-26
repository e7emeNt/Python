# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print "Longest substring in alphabetical order is: beggh"

#In the case of ties, print the first substring.
#For example, if s = 'abcbcd', then your program should print "Longest substring in alphabetical order is: abc"


from itertools import count

s = "azcbobobegghakl"

maxSubstr = s[0:0]
for start in range(len(s)):
    for end in count(start + len(maxSubstr) + 1):
        substr = s[start:end]
        if len(substr) != (end - start):
            break
        if sorted(substr) == list(substr):
            maxSubstr = substr

print "Longest substring in alphabetical order is: " + str(maxSubstr)







# second way:

count = 1
result = s[0]
while s:
    newcount = 1
    newresult = ''
    i = 0
    while i + 1 < len(s):
        if ord(s[i]) <= ord(s[i + 1]):
            newresult += s[i + 1]
            newcount += 1
        else:
            break
        i += 1
    if newcount > count:
        count = newcount
        result = s[0] + newresult
    s = s[i + 1:]
print result