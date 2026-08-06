# ================================
# MY PET CARE DASHBOARD
# ================================

# Parent Class
class Pet:
    def __init__(self, name, health):
        self.name = name
        self.__health = health   # Private attribute

    def show_info(self):
        print(f"Pet Name: {self.name}")
        print(f"Health Level: {self.__health}")

    def care_action(self):
        print(f"{self.name} needs general care.")

    # Setter Method
    def set_health(self, new_health):
        if new_health >= 0 and new_health <= 100:
            self.__health = new_health
            print(f"{self.name}'s health updated to {self.__health}.")
        else:
            print("Health must be between 0 and 100.")


# Child Class 1
class Dog(Pet):
    def care_action(self):   # Method Overriding
        print(f"{self.name} needs a walk and some playtime.")


# Child Class 2
class Cat(Pet):
    def care_action(self):   # Method Overriding
        print(f"{self.name} needs grooming and quiet rest.")


# Child Class 3
class Rabbit(Pet):
    def care_action(self):   # Method Overriding
        print(f"{self.name} needs fresh carrots and a clean cage.")


# Creating Objects
dog = Dog("Buddy", 85)
cat = Cat("Misty", 75)
rabbit = Rabbit("Snowy", 65)


# Polymorphism with a Loop
pets = [dog, cat, rabbit]

print("===== My Pet Care Dashboard =====")

for pet in pets:
    pet.show_info()
    pet.care_action()
    print()


# Using Setter Methods
print("===== Updating Pet Health =====")

dog.set_health(90)
cat.set_health(80)
rabbit.set_health(70)

print("===== Final Pet Care Summary =====")

for pet in pets:
    pet.show_info()
print()