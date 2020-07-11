x = [1,2,3,4,5,6,7,8,9,10,11]

pair = [(x[i], x[-i-1]) for i in range(0, int(len(x)/2))]
unpack = []
# unpack = [a,b for (a, b) in pair]

# for i in range(0, int(len(x)/2)):
# 	(a, b) = (x[i], x[-i-1])
# 	pair.append((a, b))

for a, b in pair:
	unpack.append(a)
	unpack.append(b)

# if len(x) % 2 == 1:
# 	j = int(len(x)/2)
# 	unpack.append(x[j])

print(unpack)