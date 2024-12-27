def generate_pd(n):
    if n % 2 == 1 or n == 0:
        return []

    ans = []
    backtrack(ans, n)
    return ans

def backtrack(ans, n, curr_balanced = '', num_left = 0, num_right = 0):
    if len(curr_balanced) == n:
        ans.append(curr_balanced)
        return

    if num_left < n // 2:
        backtrack(ans, n, curr_balanced + "p", num_left + 1, num_right)
    if num_right < num_left:
        backtrack(ans, n, curr_balanced + "d", num_left, num_right + 1)


def main():
    n = int(input())

    print(generate_pd(n))

if __name__ == "__main__":
    main()
