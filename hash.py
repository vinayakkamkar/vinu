print('Hash for 181 is:',hash(181))
print('Hash for 181.23 is:',hash(181.23))
print('Hash for python is:',hash('python'))
class person:
    def __init__(self, age, name):
        self.age=age
        self.name=name
    def __eq__(self, other):
        return self.age==other.age and self.name==other.name
    def __hash__(self):
        print('The hash value of custome objects are;')
        return hash((self.age, self.name))
person = person(25, 'vinu')
print(hash(person))
