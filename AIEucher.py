import random
from collections import deque, Counter

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['9', '10', 'J', 'Q', 'K', 'A']
POINTS_TO_WIN = 10

# Euchre deck setup
def create_deck():
    return [(rank, suit) for suit in SUITS for rank in RANKS]

def card_value(card, trump_suit):
    rank, suit = card
    if rank == 'J':
        if suit == trump_suit:
            return 30  # Right bower
        elif is_left_bower(card, trump_suit):
            return 29  # Left bower
    order = RANKS.index(rank)
    return order + (15 if suit == trump_suit else 0)

def is_left_bower(card, trump):
    rank, suit = card
    return rank == 'J' and suit_color(suit) == suit_color(trump) and suit != trump

def suit_color(suit):
    return 'red' if suit in ['Hearts', 'Diamonds'] else 'black'

def deal():
    deck = create_deck()
    random.shuffle(deck)
    return [deck[i:i+5] for i in range(0, 20, 5)], deck[20]

def print_hand(player_num, hand):
    print(f"\nPlayer {player_num}'s hand:")
    for i, card in enumerate(hand):
        print(f"{i + 1}: {card[0]} of {card[1]}")

def choose_trump(faceup, hands):
    trump = faceup[1]
    print(f"\nFace-up card: {faceup[0]} of {faceup[1]}")
    choice = input(f"Do you want to pick {faceup[1]} as trump? (y/n): ")
    if choice.lower() == 'y':
        return trump
    else:
        alt_suits = [s for s in SUITS if s != trump]
        trump = input(f"Choose a trump suit from {alt_suits}: ")
        return trump

def play_card(player, hand, lead_suit, trump):
    if player == 0:
        print_hand(1, hand)
        while True:
            try:
                choice = int(input("Choose a card to play (1-{}): ".format(len(hand)))) - 1
                if 0 <= choice < len(hand):
                    card = hand.pop(choice)
                    return card
            except ValueError:
                pass
            print("Invalid choice.")
    else:
        valid_cards = [card for card in hand if card[1] == lead_suit or is_left_bower(card, trump)]
        card = valid_cards[0] if valid_cards else hand[0]
        hand.remove(card)
        return card

def winner_of_trick(trick, trump):
    lead_suit = trick[0][1][1]
    values = [
        (i, card_value(card, trump))
        for i, card in trick
    ]
    return max(values, key=lambda x: x[1])[0]

def play_round(hands, trump):
    trick_order = deque([0, 1, 2, 3])
    scores = [0, 0]
    for _ in range(5):
        trick = []
        lead_card = play_card(trick_order[0], hands[trick_order[0]], None, trump)
        lead_suit = lead_card[1]
        trick.append((trick_order[0], lead_card))

        for i in list(trick_order)[1:]:
            trick.append((i, play_card(i, hands[i], lead_suit, trump)))

        winner = winner_of_trick(trick, trump)
        trick_order.rotate(-trick_order.index(winner))
        print("\nTrick result:")
        for p, c in trick:
            print(f"Player {p + 1}: {c[0]} of {c[1]}")
        print(f"Player {winner + 1} wins the trick!\n")
        if winner in [0, 2]:
            scores[0] += 1
        else:
            scores[1] += 1
    return scores

def main():
    team_scores = [0, 0]
    round_num = 1
    while max(team_scores) < POINTS_TO_WIN:
        print(f"\n--- Round {round_num} ---")
        hands, faceup = deal()
        trump = choose_trump(faceup, hands)
        print(f"Trump is {trump}\n")
        round_scores = play_round(hands, trump)
        print(f"Team 1 (Players 1 & 3) won {round_scores[0]} tricks.")
        print(f"Team 2 (Players 2 & 4) won {round_scores[1]} tricks.")
        if round_scores[0] > round_scores[1]:
            team_scores[0] += 1
        else:
            team_scores[1] += 1
        print(f"Score: Team 1 = {team_scores[0]}, Team 2 = {team_scores[1]}")
        round_num += 1
    print("\nGame over!")
    winner = "Team 1" if team_scores[0] >= POINTS_TO_WIN else "Team 2"
    print(f"{winner} wins the game!")

if __name__ == '__main__':
    main()
