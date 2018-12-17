#Sign sequence
def signSequence(n,m):
    k ='AAA'
    l = 'BBB'
    a = []
    for i in range(n):
        if i % 2 !=0:
            a.append([(l + k)*m])
        else:
            a.append([(k + l) * m])
    for row in a:
        print(' '.join(row))
signSequence(int(input('input n: ')),int(input('input m: ')))
