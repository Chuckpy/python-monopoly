from models import Game, exit
from heapq import nlargest

def run():
    auto_run = input("Game will auto run ? ( y / n )")
    if auto_run.lower() in ['y','s']:
        times = int(input("How many times ?"))
        result = exit 
        try :

            for i in range(0,times) :
                game = Game(auto_run=True)
                while not game.done :
                    game.roll()
                else :
                    print(f" {game.winner} Won the game ! ".center(40,'*'))
                    game.finish(result)

        except TypeError: 
            raise ("Times must be an integer value")
        
        result['rounds_average'] = round((sum(result['rounds']))/(len(result["rounds"])), 2)
        result["most_winner"] = nlargest(1, result['winner_average'], key = result['winner_average'].get)[0]

        return result
        
    elif auto_run.lower() == 'n' :
        game = Game()
        while not game.done :
            roll_conf = input("Roll dices with Enter ")
            if roll_conf == "":
                game.roll()    


if __name__ == "__main__":
    result = run()
    from pprint import pprint
    pprint(result)
