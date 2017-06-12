N = int(input())
S = input()

output = ''

hiraki = 0
toji = 0
for i in S:
    if i == '(':
        if toji > 0:
            output = '(' * toji + output
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
            output += i

output += ')' * hiraki
output = '(' * toji + output

print(output)
