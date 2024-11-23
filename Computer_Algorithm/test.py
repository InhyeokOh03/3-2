import itertools

# 해시 함수 정의
def h(x, b):
    return (85 * x + b) % 13

# x의 범위 (우주)
universe = list(range(30))
b_values = list(range(13))

# 충돌 횟수 계산
collision_count = 0
total_pairs = 0

for b in b_values:
    for x, y in itertools.combinations(universe, 2):
        if h(x, b) == h(y, b):
            collision_count += 1
        total_pairs += 1

# 충돌 확률 계산
collision_probability = collision_count / (len(b_values) * total_pairs)

print(f"총 충돌 수: {collision_count}")
print(f"총 쌍의 수: {total_pairs}")
print(f"충돌 확률: {collision_probability}")
