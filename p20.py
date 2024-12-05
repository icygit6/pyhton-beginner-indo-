class animal:
    def __init__(self,animalname):
        print(animalname,'is an animal')
class mammal(animal):
    def __init__(self,mammalname):
        print(mammalname,'is a mammal')
        super().__init__(mammalname)
class cannotfly(mammal):
    def __init__(self,mammalthatcantfly):
        print(mammalthatcantfly,'cannot fly')
        super().__init__(mammalthatcantfly)
class cannotswim(mammal):
    def __init__(self,mammalthatcantswim):
        print(mammalthatcantswim,'cannot swim')
        super().__init__(mammalthatcantswim)
class cat (cannotswim,cannotfly):
    def __init__(self):
        print('i am a cat')
        super().__init__('cat')
cat()
bat = cannotswim('bat')

