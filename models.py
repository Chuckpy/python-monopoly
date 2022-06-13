import random
import settings
import time 



class Player(object) :

    def __init__(self, name:str ="Player", money:int = 300, house:int = 0) :
        self.name = name
        self.money = money
        self.house = house

    def run_board(self, rolling):
        if (self.house + rolling) > (settings.NUM_HOUSES - 1) :
            self.money += 100
            print(f"Congratulation {self.name} you got $100 by passing Start !")
            self.house = ( (self.house + rolling) - settings.NUM_HOUSES  )
        else :
            self.house += rolling

    def __str__(self):
        return f"Player {self.name}"
    

class House(object):

    def __init__(self, name:str= 'House', price : int = 0, rent : int = 0, owner : Player = None):
        self.name = name        
        self.price = price
        self.rent = rent
        self.owner = owner
            
    def __str__(self):
        return f"{self.name}"
        

        
class Board(object):
    def __init__(self, name:str = "Default", houses : list[House] = []):
        self.name = name
        self.houses = houses
        self.houses_names = ["Start", "Trancoso", "Porto Seguro", "Salvador", "Jericoacoara", "Maragogí", "Fernando de Noronha","Campinas", "São José dos Campos", "Campos do Jordão", "Manaus","Capitólio", "Brasilia", "Copacabana","Arraial do Cabo","Búzios", "B. Camboriú", "Gramado", "São Paulo", "Belo Horizonte"]
        self.houses_price = [0,200,250,200,200,150,350,85,90,100,75,85,300,100,150,275,150,400,450,155]
        self.houses_rent = [0,40,45,40,35,30,70,10,15,20,5,10,60,20,30,55,30,75,65,25]
        for house_id in range(settings.NUM_HOUSES) :
            house_name = self.houses_names.pop(0)
            house_price = self.houses_price.pop(0)
            house_rent = self.houses_rent.pop(0)
            house = House(f"{house_name} #{house_id}", house_price,house_rent)
            self.houses.append(house)
    
    def __str__(self):
        return f"Board {self.name}"



class Game(object):
    '''
    Here's the magic !
    The object Game gather the other models and runs the main methods to the players user the game, it has default values
    but you has to insert at least the Players models to use it
    The object also has the number of rounds in it, and wil stop the game if the number of rounds were bigger than 1000 (Could also be changed at settings)
    '''

    def __init__(self, auto_run = False, max_rounds:int = settings.MAX_ROUNDS) :
        self.round = 1
        self.players = None
        self.now_playing = None
        self.board = None
        self.max_rounds = max_rounds
        self.done = False
        self.winner = None
        self.auto_run = auto_run
        self.mode = None
        self.get_players(settings.NUM_PLAYERS)
        self.get_board()
        self.next_player()
        print("-"*50)
        print(f" Round #{self.round} ".center(50,'-'))
        print("-"*50)
        print(f"{self.now_playing} It's your turn ! The game will begin")

    def get_players(self, num_players : int ):
        '''
        Create a list of Players between 2 and 8 players. It Could have also have the difference between the players
        '''        
        print("Creating the players list")
        if (num_players < 2) or (num_players > 8):
            raise ValueError(f"A game must have between 2 to 8 players. You input {num_players} players. You should change inside settings.py")
        if self.auto_run :
            players_list = ["Impulsive", "Demanding", "Cautious", "Random"]
            self.players = [Player(player) for player in players_list]
        else :
            self.players = [Player(input(f"Player #{player} name here :  ")) for player in range(1,num_players+1)]

    def next_player(self):
        if not self.now_playing :
            print("No one was playing before, lets randomize the players list")
            self.players = random.sample(self.players, len(self.players))
            print("This is the new order of Players :")
            self.list_players_order()
        self.now_playing = self.players.pop(0)
        self.players.append(self.now_playing)
        return self.now_playing

    def roll(self):
        if self.done :
            raise StopIteration("Game has ended")
        if self.now_playing :
            print(f"You are in the house {self.board.houses[self.now_playing.house]}")
            print("Roling Dices ... ")
            if not self.auto_run :
                time.sleep(random.randrange(1,3))
            roll = random.randint(1,6)
            if not self.auto_run :
                time.sleep(random.randrange(1,3))
            print(f" {self.now_playing} you got {roll} on dice!")
            if not self.auto_run :
                time.sleep(random.randrange(1,3))
            self.now_playing.run_board(roll)
            if not self.auto_run :
                time.sleep(random.randrange(1,3))
            self.show_wallet()
            print(f"{self.now_playing} you reach at {self.board.houses[self.now_playing.house]} !")
            print(f"Price : ${self.board.houses[self.now_playing.house].price} ")
            print(f"Rent :$ {self.board.houses[self.now_playing.house].rent} ")
            if not self.auto_run :
                time.sleep(random.randrange(1,3))
            self.buy(self.board.houses[self.now_playing.house])            
            self.show_wallet()
            if not self.auto_run :
                time.sleep(random.randrange(1,3))
            self.quit_player()
            self.update_round()
            if not self.done :
                print("-"*50)
                print(f" Round #{self.round} ".center(50,'-'))
                print("-"*50)
                print(self.next_player(), "It's your turn !")
        elif self.done :
            raise AttributeError("Game Just ended !")
        else :
            raise ValueError("You must have a player on the roll")

    def list_players_order(self):
        print("-"*50)
        if self.players :
            for player in self.players :
                print(f"{player} | wallet : {player.money}")
        print("-"*50)
    
    def list_players_end(self):
        print(f"  Lista de Jogadores  ".center(50, '-'))
        if self.players :            
            money_list = []            
            for player in self.players :
                money_list.append(player.money)
            for player in self.players :
                if player.money == max(money_list) :
                    self.winner = player
            while len(self.players) > 0 :                
                for player in self.players :
                    if player.money == max(money_list) :
                        print(f"{player} | wallet : {player.money}")
                        self.players.remove(player)
                        money_list.remove(max(money_list))
        print("-"*50)
    
    def quit_player(self):
        if self.now_playing.money <= 0 :
            print(f"{self.now_playing} unfortunately you're bellow the minimum amount of money to keep playing, sorry")            
            for house in self.board.houses :
                if house.owner == self.now_playing :
                    house.owner = None            
            self.players.remove(self.now_playing)
            if len(self.players) == 1 :
                self.winner= self.players[0]
                self.done = True
                self.mode = 'winner'
    
    def show_wallet(self):
        print(f"Player {self.now_playing.name} you have ${self.now_playing.money} on your wallet")

    def get_board(self, name:str= "Test"):
        self.board = Board(name)
    
    def update_round(self):
        if self.round < 1000 :
            self.round += 1
        elif self.round >= 1000 :            
            print("Game has to end, thats the players list :")            
            self.done = True
            self.mode = "timed_out"
            self.list_players_end()
            
    def buy(self, house) :
        if house.owner :
            if house.owner != self.now_playing :
                print(f"This house has an owner, you must pay the rent price : $ {house.rent}")                
                value = house.rent if (self.now_playing.money >= house.rent) else self.now_playing.money
                self.now_playing.money -= value
                house.owner.money += value                
                print(f"{house.owner} you have own ${value} by renting ")
            else :
                print("You're the owner, don't need to pay rent")
        else :
            if house.name != "Start #0" :                
                if self.auto_run and self.now_playing.name == "Impulsive" : 
                    buy = "y"
                elif self.auto_run and self.now_playing.name == "Demanding" : 
                    buy = 'y' if (self.board.houses[self.now_playing.house].rent) > 50 else ''
                elif self.auto_run and self.now_playing.name == "Cautious" : 
                    buy = 'y' if (self.now_playing.money) >= 80 else ''
                elif self.auto_run and self.now_playing.name == "Random" : 
                    buy = 'y' if (bool(random.getrandbits(1))) else '' # flip a coin
                else:
                    buy = input(f"Do you want to buy this property ? [ y / n ]")
                if buy.lower() in ['y', 's']:
                    if house.price < self.now_playing.money :
                        print(f"{house.name.title()} is now property of Player #{self.now_playing.name}")
                        house.owner = self.now_playing
                        self.now_playing.money -= house.price
                    else :
                        print("You haven't enough money to buy it")

    def finish(self, result_dict):
        if self.mode == "timed_out" :
            result_dict["timed_out"] += 1
        result_dict["rounds"].append(self.round) 
        result_dict["winner_average"][f"{self.winner.name}"] += 1

    def __str__(self):
        return "Monopoly !"
    

exit = {
    "timed_out" : 0,
    "rounds" : [],
    "rounds_average" : 0,
    "winner_average" :{
        "Impulsive":0,
        "Demanding":0, 
        "Cautious":0, 
        "Random":0
    },
    "most_winner" : ""
}

