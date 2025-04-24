use rand::seq::SliceRandom;
use rand::thread_rng;
use std::stdin;


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
  Turn : bool,
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
    Player{
      ID : player,
      Cards : cards,
      Points : 0,
      Teammate : 2,
      Dealer : false,
      Turn : false
    }
  }
  let cutain = deck;
  curtain
}

fn round(player1: Player, player2: Player, player3: Player, player4: Player, player_turn: i32, curtain: Vec<Card>) {
  let players = vec![player1, player2, player3, player4];
  for player in players {
    
  }

  let up_card = curtain.iter().next();
  println!("The Up-Card is {} of {}", up_card.Rank, up_card.Suit);

  let mut decision = String::new()
  println!("Pass or Accept as trump : ");
  let _ = stdin().read_line(&mut decision).unwrap();
  match decision {
    "pass" => {
      
    }
  }
  
}
