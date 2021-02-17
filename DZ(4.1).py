inp = open ('input.txt')
fnp = open('output.txt', 'w')
read = inp.read().split()
a = list(map(int, read))[1:]
l = [0 for _ in range(-100, 101)]
for x in range(len(a)):
    num = a[x]
    l[num] += 1

new = []
s = ''
for m in range(-100, 101):
    if l[m]:
        s += ((str( m ))+ ' ') * l[m]
fnp.write(s)
