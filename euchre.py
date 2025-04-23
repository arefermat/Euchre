import random
import time



class deck:
  def __init__(self):
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
      

deck = deck()
print(deck.shuffled())
