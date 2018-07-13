def count_char(text,char):
    count=0
    for c in text:
        if (c==char):
            count+=1
    return count

file = input("Enter file path: ")
with open(file) as f:
    text=f.read()

for char in "abcdefhijklmnopqrstuvwxyz123456789":
    percentage=100* count_char(text,char)/len(text)
    print("{0} = {1}%".format(char,round(percentage,4)))
