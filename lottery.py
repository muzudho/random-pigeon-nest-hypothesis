from random import seed, randrange

# 乱数の種
seed() 


def play(N, trial):
    not_used_balls = [True] * N
    not_used_ball_num = N

    for _i in range(0, trial):
        ball_number = randrange(0, N)
        if ball_number == N:
            raise ValueError("0<=i<N だと思った（＾～＾）")

        if not_used_balls[ball_number]:
            not_used_ball_num -= 1
            not_used_balls[ball_number] = False

        if not_used_ball_num == 0:
            break  # 全てのボールを引いたので終わります

    return not_used_ball_num
