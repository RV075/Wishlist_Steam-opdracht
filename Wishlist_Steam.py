class Game:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - €{self.price:.2f}"


class Wishlist:
    def __init__(self):
        self.games = []

    def add_game(self, game: Game):
        self.games.append(game)

    def view_games(self):
        if not self.games:
            print("wishlist is empty")
        else:
            print("wishlist:")
            for game in self.games:
                print(f"- {game}")

    def total_price(self):
        total = sum(game.price for game in self.games)
        return total

def main():
    wishlist = Wishlist()

    while True:
        print("steam wishlist")
        print("1) view games")
        print("2) add game")
        print("3) calculate total price")
        print("4) exit")

        choice = input("choose from 1, 2, 3, 4: ")

        match choice:
            case "1":
                wishlist.view_games()
            case "2":
                name = input("enter the game's name: ")
                try:
                    price = float(input("enter the game's price: €"))
                    game = Game(name, price)
                    wishlist.add_game(game)
                    print(f"{name} added to wishlist")
                except ValueError:
                    print("invalid price")
            case "3":
                total = wishlist.total_price()
                print(f"total price of the wishlist: €{total:.2f}")
            case "4":
                print("exit successful")
                break
            case _:
                print("invalid input")


if __name__ == "__main__":
    main()