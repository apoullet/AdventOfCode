# part 1
print(sum(map(lambda p:abs(p[0]-p[1]),zip(sorted(map(lambda ll:int(ll[0]),p_input:=list(map(lambda l:l.split('  '),map(str.strip,open(__import__('sys').argv[1]).readlines()))))),sorted(map(lambda lr:int(lr[1]),p_input))))))
# part 2
print(sum(map(lambda x:int(x)*list(map(lambda lr:int(lr[1]),p_input)).count(x),map(lambda ll:int(ll[0]),p_input:=list(map(lambda l:l.split('  '),map(str.strip,open(__import__('sys').argv[1]).readlines())))))))
