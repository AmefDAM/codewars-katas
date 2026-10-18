def solve(s):
    errors = 0
    for index in range(len(s) // 2):
        if s[index] != s[-(index + 1)]:
            errors += 1
    if errors <= 1 and len(s) % 2 != 0:
        return True
    else:
        return errors == 1