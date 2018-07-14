import tensorflow as tf

rands = []

# 정규분포로부터의 난수 값을 반환
# 모양, 정규분포평균값, 정규푼포표준편차, 타입, 시드, 명칭
random = tf.random_normal([3, 3], name="random")
rands.append(random)

# 절단정규분포로부터의 난수 값을 반환
# 모양, 절단정규분포평균값, 절단정규푼포표준편차, 타입, 시드, 명칭
truncated = tf.truncated_normal([3, 3], name="truncated")
rands.append(truncated)

# 균등분포로부터의 난수 값을 반환 (0 ~ 1)
# 모양, 타입, 시드1, 시드2, 명칭
uniform = tf.random_uniform([3, 3], name="uniform")
rands.append(uniform)

# 값의 첫 번째 차원을 기준으로 랜덤하게 섞기
# 섞기 위한 텐서, 시드1, 시드2, 명칭
shuffle = tf.random_shuffle(tf.range(1, 10), name="shuffle")
rands.append(shuffle)

# 텐서를 주어진 크기만큼 랜덤하게 잘라냄
# 자르기 위한 텐서, 잘라낼 크기, 시드, 명칭
crop = tf.random_crop(uniform, [2, 2], name="crop")
rands.append(crop)

# 다항분포로부터 샘플을 추출
# 비정규화 로그 확률, 샘플 갯수, 시드1, 시드2, 타입, 명칭
samples = tf.multinomial(tf.log([[0.5, 0.5]]), 10)
rands.append(samples)

# 그래프 수준의 난수 시드 설정
tf.set_random_seed(12523)

with tf.Session() as s:
    for rand in rands:
        print(s.run(rand), end="\n\n")
