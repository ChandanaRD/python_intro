# # https://www.hackerrank.com/challenges/alphabet-rangoli/problem?h_r=next-challenge&h_v=zen
#
# def print_rangoli(size):
#     # your code goes here
#     alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
#                 'n','o','p','r','s','t','u','v','w','x','y','z']
#     top = []
#     middle = []
#     left = ""
#     for j in range (size-1,0,-1):
#         left = alphabets[j]
#         for i in range (j+1,size):
#             left = alphabets[i]+'-'+left+'-'+alphabets[i]
#         top.append(left.center(size*4 -3, '-'))
#     left = ''
#     for i in range (size-1,-1,-1):
#             left+=alphabets[i]+'-'
#     middle = [left[:len(left)-3]+left[::-1]]
#
#     print("\n".join(top+middle+top[::-1]))
#
# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)

import string
alpha = string.ascii_lowercase

def print_rangoli(n):
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)