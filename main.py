import datetime

from pigeon import trial_count
from lottery import play, is_fill


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

        has_failed = not is_fill(used_numbers)

        # 定期的な報告
        if N % 1000 == 0:
            if not has_failed:
                print(
                    f"{time_stamp()} N={N} ok (Failure count={failure} Success rate={(N-failure)/N})")
        # 失敗報告
        if has_failed:
            failure += 1
            print(
                f"{time_stamp()} N={N} Fail (Failure count={failure} Success rate={(N-failure)/N})")
