class Cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Cricket - Player: {self.__player} | Score: {self.__score}")

    def play(self):
        print(f"{self.__player} hits a six!")

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score cannot be negative.")

class Football:
        def __init__(self, player, goals):
            self.__player = player
            self.__goals = goals

        def info(self):
            print(f"Football - Player: {self.__player} | Goals: {self.__goals}")

        def play(self):
            print(f"{self.__player} scores a goal!")

        def get_goals(self):
            return self.__goals

        def set_goals(self, new_goals):
            if new_goals >= 0:
                self.__goals = new_goals
                print(f"Goals updated to {self.__goals}")
            else:
                print("Goals cannot be negative.")  

cricket =  Cricket("Rohit", 85)
football = Football("Arjun", 2)

print("==== Sports Scoreboard ====")
for sport in (cricket, football):
        sport.info()
        sport.play()
        print()

print("---Direct Change Attempt---")
cricket.__score = 999
print(f"get_score() still shows {cricket.get_score()}")

print("\n--- Updating Scores ---")
cricket.set_score(100)
football.set_goals(3)