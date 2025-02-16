"""
***TASK3 == Find the string pallandrom - comprehensive way
s = ['madam','malayalam','teacher']
    1. given value is pallandrom are not
    2. print only pallandrom value in a list
How many pallandrom in the list?
"""
pallandrom_words = []
s = ['madam','malayalam','teacher']
for i in s:
    if i == i[::-1]:
        print(f"{i} is a pallandrom")
        pallandrom_words.append(i)
    else:
        print(f"{i} is not a pallandrom")
print(f"Total words in the list are: {len(s)}")
print(f"Total pallandrom words in the list are: {len(pallandrom_words)}")