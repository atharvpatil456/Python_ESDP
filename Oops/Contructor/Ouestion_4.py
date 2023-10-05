class Team:
    def __init__(self, country_name, player_name, matches, age, batting_avg, bowling_avg):
        self.country_name = country_name
        self.player_name = player_name
        self.matches = matches
        self.age = age
        self.batting_avg = batting_avg
        self.bowling_avg = bowling_avg

    def display(self):
        return f"Country Name: {self.country_name}, Player Name: {self.player_name}, Matches: {self.matches}, Age: {self.age}, Batting Avg: {self.batting_avg}, Bowling Avg: {self.bowling_avg}"


team_records = [
    Team("India", "Sachin", 295, 30, 45.51, 40.95),
    Team("Australia", "Ricky", 160, 28, 41.00, 53.00),
    Team("India", "Saurav", 230, 31, 30.00, 67.00)
]

# Display the records
for record in team_records:
    print(record.display())