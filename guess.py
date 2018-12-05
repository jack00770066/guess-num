import random

r = random.randint(1, 100)
count = 0
print(r)
while True:
	count += 1
	g = input('猜猜數字是多少?')
	g = int(g)
	if g > r:
		print('比答案小')
	elif g < r:
		print('比答案大')
	elif g == r:
		print('終於猜對了!')
		break
		print('這是你猜的第', count, '次')
	print('這是你猜的第', count, '次')