import tensorflow as tf

sequences = []

# start부터 stop 까지의 num개의 고르게 분포된 값들의 시퀀스 생성
# start, stop, num, 명칭
linspace = tf.linspace(1.0, 10.0, 25, name="linspace")
sequences.append(linspace)

# start부터 limit 미만까지 delta만큼 증가하여 정수 리스트 생성
# start, limit, delta, 명칭
rang = tf.range(2, 10, 1, name="range")
sequences.append(rang)

with tf.Session() as s:
    for sequence in sequences:
        print(s.run(sequence), end="\n\n")
