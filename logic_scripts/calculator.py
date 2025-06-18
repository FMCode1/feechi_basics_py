# A program that does basic addition, subtraction, multiplication and floor division operations
# using lambda functions

# Lambda functions for math operations
add = lambda a, b: a + b
sub = lambda c, d: c - d
mul = lambda e, f: e * f
div = lambda g, h: g // h

# the length of fee_str will be passed as an arg
fee_str = "five"
length = len(fee_str)

# the time is cast from a string to an integer
time = "3456"
t_int = int(time)

print(add("2", "2"))
print(sub(3, length))
print(mul(3, t_int))
print(div(3, 4.1))
