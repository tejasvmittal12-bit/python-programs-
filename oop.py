class robot:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
            return "{} sings {}".format(self.name, song)
        
    def dance(self):
            return "{} is now dancing".format(self.name)
        
eric = robot("eric", 10)

print(eric.sing("Happy"))
print(eric.dance())