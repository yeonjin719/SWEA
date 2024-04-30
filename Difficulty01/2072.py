t = int(input())

def solution(_list):
    ans = 0
    for i in _list:
        if i%2 != 0:
            ans += i
    return ans


for i in range(t):
    nums = list(map(int, input().split(' ')))
    print("#"+str(i+1), end=' ')
    print(solution(nums))
