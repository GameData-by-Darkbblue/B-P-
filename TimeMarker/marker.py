# 功能：提供每个分段视频的时长，给出将其合并后的完整视频中各视频开头的时间点

# struct
# [hour, minute, second]

input_time = [
	[0, 4, 43],
	[0, 13, 48],
	[0, 3, 1],
	[0, 2, 16],
	[0, 8, 33],
	[0, 5, 50],
	[0, 7, 50],
	[0, 5, 53],
	[0, 5, 35],
	[0, 7, 42],
	[0, 9, 20],
	[0, 7, 53]
]

current = [0, 0, 0]
for t in input_time:
	print(''.join([':'+str(t) if len(str(t)) == 2 else ':0'+str(t) for t in current])[1:])
	carry = 0
	for i in range(2, -1, -1):
		total = carry + current[i] + t[i]
		current[i] = total % 60
		carry = int(total / 60)
