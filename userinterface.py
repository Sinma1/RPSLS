from versions import ClassicVersion, ExtendedVersion


class UserInterface:
    def __init__(self):
        self.version = None
        self.versions = {
            'c': ClassicVersion,
            'e': ExtendedVersion
        }

    def select_version(self):
        while True:
            v = input("Select desired version of game([C]lassic or [E]xtended): ").lower()
            if v in self.versions:
                self.version = self.versions[v]()
                break
            print("Not recognized choice.")

    def select_shape(self):
        while True:
            print("Select shape")
            for k, v in self.version.shortcuts.items():
                print(f"[{k}]: {v.value}", end=' ')

            print()
            choice = input("What is shape of your choice?: ")
            if choice in self.version.shortcuts:
                return self.version.shortcuts[choice]

            print("Not recognized choice.")

    def results(self, player, computer):
        print(f"You played {player.value}, and computer played {computer.value}")
        winner, loser = self.version.get_result(player, computer)
        if winner is None:
            print("Draw.")
            return

        player_won = True if player == winner else False
        interaction = self.version.get_interaction(winner, loser)
        print(f"{winner.value} {interaction} {loser.value}")
        print(f"You", "won." if player_won else "lost.")

    def run(self):
        while True:
            self.select_version()
            player_shape = self.select_shape()
            computer_shape = self.version.get_random_shape()
            self.results(player_shape, computer_shape)

            ans = input("Enter x to exit: ").lower()
            if ans in ('X', 'x'):
                break

        print("Thanks for playing, bye!")
