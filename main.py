import datetime

from pigeon import trial_count
from lottery import play


def time_stamp():
    return datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')


if __name__ == "__main__":
    failure = 0
    print(f"{time_stamp()} Start!")
    N = 0
    while True:
        N += 1
        trial = trial_count(N)

        not_used_ball_num = play(N, trial)

        # 定期的な報告
        if N % 1000 == 0:
            if not_used_ball_num < 1:
                print(
                    f"{time_stamp()} N={N} ok (Failure count={failure} Success rate={(N-failure)/N})")
        # 失敗報告
        if 0 < not_used_ball_num:
            failure += 1
            print(
                f"{time_stamp()} N={N} Fail. I didn't take out the {not_used_ball_num} balls. (Failure count={failure} Success rate={(N-failure)/N})")
