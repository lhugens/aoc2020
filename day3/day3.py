pos = 0
c1, p1 = 0, 0
c2, p2 = 0, 0
c3, p3 = 0, 0
c4, p4 = 0, 0
c5, p5 = 0, 0

def ind(i):
    return i % 31

with open("input.txt") as f:
    for cnt, line in enumerate(f):
        if line[ind(p1)] == '#':
            c1 += 1
        if line[ind(p2)] == '#':
            c2 += 1
        if line[ind(p3)] == '#':
            c3 += 1
        if line[ind(p4)] == '#':
            c4 += 1
        if cnt % 2 == 0 :
            if line[ind(p5)] == '#':
                c5 += 1
            p5 += 1
        p1 += 1
        p2 += 3
        p3 += 5
        p4 += 7

print(c1, c2, c3, c4, c5)
print(c1*c2*c3*c4*c5)
