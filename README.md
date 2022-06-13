# Python Monopoly

Here's a challenge, made it to use native python to make a game like monopoly and run a few trials with some kind of different players actions to understand witch one will be better in the game score

## Challenge

Consider the following hypothetical game very similar to Monopoly, where several of its mechanics have been simplified. In a match of this game, players change in rounds, in an order randomly defined at the beginning of the match. Players always start a match with a balance of 300 for each.

In this game, the board consists of 20 properties in sequence. Each property has a sale cost, a rental amount, a case owner are already purchased, and follow a certain order on the board. It is not possible to build hotels and no other improvement on the properties of the board, for simplicity of the problem.

At the beginning of the turn, the player plays an equiprobable dice of 6 faces that determine spaces on the board the player will walk.

- When falling into a property without owner, the player can choose between buying or not property. This is the only way a property can be purchased.
- When falling into a property that has owner, he must pay the owner the rent amount of the property.
- Upon completing a turn on the board, the player gains 100 balance.

Players can only buy properties if they have no owner and the player has the money from the sale. When buying a property, the player loses the money and gains ownership of the property.

Each of the players has a different behavior implementation, which dictates the actions that they will take over the course of the game. More details about the behavior will be explained later.
A player who gets a negative balance loses the game, and no longer plays. Loses its properties and therefore can be purchased by any other player.

Ends when only one player with a positive balance is left at any time of the match. This player is declared the winner.

We want to run a simulation to decide what the best strategy is. For this, we idealize a match with 4 different types of possible players. The defined behaviors are:

- Player one is Impulsive
- Player two is Demanding
- Player three is Cautious
- Player four is Random
  
The impulsive player buys any property on which he stops.

The demanding player buys any property, as long as the rental value of it is greater than 50.

The cautious player buys any property as long as he has a reserve of 80 balance left over after the purchase has been made.

The random player buys the property he stops on top with 50% probability.

If the game takes too long, as is customary in games of this nature, the game ends in the thousandth round with the win of the player with the most balance. The tiebreaker criterion is the turn order of the players in this departure.

## Exit

An execution of the proposed program should run 300 simulations, printing on the console the data executions. We hope to find in the data the following information:

- How many matches end per time out (1000 rounds);
- How many shifts on average takes a match;
- What is the percentage of wins by player behavior;
- What behavior wins the most.

## How to run

First of all you could need to use a virtual env to properly configure the requirements and exit after a few runs without use you own virtual environ. To do it, on a Linux, just type :

```bash
$ python3 -m venv venv
```

and activate with :

```bash
$ source venv/bin/activate
```

This project use just the native Python3+ libraries. So if you have it, don't need to install any requirements external libs.

To run the project, just type :

```bash
$ python3 main.py
```
