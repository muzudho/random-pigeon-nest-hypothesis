import math

# 定数
a = 2 * math.pi * math.e # 理論値。ボールが１個見つからないぐらいのギリギリの精度
# a = (2 * math.pi * math.e) + 1 # 理論値要らなければ 1 でも足しとけば 遊びで使うのに十分な いい感じ（＾～＾）

def trial_count(N):
    return math.ceil(N * a)


