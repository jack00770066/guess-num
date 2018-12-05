import random

r = random.randint(1, 100)
print(r)
while True:
	g = input('猜猜數字是多少?')
	g = int(g)
	if g > r:
		print('比答案小,再猜猜看')
	elif g < r:
		print('比答案大,再猜猜看')
	elif g == r:
		print('終於猜對了!')
		break