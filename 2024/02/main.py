# Part 1
print(sum(map(lambda xxs: (all(map(lambda xx: xx<0,xxs)) or all(map(lambda xx: xx>0,xxs))) and (all(map(lambda xx: abs(xx)>0 and abs(xx)<4,xxs))),map(lambda xs:list(map(lambda p:p[0]-p[1],zip((t:=list(map(int,xs)))[1:],t[:-1]))),map(lambda l:l.split(' '),map(str.strip,open(__import__('sys').argv[1]).readlines()))))))
# Part 2
print(sum(map(lambda xxs: any(map(lambda xxx: (all(map(lambda xx: xx<0,xxx)) or all(map(lambda xx: xx>0,xxx))) and (all(map(lambda xx: abs(xx)>0 and abs(xx)<4,xxx))), xxs)),map(lambda xs:[list(map(lambda p:p[0]-p[1],zip((t:=list(map(int,xs[:i]+xs[i+1:])))[1:],t[:-1]))) for i in range(len(xs))],map(lambda l:l.split(' '),map(str.strip,open(__import__('sys').argv[1]).readlines()))))))
