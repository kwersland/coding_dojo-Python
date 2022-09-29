# august 2
cat1 = {
    'name': 'Spike',
    'age': 2,
    'hair_color': 'orange'
}

cat2 = {
    'name': 'Tiger',
    'age': 2,
    'hair_color': 'striped'
}

cat3 = {
    'name': 'Lucy',
    'age': 2,
    'hair_color': 'calico'
}
class Toy:
    def __init__(self, type, color, action):
        self.type = type
        self.color = color
        self.action = action


class Cat:
    all_cats = []
    def __init__(self, name, age, hair_color, toy):
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.cute = True
        self.toy = toy
        Cat.all_cats.append(self)

    @classmethod
    def print_all_cats(cls):
        for one_cat in cls.all_cats:
            print(f"Name: {one_cat.name} Age: {one_cat.age}")
    
    def meow(self):
        print(f"Meeeeeow my name is {self.name}")
        return self

    def play(self):
        print(f"{self.name} plays with a {self.toy.color}{self.toy.type} and it {self.toy.action}")

    def __repr__(self):
        return f"Cat Object Name: {self.name} Age:{self.age}"



toy1 = Toy("ball of yarn", "red", "rolls away and unravels")
toy2 = Toy("scratcher", "blue", "takes critical damage")
toy3 = Toy("laser pointer", "red", "jumps around the room")

cat1 = Cat("Spike", 2, "orange", toy1)
cat2 = Cat("Tiger", 3, "striped", toy2)
cat3 = Cat("Lucy", 2, "calico", toy3)

cat1.play()

cat2.play()

cat3.play()

print(Cat.all_cats)


