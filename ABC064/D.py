N = int(input())
S = input()

output = ''

hiraki = 0
for i in S:
    if i == '(':
        hiraki += 1
        output += i
    else:
        if hiraki > 0:
            hiraki -= 1
            output += i
        else:
            output = '(' + output
            output += i

output += ')' * hiraki

print(output)
