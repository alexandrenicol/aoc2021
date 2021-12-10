from typing import List

puzzle_input = open("puzzle-input-6-example.txt", "r")
lines = puzzle_input.readlines()


class FishRegister:
    def __init__(self):
        self.lanternfishes: List[Lanternfish] = []

    def create_new_lanternfish(self):
        self.lanternfishes.append(Lanternfish(self))

    def get_state(self) -> str:
        state = ",".join([str(fish.internal_timer) for fish in self.lanternfishes])
        return state


class Lanternfish:
    def __init__(
        self,
        fish_register: FishRegister,
        initial_timer: int = 9,
    ):
        self.internal_timer = initial_timer
        self.fish_register = fish_register

    def age(self):
        self.internal_timer -= 1
        if self.internal_timer < 0:
            self.internal_timer = 6
            self.fish_register.create_new_lanternfish()


class Scenario:
    def __init__(self, fish_register: FishRegister, days: int = 80):
        self.fish_register = fish_register
        self.days = days

    def simulate(self):
        # print(f"Initial state: {self.fish_register.get_state()}")
        for i in range(self.days):
            self.turn()
            print(i)
            # print(f"After {i+1} day(s): {self.fish_register.get_state()}")

        print(len(self.fish_register.lanternfishes))

    def turn(self):
        for fish in self.fish_register.lanternfishes:
            fish.age()


fish_register = FishRegister()

for line in lines:
    input_data = list(map(int, line.split(",")))

    for initial_fish_timer in input_data:
        fish_register.lanternfishes.append(
            Lanternfish(fish_register, initial_fish_timer)
        )

game = Scenario(fish_register, 256)
game.simulate()
