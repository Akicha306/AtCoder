# https://atcoder.jp/contests/code-thanks-festival-2017-open/tasks/code_thanks_festival_2017_c

N,K = map(int,input().split())

data = [list(map(int, input().split())) for _ in range(N)]

data.sort(key=lambda x: x[0],reverse=True)
