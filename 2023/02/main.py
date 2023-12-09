# Part 1 - one expression
print(sum([i * (1-any([any([((p:=c.split(' '))[1]=='blue' and int(p[0])>14) or (p[1]=='red' and int(p[0])>12) or (p[1]=='green' and int(p[0])>13) for c in map(str.strip,s.split(','))]) for s in l.split(';')])) for i, l in enumerate(map(str.strip,map(lambda l: l.split(':')[1],open('input.txt').readlines())),1)]))

# Part 2 - one expression
print(sum(map(lambda l:max(map(lambda fs:int(fs[0].split(' ')[0]),filter(None,map(lambda s:[*filter(lambda sss:'red' in sss,map(str.strip,s.split(',')))],l.split(';')))))*max(map(lambda fs:int(fs[0].split(' ')[0]),filter(None,map(lambda s:[*filter(lambda sss:'green' in sss,map(str.strip,s.split(',')))],l.split(';')))))*max(map(lambda fs:int(fs[0].split(' ')[0]),filter(None,map(lambda s:[*filter(lambda sss:'blue' in sss,map(str.strip,s.split(',')))],l.split(';'))))),map(str.strip,map(lambda l: l.split(':')[1],open('input.txt').readlines())))))
