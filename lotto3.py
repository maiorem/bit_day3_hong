import random

# 랜덤으로 섞어서 0번째부터 6 전까지 뽑기
balls = [ x for x in range(1, 46)]
random.shuffle(balls)
print(balls[0:6])