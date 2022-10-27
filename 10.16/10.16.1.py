from random import randrange as rr, choice as ch
from string import ascii_lowercase as alc


class TestCase:
    def __init__(self):
        self.messages = [
            ''.join(ch(alc) for _ in range(rr(3, 6)))
            for _ in range(1000)
        ]
        self.numbers = [
            (rr(10, 100) for _ in range(rr(4, 7)))
            for _ in range(1000)
        ]
        # ... другие поля?

    def print_msg(self):
        msg = self.messages.pop()
        print(msg)

    def sum_nums(self):
        nums = self.numbers.pop()
        print(sum(nums))