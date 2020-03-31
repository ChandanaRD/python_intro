# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/designer-door-mat/problem?h_r=next-challenge&h_v=zen

r,c = input().split()
r = int(r)
c = int(c)
dash = '-'
line = '.|.'
half = int(r/2).__floor__()
for i in range (0,half):
    lineLen = len(line)
    oddNum = ((i)*2)+1
    lineHalf = int((c-(lineLen*oddNum))/2)
    print(dash*(lineHalf)+line*oddNum+dash*(lineHalf))

print(dash * int((c-7)/2) + "WELCOME" + dash * int((c-7)/2))

for i in range (half,0,-1):
    lineLen = len(line)
    oddNum = ((i-1)*2)+1
    lineHalf = int((c-(lineLen*oddNum))/2)
    print(dash*(lineHalf)+line*oddNum+dash*(lineHalf))

# -------------Using simple text Align methods------------------------
# n, m = map(int,input().split())
# pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1])) --> list concatenation since join takes single argument