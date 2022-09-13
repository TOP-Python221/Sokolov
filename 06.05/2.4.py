counter = {}
for i in range(int(input())):
    line =input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1

min_count = min(counter.values())
most_ferquent = [k for k, v in counter.items() if v == min_count]
print(min(most_ferquent))