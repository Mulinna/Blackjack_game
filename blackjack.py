rom replit import clear
from art import logo
import random

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose!"
    
  if user_score == computer_score:
    return "It's a draw!"
  elif computer_score == 0:
    return "Lose! The opponent has a Blackjack!"
  elif user_score == 0:
    return "Win with a Blackjack!"
  elif user_score > 21:
    return "You went over. You lose!"
  elif computer_score > 21:
    return "Computer went over. You win!"
  elif user_score > computer_score:
    return "You win!"
  else:
    return "You lose!"
  


def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not game_over:
  
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f" Your cards: {user_cards}, current score {user_score}")
    print(f" Computer's first hand {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      deal = input("Type 'y' to get another card, type 'n' to pass. ").lower()
      if deal == "y":
        user_cards.append(deal_card())
      else:
        game_over = True
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f" Your final hand: {user_cards}, final score: {user_score}")
  print(f" Computer's final hand: {computer_cards}, final score {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you wanna play a game of Blackjack? Type 'y' or 'n'. ").lower() == "y":
  clear()
  play_game()
