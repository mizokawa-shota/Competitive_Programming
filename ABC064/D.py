N = int(input())
S = input()

output = ''

hiraki = 0
toji = 0
for i in S:
    if i == '(':
        if toji > 0:
            output = '(' * toji + output
            output += ')' * toji
            toji = 0
            hiraki += 1
            output += i
        else:
            hiraki += 1
            output += i
    else:
        if hiraki > 0:
            hiraki -= 1
            output += i
        else:
            toji += 1

for i in range(hiraki):
    output += ')'

for i in range(toji):
    output += ')'

output = '(' * toji + output

print(output)
