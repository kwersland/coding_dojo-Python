class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return(self)

    def enroll(self):
        if self.is_rewards_member == True:
            print("Already a Member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self
    
    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points = self.gold_card_points - amount
        else:
            print("Not enough points")
        return(self)

user1 = User("Samantha", "Wersland", "samwersland@gmail.com", 24)
user1.enroll().enroll().spend_points(50).display_info()


user2 = User("Karsten", "Wersland", "k.wersland25@gmail.com", 22)
user3 = User("Jackson", "Paulo", "jpaulo@yahoo.com", 19)


user2.enroll().spend_points(80).display_info()
user3.display_info().spend_points(40)
