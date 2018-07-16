def solve(i, n, dp):
	if dp[i][n] != -1:
		return dp[i][n]
	if n == 0:
		return 1
	if i > n:
		return 0
	ans = 0
	for j in range(i, n+1):
		ans = ans + solve(j+1, n-j, dp)
	dp[i][n] = ans
	return ans

def answer(n):
	dp = [[-1 for i in range(210)] for j in range(210)]
	return solve(1, n, dp) - 1 # at least two steps

print(answer(3))