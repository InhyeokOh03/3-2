def count_plans(days, bread):
    queue = [(days, bread, -1)]  # (남은 날, 남은 붕어빵, 전날 먹은 양)
    plan_count = 0 

    while queue:
        # print(queue)
        remaining_days, remaining_bread, prev_eaten = queue.pop(0)

        if remaining_days == 0 and remaining_bread >= 0:
            plan_count += 1
            continue

        for today_eaten in range(10):
            # 조건 1
            if today_eaten > remaining_bread:
                break

            # 조건 2
            if today_eaten == 0 and prev_eaten == 0:
                continue

            # 조건 3
            if prev_eaten != -1 and abs(today_eaten - prev_eaten) > 1:
                continue

            queue.append((remaining_days - 1, remaining_bread - today_eaten, today_eaten))

    return plan_count

if __name__ == "__main__":
    days, bread = map(int, input().split())
    result = count_plans(days, bread)
    print(result) 