import random

# 乱数
rnd = random.SystemRandom()


def play(N, trial):
    used_numbers = [0] * N

    for _i in range(0, trial):
        ball_number = rnd.randrange(0, N)
        used_numbers[ball_number] += 1

    return used_numbers


def is_fill(used_numbers):
    for volume in used_numbers:
        if volume < 1:
            return False

    return True
