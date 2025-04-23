use rand::seq::SliceRandom;
use rand::thread_rng;


enum Suits {
  Hearts,
  Clubs,
  Diamonds,
  Spades,
}

enum Ranks {
  Ace,
  Nine,
  Ten,
  Jack, 
  Queen,
  King,
}

struct Card {
  Suit : Suits,
  Ranks : Ranks,
  Trump : bool,
  Right_Bower : bool,
  Left_Bower : bool,
  Value : i32,
}

struct Player {
  ID : i32,
  Cards : Vec<Card>,
  Points : i32,
  Teammate : i32,
  Dealer : bool,
}

fn build() -> Vec<Card> {
  let suits = vec![Suits::Hearts, Suits::Diamonds, Suits::Spades, Suits::Clubs];
  let ranks = vec![Ranks::Ace, Ranks::Nine, Ranks::Ten, Ranks::Jack, Ranks::Queen, Ranks::King];
  let mut deck = Vec::new();

  for suit in &suits {
    for rank in &ranks {
      let _ = Card {
        Suit : &suit,
        Ranks : &rank,
        Trump : false,
        Right_Bower : false,
        Left_Bower : false,
        Value : 0, 
      };
      deck.push(&card);
    }
  }
  deck
}

fn shuffle(deck: Vec<Card>) -> Vec<Card> {
  let unshuffled = deck;
  
  let mut shuffled = Vec::new();
  let mut rng = thread_rng();

  shuffled = &unshuffled.shuffle(&mut rng);
  
  shuffled
}



fn deal(deck: Vec<Card>) -> Player, Player, Player, Player, Vec<Card> {
  for player in 0..4 {
    let cards = Vec::new()
    for card in 0..5 {
      cards.push(deck.choice())
    }
    let _ = Player{
      ID : player,
      Cards : cards,
      Points : 0,
      Teammate : 2,
      Dealer : true,
    };
  }
}
