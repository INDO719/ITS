def define_power(n: int) -> int:
    pow = 1
    while 10**pow <= n:
        pow += 1
    return pow - 1

def solution(n:int) -> int:
    pow = define_power(n)
    lst_candidates = {
        int(((9 * i - 10) * 10 ** (i - 1) + 1)) // 9: i - 1
        for i in range(pow-1, pow + 4)
    }

    if n in lst_candidates:
        return str(10**lst_candidates[n] - 1)[-1]

    r_s = [c for c in lst_candidates.keys() if n < c][0]
    l_s = [c for c in lst_candidates.keys() if n > c][-1]
    rng_s = [l_s, r_s]

    pow_l = lst_candidates[rng_s[0]]
    pow_r = lst_candidates[rng_s[1]]

    rng_n = [10**pow_l, 10**pow_r]

    c = (n - rng_s[0] - 1) // pow_r - 1
    c = c if c >= 0 else 0

    right_b = rng_n[0] + c

    right_s = rng_s[0] + 1 + c * lst_candidates[rng_s[1]]

    x1 = right_b
    x2 = x1 + 4
    string = list("".join([str(x) for x in range(x1, x2 + 1)]))

    y = list(map(int, string))
    x = [x + right_s for x in range(len(y))]

    result = {x[i]: y[i] for i in range(len(x))}

    return result[n]

def main():
    n = 12312
    print(solution(n))

if __name__ == "__main__":
    main()
