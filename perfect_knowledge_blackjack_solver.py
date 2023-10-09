import random

def deal_card(deck):
    card = deck.pop()
    return card

def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    
    for card in hand:
        if card in "23456789":
            value += int(card)
        elif card in "TJQK":
            value += 10
        elif card == "A":
            value += 1
            num_aces += 1

    # Adjust the value for aces
    while num_aces > 0 and value <= 11:
        value += 10
        num_aces -= 1
    
    return value

def simulate_blackjack(deck):
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    while calculate_hand_value(player_hand) < 12:
        player_hand.append(deal_card(deck))

    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if player_value > 21 or (dealer_value <= 21 and dealer_value >= player_value):
        return -1
    else:
        return 1

def blackjack_solver(deck, num_simulations):
    wins = 0
    losses = 0

    for _ in range(num_simulations):
        new_deck = deck[:]
        random.shuffle(new_deck)
        result = simulate_blackjack(new_deck)

        if result == 1:
            wins += 1
        else:
            losses += 1

    return wins - losses

# Example usage:
deck = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'] * 4  # Standard deck with four suits
num_simulations = 10000
score = blackjack_solver(deck, num_simulations)
print(f"Player's score after {num_simulations} simulations: {score}")
