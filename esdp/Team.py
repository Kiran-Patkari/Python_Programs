class Team:

    def __init__(self,country_name,name_of_player,age,no_of_matches,batting_avg,building_avg):
        self.country_name=country_name
        self.name_of_player=name_of_player
        self.age=age
        self.no_of_matches=no_of_matches
        self.batting_avg=batting_avg
        self.batting_avg=batting_avg

    def display(self):
       print(self.country_name)
       print(self.name_of_player)
       print(self.age)
       print(self.no_of_matches)
       print(self.batting_avg)
       print(self.building_avg)


country_name=input()
name_of_player=input()
age=int(input())
no_of_matches=int(input())
batting_avg=float(input())
building_avg=float(input())

t1=Team(country_name,name_of_player,age,no_of_matches,batting_avg,building_avg)
t1.display()





