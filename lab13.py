# This is the parent class for all possible strategies
class Strategy():
    # The constructor initializes the strategy description
    def __init__(self, desc):
        self.__description = desc

    # This method is used to describe what a strategy does      
    def use(self):
        return 'uses a generic strategy'
    
    # This method the name of the strategy class
    def get_id(self):
        return self.__class__.__name__

    # This method is used to print a strategy and does not need to be
    # changed
    def __str__(self):
        return self.__description
    
    # This method is use to describe what will happen when two
    # strategies are played against each other. This returns one
    # of three values:
    # 
    # * Return -1 if other beats self
    # * Return 1 if self beats other
    # * Return 0 if it's a tie
    # 
    def fight(self, other):
        return 0


# We have completed the RockStrategy class for you. Its parent is the
# Strategy class. It overrides use() and fight() and uses its parent
# constructor, get_id(), and __str__() 
class RockStrategy(Strategy):
    def __init__(self):
        super().__init__('Playing the rock')
            
    def use(self):
        return 'Rock!!'
    
    def fight(self, other):
        if other.get_id() == 'RockStrategy':
            print('Tie')
            return 0
        elif other.get_id() == 'PaperStrategy':
            print('Paper wins over rock')
            return -1
        elif other.get_id() == 'ScissorsStrategy':
            print('Rock wins over scissors')
            return 1


# TODO: Now you will complete the Paper and Scissors Strategy classes below.
class PaperStrategy(Strategy):
    def __init__(self):
        super().__init__('Playing the paper')

    def use(self):
        return 'Paper!!'
    
    def fight(self, other):
        if other.get_id() == 'PaperStrategy':
            print('Tie')
            return 0
        elif other.get_id() == 'RockStrategy':
            print('Paper wins over rock')
            return 1
        elif other.get_id() == 'ScissorsStrategy':
            print('Scissor wins over paper')
            return -1


class ScissorsStrategy(Strategy):
    def __init__(self):
        super().__init__('Playing the scissors')

    def use(self):
        return 'Scissors!!'
    
    def fight(self, other):
        if other.get_id() == 'ScissorsStrategy':
            print('Tie')
            return 0
        elif other.get_id() == 'RockStrategy':
            print('Rock wins over scissors')
            return -1
        elif other.get_id() == 'PaperStrategy':
            print('Scissor wins over paper')
            return 1

# The following code tests your code. Do not change it.
rock_strategy = RockStrategy()
scissors_strategy = ScissorsStrategy()
paper_strategy = PaperStrategy()

assert(rock_strategy.fight(rock_strategy) == 0)
assert(scissors_strategy.fight(scissors_strategy) == 0)
assert(scissors_strategy.fight(scissors_strategy) == 0)
assert(rock_strategy.fight(scissors_strategy) == 1)
assert(rock_strategy.fight(paper_strategy) == -1)
assert(scissors_strategy.fight(paper_strategy) == 1)