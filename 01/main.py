# Part 1 - one expression
print(sum([*map(int,[*map(lambda n:''.join([n[0],n[-1]]),[*map(lambda w:[*filter(str.isnumeric,w)],[*map(str.strip,open('input.txt').readlines())])])])]))

# Part 2 - one expression
print(sum([*map(int,[*map(lambda n:''.join([n[0],n[-1]]),[*map(lambda w:[*filter(str.isnumeric,w)],[''.join(['1'+w[i] if w[i:i+3]=='one'else'2'+w[i] if w[i:i+3]=='two'else'3'+w[i] if w[i:i+5]=='three'else'4'+w[i] if w[i:i+4]=='four'else'5'+w[i] if w[i:i+4]=='five'else'6'+w[i] if w[i:i+3]=='six'else'7'+w[i] if w[i:i+5]=='seven'else'8'+w[i] if w[i:i+5]=='eight'else'9'+w[i] if w[i:i+4]=='nine' else w[i] for i in range(len(w))]) for w in [*map(str.strip,open('input.txt').readlines())]])])])]))
