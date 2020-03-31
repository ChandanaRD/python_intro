#https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    marksList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksList.append([name, score])

    secondHighest = sorted(list(set(marks for name, marks in marksList)))[1]

    print('\n'.join(sorted([a for a,b in marksList if b == secondHighest])))

