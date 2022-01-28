from pigeon import trial_count
from lottery import play, is_fill

if __name__ == "__main__":
    print(f"Start!")
    for N in range(0, 100000):

        trial = trial_count(N)

        used_numbers = play(N, trial)
        # print(f"used_numbers={used_numbers}") # Nがでかくなると大変なことになる

        if N % 1000 == 0:
            print(f"N={N}")

        if not is_fill(used_numbers):
            print(f"N={N} Fail")
            break
