def solve(M, F):
	if F == 1:
		return M-1
	if F == 0:
		return -1
	temp = solve(F, M % F)
	if temp == -1:
		return -1
	return M // F + temp

def answer(M, F):
	M = int(M)
	F = int(F)
	if F > M:
		F, M = M, F
	ans = solve(M, F)
	if ans == -1:
		return "impossible"
	return str(ans)

print(answer("4", "7"))