"""CS 61A Presents The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS>0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return the
    number of 1's rolled."""
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    total = 0
    sums = 0
    while num_rolls>0:
        k = dice()
        if k == 1:
            total += 1
        else:
            sums += k
        num_rolls -= 1
    if total > 0:
        return total
    else:
        return sums

def free_bacon(opponent_score):
    """Return the points scored from rolling 0 dice (Free Bacon)."""
    return 1 + max(opponent_score // 10, opponent_score % 10)

def is_prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(2, x):
        if (x % i) == 0:
            return False
    return True

def next_prime(x):
    k = x + 1
    while not is_prime(k):
        k+=1
    return k

def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player. Also
    implements the Hogtimus Prime and When Pigs Fly rules."""
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    if num_rolls==0:
        score = free_bacon(opponent_score)  #Free Bacon
    else:
        score = roll_dice(num_rolls, dice)

    if is_prime(score):                     #Hogtimus Prime rule
        score = next_prime(score)
    
    if score > (25 - num_rolls):                  #When Pigs Fly rule
        score = (25 - num_rolls)

    return score

def reroll(dice=six_sided):
    """Return dice that return even outcomes and re-roll odd outcomes of DICE."""
    def rerolled():
        k = dice()
        if k % 2 == 0:
            return k
        else:
            return dice()
    return rerolled

def select_dice(score, opponent_score, dice_swapped):
    """Return the dice used for a turn, which may be re-rolled (Hog Wild) and/or
    swapped for four-sided dice (Pork Chop).DICE_SWAPPED is True if and only if
    four-sided dice are being used."""
    if dice_swapped == True:
        dice = four_sided                   #Pork Chop
    else:
        dice = six_sided
    if (score + opponent_score) % 7 == 0:   #Hog Wild
        dice = reroll(dice)
    return dice

def other(player):
    """Return the other player, for a player PLAYER numbered 0 or 1."""
    return 1 - player

def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players"""
    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    dice_swapped = False  # Whether 4-sided dice have been swapped for 6-sided
    num_rolls = 0
    dice = 0
    while score0 < goal and score1 < goal:
        if player == 0:
            num_rolls = strategy0(score0, score1)
            if num_rolls == -1:
                dice_swapped = not dice_swapped
                dice = select_dice(score0, score1, dice_swapped)
                score0 += 1
            else:
                dice = select_dice(score0, score1, dice_swapped)
                score0 += take_turn(num_rolls, score1, dice)                
        else:
            num_rolls = strategy1(score1, score0)
            if num_rolls == -1:
                dice_swapped = not dice_swapped
                dice = select_dice(score1, score0, dice_swapped)
                score1 += 1
            else:
                dice = select_dice(score1, score0, dice_swapped)
                score1 += take_turn(num_rolls, score0, dice)
        if (2*score0 == score1) or (2*score1 == score0):
            temp = score0
            score0 = score1
            score1 = temp
        player = other(player)
    return score0, score1



#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice."""
    def strategy(score, opponent_score):
        return n
    return strategy

def check_strategy_roll(score, opponent_score, num_rolls):
    """Raises an error with a helpful message if NUM_ROLLS is an invalid
    strategy output. All strategy outputs must be integers from -1 to 10."""
    msg = 'strategy({}, {}) returned {}'.format(
        score, opponent_score, num_rolls)
    assert type(num_rolls) == int, msg + ' (not an integer)'
    assert -1 <= num_rolls <= 10, msg + ' (invalid number of rolls)'

def check_strategy(strategy, goal=GOAL_SCORE):
    """Checks the strategy with all valid inputs and verifies that the
    strategy returns a valid input. Use `check_strategy_roll` to raise
    an error with a helpful message if the strategy returns an invalid
    output."""
    score0 = 0
    num_rolls = 0
    while score0 < goal:
        score1 = 0
        while score1 < goal:
            num_rolls = strategy(score0, score1)
            if (num_rolls < 11) & (num_rolls > 0):
                score1 += 1
            else:
                return check_strategy_roll(score0, score1, num_rolls)
        score0 += 1
    return None

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called."""
    def sum_fn(*args):
        total = 0
        for i in range(num_samples):
            total += fn(*args)
        return total/num_samples
    return sum_fn

def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes."""
    k = 1
    max_average, num_rolls = 0, 0
    while k<=10:
        if max_average < make_averaged(roll_dice, num_samples)(k, dice):
            num_rolls = k
            max_average = make_averaged(roll_dice, num_samples)(k, dice)
        k += 1
    return num_rolls

def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1

def average_win_rate(strategy, baseline=always_roll(4)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1."""
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2

def run_experiments():
    """Run a series of strategy experiments and report results."""
    if False:
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        rerolled_max = max_scoring_num_rolls(reroll(six_sided))
        print('Max scoring num rolls for re-rolled dice:', rerolled_max)

    if True:
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if True:
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if True:
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    "*** You may add additional experiments as you wish ***"

def bacon_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise."""
    if take_turn(0, opponent_score) >= margin:
        return 0
    else:
        return num_rolls
check_strategy(bacon_strategy)

def swap_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points. Otherwise, it rolls
    NUM_ROLLS."""
    if opponent_score == 2 * (score + free_bacon(opponent_score)):
        return 0
    elif take_turn(0, opponent_score) >= margin:
        return bacon_strategy(score, opponent_score, margin, num_rolls)
    else:
        return num_rolls
check_strategy(swap_strategy)

def final_strategy(score, opponent_score):
    """Switch the dice to mess with the computer's strategy so that it
    does not return the highest possible score. Switch the strategy to
    make it optimal for you to score."""
    if score == 0:
        return -1
    else:
        return swap_strategy(score, opponent_score, margin=5, num_rolls=3)
    check_strategy(final_strategy)

##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions. This
    function uses Python syntax/techniques not yet covered in this course."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()