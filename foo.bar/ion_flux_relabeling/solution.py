import math

# ref: https://www.daniweb.com/programming/software-development/code/406590/lowest-highest-bit-set-in-integer
def high_bit_order(n):
    """Return the integer k >= 0 such that 2**k <= n < 2**(k+1).
    This is also the order of the last bit set in the bitwise representation of n.
    Raise value error if n <= 0
        * for n == 0, no bit is set.
        * for n < 0, an infinite number of bits are set.
    For example
        high_bit_order(2368) --> 11
        n = 2368  bits: 000000101001000000000000000...
        n = -2368 bits: 000000110110111111111111111...
        n = 2**11 bits: 000000000001000000000000000...
    This function checks its return value and raise ValueError if an error
    is detected.
    """
    k = int(math.log(n, 2))
    if k:
        x = n >> (k-1)
        if x == 1: # correct log() imprecision for very large integers
            return k - 1
        elif 2 <= x < 4:
            return k
        else: # very unlikely, but handled
            raise ValueError("high_bit_order() failed on unusual value.")
    else:
        return k

def helper(h, e):
	if e < 0:
		raise ValueError("e should never be negative")
	if e == (1<<h) - 1:
		return -1
	if e == 1 or e == 2:
		return 3
	high = high_bit_order(e)
	if e == (1<<(high+1))-1:
		return 2*e+1
	if e == (1<<(high+1))-2:
		return e+1
	if high != h-1:
		return helper(h-1, e)
	return (1<<high) + helper(h, e-(1<<high)+1) - 1

def answer(h, q):
    return [helper(h, i) for i in q]

print answer(5, [19,14,28])