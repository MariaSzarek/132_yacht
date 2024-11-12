YACHT = lambda x: 50 if len(set(x))==1 else 0
ONES = lambda x: count_points(1, x)
TWOS = lambda x: count_points(2, x)
THREES = lambda x: count_points(3, x)
FOURS = lambda x: count_points(4, x)
FIVES = lambda x: count_points(5, x)
SIXES = lambda x: count_points(6, x)
FULL_HOUSE = None
FOUR_OF_A_KIND = lambda x: four_of_a_kind(x)
LITTLE_STRAIGHT = lambda x: 30 if x==[1, 2, 3, 4, 5] else 0
BIG_STRAIGHT = lambda x: 30 if x==[2, 3, 4, 5, 6] else 0
CHOICE = lambda x: sum(x)


def four_of_a_kind(throw):
    return sum([num for num in throw if throw.count(num) == 4])

def count_points(digit, throw):
    return digit * throw.count(digit)