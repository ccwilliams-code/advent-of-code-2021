# Author: Charlie Williams

"""Simulate Lanternfish"""

from aoc_utils import read_input


class Fish:

    def __init__(self, timer=8):
        self.timer = timer

    @staticmethod
    def spawn() -> 'Fish':
        return Fish(6 + 2)

    def tick(self) -> 'Fish':
        if self.timer == 0:
            self.timer = 6
            return Fish.spawn()

        else:
            self.timer -= 1
            return None

    def __repr__(self):
        return str(self.timer)


def main():
    data = read_input('input.txt')
    days_to_simulate = 256
    data = data[0].split(',')
    sea: list[Fish] = []
    for each in data:
        sea.append(Fish(int(each)))

    for day in range(1, days_to_simulate + 1):
        print(f'Day:{day}')
        # print(f'Start:{sea}')
        new_fish: list['Fish'] = []
        for fish in sea:
            result = fish.tick()
            if result:
                new_fish.append(result)
        if len(new_fish) > 0:
            sea += new_fish

        # print(f'Finish:{sea}')
        print(len(sea))


if __name__ == "__main__":
    main()
