# MLiS---RL-Project

Rules of Stylised Blackjack
• There is a single player_hand. The dealer is passive (just deals the cards).
• The game is played with a number D of decks of Poker cards (52 cards
per deck, 13 per suit ranging from 2-10 plus J/Q/K/A).
• Cards have a numerical value equal to their number for 2-10, figures
J/Q/K are all valued 10, and Aces are valued 11 unless the sum in the
hand goes over 21 and then they are valued 1. The suit is irrelevant.
• The D decks are shuffled randomly at the start of the game. The cards
are dealt one by one from this random shuffle.
• The game lasts until all the cards are used. This defines an episode of
the game (in RL terminology). NB the cards are not reshuffled between
hands.
• The aim of the game is to obtain the maximum accumulated score over
an episode, by adding up the score of each hand played, see Eq. (1)
below.
1
• A hand represents one cycle of the game through the following sequence
of steps:
1. A card is dealt. We call its numerical value C1.
2. At iteration n, the player_hand considers the total sum of the cards dealt
in the hand, C1 + · · · + Cn, and decides whether to “stick” thus
ending the hand and going to Step 4, or to “hit” to get another
card from the deck and continue with the hand.
3. A new card is dealt, we call its value Cn+1. The sum is updated to
C1 +· · ·+Cn+1. If the total is less than 21, the hand can continue
and we go back to Step 2 (recall the rule about Aces).
4. The hand is finished, either because the player_hand stuck at Step 2 or
because the total value of the cards is 21 or beyond. The resulting
score for the hand is
S =
(
(C1 + · · · + Cn+1)
2
if C1 + · · · + Cn+1 ≤ 21
0 if C1 + · · · + Cn+1 > 21 (1)
That is, the score is quadratic in the total if it does not exceed 21,
and zero otherwise.
5. NB there are no other moves such as splits or surrender as in real
Blackjack.
