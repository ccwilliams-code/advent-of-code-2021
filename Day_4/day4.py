# Author: Charlie Williams

"""Calculate the first and last bingo cards to win a given bingo calling"""
from functools import total_ordering
from pprint import pprint

from aoc_utils import read_input


@total_ordering
class BingoCard:
    def __init__(self, cid: int, matrix: list[list]):
        self.numbers: list[list] = matrix
        self.wins_on_turn: int = 1
        self.score: int = 0
        self.final_score: int = -1
        self.done = False
        self.won_on_number = -1
        self.cid = cid

    def calc_score(self, winning_numbers: list[int]):
        for each in winning_numbers:
            if not self.done:
                self.mark_number(each)
                self.wins_on_turn += 1
                self.won_on_number = each
        for row in self.numbers:
            for number in row:
                if number != '*':
                    self.score += number
        self.final_score = self.score * self.won_on_number

    def mark_number(self, target_number):
        for each in self.numbers:
            try:
                each[int(each.index(int(target_number)))] = '*'
                if self.check_win():
                    self.done = True
                    pprint(self.numbers)

            except ValueError as ve:
                # expected error for when the value is not present in the current row
                pass
            if self.done:
                break

    def check_win(self) -> bool:
        return self.check_row_win() \
               or self.check_col_win()
        # or self.check_diagonal_win()

    def check_row_win(self):
        for each in self.numbers:
            if len(set(each)) == 1:
                return True

        return False

    def check_col_win(self):
        for r in range(0, len(self.numbers[0])):
            col = set()
            for c in range(0, len(self.numbers)):
                col.add(self.numbers[c][r])
            if len(col) == 1:
                return True
        return False

    def __eq__(self, other: 'BingoCard'):
        return self.wins_on_turn == other.wins_on_turn

    def __ne__(self, other: 'BingoCard'):
        return self.wins_on_turn != other.wins_on_turn

    def __lt__(self, other: 'BingoCard'):
        return self.wins_on_turn < other.wins_on_turn

    def __repr__(self):
        return f"Card #{self.cid} wins on turn #{self.wins_on_turn} with winning number {self.won_on_number} and final score {self.final_score}"


def main():
    data = read_input('input.txt')
    drawn_numbers = data.pop(0)
    # Absorb empty line
    data.pop(0)
    split_data = []

    # Sanitize the input - split on white space, eliminate extra \n
    for each in data:
        if len(each) > 1:
            split_data.append(list(map(int, each.split())))

    # split every 5 lines into its own matrix to represent Bingo card
    cards: list[BingoCard] = []
    for i in range(0, len(split_data), 5):
        card = BingoCard(int(i / 5 + 1), split_data[i:i + 5])
        card.calc_score(list(map(int, drawn_numbers.split(","))))
        cards.append(card)

    cards.sort()
    pprint(cards)


if __name__ == "__main__":
    main()
