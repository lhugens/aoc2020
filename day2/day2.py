count = 0

with open("input.txt") as f:
    for cnt, line in enumerate(f):
        arr = line.split()

        passwd = arr[-1]
        letter = arr[1][0]
        mini, maxi = arr[0].split('-')

        if int(mini) <= passwd.count(letter) <= int(maxi):
            count +=1

print(count)

count = 0

def xor(a, b):
    if a == True and b == False:
        return True
    elif b == True and a == False:
        return True
    else:
        return False

with open("input.txt") as f:
    for cnt, line in enumerate(f):
        arr = line.split()

        passwd = arr[-1]
        letter = arr[1][0]
        i, j = arr[0].split('-')
        i, j = int(i)-1, int(j)-1

        if xor(passwd[i] == letter, passwd[j] == letter):
            count +=1

print(count)

