def is_possible(task_times, k, max_time):
    cores = [0] * k
    for task in sorted(task_times, reverse=True):
        cores[0] += task
        cores.sort()
        # print(cores)
        
        if cores[-1] > max_time: 
            return False
    return True

def calculate_max_remaining_time(n, k, T, task_times):
    left, right = max(task_times), sum(task_times)
    best_time = -1

    # mid 시간이 가능하다면, 그보다 큰 시간들도 모두 가능.
    # mid 시간이 불가능하다면, 그보다 작은 시간들도 모두 불가능.

    while left <= right:
        mid = (left + right) // 2
        if is_possible(task_times, k, mid):
            best_time = mid
            right = mid - 1
        else:
            left = mid + 1
    
    if best_time <= T:
        return T - best_time
    else:
        return -1

if __name__ == "__main__":
    n, k, T = map(int, input().strip().split())
    task_times = [int(input().strip()) for _ in range(n)]
    
    result = calculate_max_remaining_time(n, k, T, task_times)
    print(result)

# 5 2 13
# 4
# 7
# 1
# 2
# 8