
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
  suit : Suits,
  ranks : Ranks,
  trump : bool,
  right_bower : bool,
  left_bower : bool,
  value : i32,
}

fn build() -> [Card] {
  let suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
  let ranks = ["Ace", "9", "Ten", "Jack", "Queen", "King"]
}
      
