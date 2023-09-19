# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category:int):
    if category in (1,2,3,4,5,6):
        return category*dice.count(category)
    if category == 7 and len(set(dice)) == 2 and (dice.count(dice[0]) == 3 or dice.count(dice[0]) == 2):
        return sum(dice)
    if category == 8 and len(set(dice)) <= 2:
        if dice.count(dice[0]) >= 4:
            return 4*dice[0]
        if dice.count(dice[1]) == 4:
            return 4*dice[1]
    if category == 0 and len(set(dice)) == 1:
        return 50
    if category == 9 and len(set(dice))==5 and 6 not in dice:
        return 30
    if category == 10 and len(set(dice))==5 and 1 not in dice:
        return 30
    if category == 11:
        return sum(dice)
    return 0