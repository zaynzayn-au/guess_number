import random

r = random.randint(1,100)
r = str(r)

while True:
	number = input('请猜一下数字是多少吧：')
	if number == r:
		print('恭喜你猜对了！')
		break
	else:
		if number > r:
			print('不对哦，还要再小一点！')
		else:
			print('不对哦，还要再大一点哦')