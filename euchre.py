import random
import time



class deck:
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
    self.curtain = self.deck
    self.deck.clear()
    return self.player1, self.player2, self.player3, self.player4


deck = Deck()
deck_shuffled = deck.shuffle()
player1, player2, player3, player4 = deck.deal()
print(f"Player 1 : {player1} \nPlayer 2 : {player2} \nPlayer 3 : {player3} \nPlayer 4 : {player4}")
