import random
import time


class Deck 
  def __init__(self):
    self.player1 = []
    self.player2 = []
    self.player3 = []
    self.player4 = []
    self.curtain = []
    self.deck = []
    self.shuffled = []
    self.unshuffled = ["ah", "9h", "10h", "jh", "qh", "kh", "ad", "9d", "10d", "jd", "qd", "kd", "as", "9s", "10s", "js", "qs", "ks", "ac", "9c", "10c", "jc", "qc", "kc"]
    
  def shuffle(self):
    if self.unshuffled == []:
      self.unshuffled = self.shuffled
      self.shuffled.clear()
    for i in range(len(self.unshuffled)):
      random_card = random.choice(self.unshuffled)
      random_card_index = self.unshuffled.index(random_card)
      self.unshuffled.pop(random_card_index)
      self.shuffled.append(random_card)
    return self.shuffled
    
  def deal(self):
    self.deck = self.shuffled
    player = 1
    for i in range(20):
      dealt = random.choice(self.deck)
      dealt_index = self.deck.index(dealt)
      
      if player == 1:
        self.player1.append(dealt)
      elif player == 2:
        self.player2.append(dealt)
      elif player == 3:
        self.player3.append(dealt)
      elif player == 4:
        self.player4.append(dealt)

      self.deck.pop(dealt_index)
      player += 1
      if player == 5:
        player = 1
    self.curtain = self.deck
    return self.player1, self.player2, self.player3, self.player4, self.curtain

if __name__ == "__main__":
  deck = deck()
  deck.shuffle()
  player1, player2, player3, player4, curtain = deck.deal()
  
  print(f"Player 1 :", " ".join(player1))
  print(f"Curtain : {curtain[0]}")
  
  
