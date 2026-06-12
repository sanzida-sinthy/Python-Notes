# The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 2 = 0010

print(6 & 3)

# The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 7 = 0111

print(6 | 3)


# The ^ operator compares each bit and set it to 1 if only one is 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 5 = 0101

print(6 ^ 3)
