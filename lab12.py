# part a
class Dog():
    """The Dog has a name, weight, and breed. It can eat or exercise."""
     
    # Constructor as given in slides
    def __init__(self, name, weight, breed):
        self.name = name
        self.weight = weight
        self.breed = breed

    # Method for the dog to eat given in slides
    # Notice that the weight of the dog increases
    # by the amount fed    
    def eat(self, amount):
        self.weight += amount


    # Write a method called exercise
    # that takes an amount and decreases the
    # dog's weight by that amount
    # TODO: ADD METHOD EXERCISE BELOW
    def exercise(self, amount):
        self.weight -= amount

toto = Dog('Toto', 13, 'Cairn Terrier')

assert(toto.name == 'Toto')
assert(toto.weight == 13)
assert(toto.breed == 'Cairn Terrier')

# part b 
class Person(object):
    """The Person has a name, a Dog, and a generosity. It can feed its Dog."""

    # TODO: Complete the constructor the the Person below
    # Be sure to save each input parameter except
    # self as an attribute
    def __init__(self, name, dog, generosity):
        self.name = name
        self.dog = dog
        self.generosity = generosity

    # TODO: Complete the following feed_dog method
    # The amount of food that people
    # feed their dogs are their generosity 
    def feed_dog(self):
        self.dog.eat(self.generosity)

    # Create a Person object with name Gregory
# Gregory owns a Border Terrier named Hickory, whose weight is 15.2 pounds.
# Gregory's generosity is 0.1.
#
#  - The dog parameter for creating the Person object for Gregory
#    will be the Dog object that is created for Hickory.
#
#  - The generosity is a floating point number such that 0 ≤ generosity ≤ 1
#

# TODO: Instantiate the owner and dog objects!
dog = Dog('Hickory', 15.2, 'Border Terrier')
owner = Person('Gregory', dog, 0.1)

print(owner.name + ' owns a ' + owner.dog.breed + ' named ' + owner.dog.name)
print(owner.dog.name + ' weighs ' + format(owner.dog.weight, 'f') + ' lbs.')
# Should be 'Gregory owns a Border Terrier named Hickory'
#           'Hickory weighs 15.200000 lbs.'

# Gregory feeds Hickory.
# TODO: Make Gregory feed Hickory.
owner.feed_dog()

print('After eating ' + owner.dog.name + ' weighs ' \
      + format(owner.dog.weight,'f') + ' lbs.')
# Should be 'After eating Hickory weighs 15.300000 lbs.'

assert(owner.name == 'Gregory')
assert(owner.generosity == 0.1)
assert(owner.dog == dog)
assert(dog.name == 'Hickory')
assert(dog.breed == 'Border Terrier')
assert(round(dog.weight, 2) == 15.3)