N=int(input())
s=list(map(int,input().split()))
if len(s) == N:
	print(min(s),max(s))
