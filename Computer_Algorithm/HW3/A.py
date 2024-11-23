import sys

class SimpleDeque:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def popleft(self):
        if not self.items:
            raise IndexError("pop from an empty deque")
        return self.items.pop(0)

    def __len__(self):
        return len(self.items)

def apply_action(state, action):
    new_state = state[:]
    if action == "swap_R":
        new_state = new_state[1:] + [new_state[0]]
    elif action == "swap_L":
        new_state = [new_state[-1]] + new_state[:-1]
    elif action == "wake":
        for i in range(len(state) - 1, -1, -1):
            if new_state[i] == 0:
                new_state[i] = 1
                break
    elif action == "toggle":
        for i in range(len(state)):
            new_state[i] = 1 - new_state[i]
    return new_state

def apply_rest(state):
    new_state = state[:]
    new_state[0], new_state[-1] = 0, 0
    return new_state

def minimum_time_to_wake_all(initial_state):
    initial_state = list(map(int, initial_state.strip()))
    queue = SimpleDeque()
    queue.append((initial_state, 0, 3))  # 초기 상태, 시간, 남은 행동 카운트
    # visited = set()  
    # visited.add(tuple(initial_state))

    while queue:
        state, time, rest_countdown = queue.popleft()

        # 모든 학생이 깨어 있는 경우
        if all(s == 1 for s in state):
            return time

        # 휴식이 필요할 때 처리
        if rest_countdown == 0:
            new_state = apply_rest(state)
            # if tuple(new_state) not in visited:
            #     queue.append((new_state, time + 1, 3))
            #     visited.add(tuple(new_state))
            queue.append((new_state, time + 1, 3))
            continue

        for action in ["swap_R", "swap_L", "wake", "toggle"]:
            new_state = apply_action(state, action)
            queue.append((new_state, time + 1, rest_countdown - 1))
            # if tuple(new_state) not in visited:
            #     queue.append((new_state, time + 1, rest_countdown - 1))
            #     visited.add(tuple(new_state))

    return -1  

if __name__ == "__main__":
    initial_state = sys.stdin.readline()
    result = minimum_time_to_wake_all(initial_state)
    print(result)
