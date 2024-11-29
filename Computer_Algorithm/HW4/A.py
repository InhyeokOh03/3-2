def calculate_min_cards(num_cards, target, initial_cards):
    initial_cards.sort()
    max_reachable = 0
    cards_needed = 0

    for card in initial_cards:
        while max_reachable + 1 < card and max_reachable < target:
            cards_needed += 1
            max_reachable += (max_reachable + 1)
        max_reachable += card
        if max_reachable >= target:
            return cards_needed

    while max_reachable < target:
        cards_needed += 1
        max_reachable += (max_reachable + 1)

    return cards_needed


if __name__ == "__main__":
    num_cards, target = map(int, input().split())
    initial_cards = list(map(int, input().split()))

    result = calculate_min_cards(num_cards, target, initial_cards)
    print(result)
