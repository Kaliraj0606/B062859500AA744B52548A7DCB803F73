class Player:
    def __init__(self, name, age, country, batting_style, bowling_style):
        self.name = name
        self.age = age
        self.country = country
        self.batting_style = batting_style
        self.bowling_style = bowling_style

    def display_player_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Country: {self.country}")
        print(f"Batting Style: {self.batting_style}")
        print(f"Bowling Style: {self.bowling_style}")



if __name__ == "__main__":
  
    player1 = Player("Virat Kohli", 33, "India", "Right-handed", "Right-arm medium")

    player1.display_player_info()
