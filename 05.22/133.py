larger = list(input().split())
smaller = list(input().split())

larger_1 = ' '.join(map(str,larger))
smaller_1 = ' '.join(map(str,smaller))
print(f'\n{bool(larger_1.find(smaller_1) + 1)}')


#56 99 78 33 4896 238 74

#здесь пустой список
#True

# 22 56 17 69 31
# 69 31
# True

# 12 23 45 56
# 12 45

# False