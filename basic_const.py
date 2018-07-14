import tensorflow as tf

consts = []

## 상수값 텐서 ##

# 모든 원소의 값이 0인 지정한 모양의 텐서를 생성
# 모양, 타입, 명칭
zeros = tf.zeros([2, 4], dtype=tf.int32, name="zeros")
consts.append(zeros)

# 텐서의 모양과 동일한 텐서를 생성, 모든 원소값은 0
# 텐서, 타입, 명칭
zeros_like = tf.zeros_like(zeros, dtype=None, name="zeros_like")
consts.append(zeros_like)

# 모든 원소의 값이 1인 지정한 모양의 텐서를 생성
# 모양, 타입, 명칭
ones = tf.ones([2, 4], dtype=tf.int32, name="ones")
consts.append(ones)

# 텐서의 모양과 동일한 텐서를 생성, 모든 원소값은 1
# 텐서, 타입, 명칭
ones_like = tf.ones_like(ones, dtype=None, name="ones_like")
consts.append(ones_like)

# 스칼라값으로 채워진 텐서를 생성
# 모양, 스칼라값, 명칭
fill = tf.fill([2, 3], 7, name="fill")
consts.append(fill)

# 지정된 값의 상수 텐서를 생성
# 값, 타입, 모양, 명칭
con = tf.constant(10, dtype=tf.int32, shape=None, name="const")
consts.append(con)

with tf.Session() as s:
    for const in consts:
        print(s.run(const), end="\n\n")