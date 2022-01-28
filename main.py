import datetime

from pigeon import trial_count
from lottery import play, count_missing_ball


def time_stamp():
    return datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')


if __name__ == "__main__":
    failure = 0
    print(f"{time_stamp()} Start!")
    N = 0
    while True:
        N += 1
        trial = trial_count(N)

        used_numbers = play(N, trial)
        # print(f"used_numbers={used_numbers}") # Nがでかくなると大変なことになる

        missing_ball_num = count_missing_ball(used_numbers)

        # 定期的な報告
        if N % 1000 == 0:
            if missing_ball_num < 1:
                print(
                    f"{time_stamp()} N={N} ok (Failure count={failure} Success rate={(N-failure)/N})")
        # 失敗報告
        if 0 < missing_ball_num:
            failure += 1
            print(
                f"{time_stamp()} N={N} Fail. There are {missing_ball_num} missing balls. {missing_ball_num/N} %. (Failure count={failure} Success rate={(N-failure)/N})")
