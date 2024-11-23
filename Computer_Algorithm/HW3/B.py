import sys
sys.setrecursionlimit(2000) 


def count_plans(days, bread):
    # Memoization
    memo = {}

    # Recursive
    def dfs(remaining_days, remaining_bread, prev_eaten):
        if remaining_days == 0:
            return 1 if remaining_bread >= 0 else 0

        if (remaining_days, remaining_bread, prev_eaten) in memo:
            return memo[(remaining_days, remaining_bread, prev_eaten)]

        plan_count = 0
        for today_eaten in range(10):
            if remaining_bread < 0:
                continue
                
            if remaining_bread < (remaining_days // 2):
                continue
                
            # 1
            if today_eaten > remaining_bread:
                break

            # 2
            if today_eaten == 0 and prev_eaten == 0:
                continue

            # 3
            if prev_eaten != -1 and abs(today_eaten - prev_eaten) > 1:
                continue

            plan_count += dfs(remaining_days - 1, remaining_bread - today_eaten, today_eaten)

        memo[(remaining_days, remaining_bread, prev_eaten)] = plan_count
        return plan_count

    return dfs(days, bread, -1)

if __name__ == "__main__":
    days, bread = map(int, input().split())
    result = count_plans(days, bread)
    print(result)
