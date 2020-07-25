import numpy as np 
import matplotlib.pyplot as plt
import random
import DP_agent as dpa

def generate_decks(num_decks): #function to initialise D decks and shuffle
    cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #initialise cards
    full_deck = [] #initialise deck
    game_deck = [] #initialise game deck

    #create full deck, 4 sets of cards (suit irrelevant)    
    for i in range(4):
        full_deck.extend(cards)
    
    for i in range(num_decks):
        game_deck.extend(full_deck)
    
    #shuffle game deck
    random.shuffle(game_deck)
    return game_deck

#functions to calculate the value of a hand
#ace value code adapted from 
#https://towardsdatascience.com/lets-play-blackjack-with-python-913ec66c732f
def possible_ace_values(num_aces):
    if num_aces == 1:
        ace_values = [1, 11]
    else:
        ace_values = [num_aces, 11 + (num_aces - 1)]
    return ace_values

def hand_score(hand):
    score = 0
    aces_present = 0

    for card in hand:
        if card != 'A':
            score += card
        else:
            aces_present += 1

    #return score based on whether or not aces are present in hand 
    if aces_present == 0:
        return score
    else:
        ace_values = possible_ace_values(aces_present)
        total_score = [i + score for i in ace_values if i + score <= 21]

        if total_score == []:
            return min(ace_values) + score
        else:
            return max(total_score)

def blackjack_game_loop(num_D_decks, policy, state_space, max_iterations = 1000):
    dealer = generate_decks(num_D_decks)
    player_hand = []
    final_score = 0
    round_scores = []
    round_flag = False
    i = 0
    state_space_list = list(state_space)
    #while i != max_iterations:
    while len(dealer) != 0:
        #initialise round
            round_flag = not round_flag
            i += 1
            #deal 2 cards at the start of a round
            player_hand.append(dealer.pop(0))
            player_hand.append(dealer.pop(0))

            while round_flag == True:
                print(player_hand)
                #determine what state agent is currently in according to hand value
                current_state = hand_score(player_hand)
                #find the index of state using the hand value
                state_index = state_space_list.index(current_state)
                #determine which action in current state according to the policy
                action = np.argmax(policy[state_index]) #0: Hit; 1: Stick 
                print(current_state)
                #action = input('would you like to hit or stick?\n')
                if action == 1: #finish the hand and tabulate the score
                    print('stick')
                    round_score = hand_score(player_hand)
                    final_score += np.power(round_score, 2)
                    round_scores.append(round_score)
                    player_hand = []
                    round_flag = not round_flag
                elif action == 0: #continue the hand
                    print('hit')
                    player_hand.append(dealer.pop(0))
                    score_check = hand_score(player_hand)
                    if score_check > 21: #if hit causes you to go bust, end the round
                        print(player_hand)
                        print(score_check)
                        print('you went bust')
                        final_score = final_score
                        round_scores.append(0)
                        player_hand = []
                        round_flag = not round_flag
    print(final_score)
    return final_score, round_scores

def main():
    state_space, rewards, policy, transition_probs = dpa.generate_blackjack_environment()
    V_star, pi_star = dpa.value_iteration(policy, state_space, rewards, transition_probs)
    final_score, round_scores = blackjack_game_loop(1, pi_star, state_space, 1000)
    #plot score obtained each round
    rounds = range(len(round_scores))
    plt.figure(figsize=(20,15))
    plt.plot(rounds, round_scores)
    plt.xlabel('Round')
    plt.ylabel('Scores')
    plt.title('Score agent achieves every round according to policy')
    plt.show()
    
    print('optimal values:')
    print(V_star)
    print('optimal policy:')
    print(pi_star)

if __name__ == '__main__':
    main()