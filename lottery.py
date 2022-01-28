import random

# 乱数
rnd = random.SystemRandom()


def play(N, trial):
    used_numbers = [0] * N

    for _i in range(0, trial):
        ball_number = rnd.randrange(0, N)
        if ball_number == N:
            raise ValueError("0<=i<N だと思った（＾～＾）")

        used_numbers[ball_number] += 1

    return used_numbers


# def is_fill(used_numbers):
#    for volume in used_numbers:
#        if volume < 1:
#            return False
#
#    return True


def count_missing_ball(used_numbers):
    """0個だったボール（数）の数"""
    zero = 0
    for volume in used_numbers:
        if volume < 1:
            zero += 1

    return zero
