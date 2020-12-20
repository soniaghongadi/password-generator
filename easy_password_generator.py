import string
from random import shuffle, randint
from copy import deepcopy

try:
    from secrets import choice
except ImportError:
    from random import choice


class PassGen:
    """

    Set following property is allowed

    | property   |                          Description                 | Default |
    | ---------- |------------------------------------------------------| ------- |
    | minlen     |   Minimum length of the password                     | 6 |
    | maxlen     |   Maximum length of the password                     | 16 |
    | minuc  |   Minimum upper case characters  | 1 |
    | minlc  |   Minimum lower case characters  | 1 |
    | minnum |   Minimum numerical characters | 1 |
    | minsc  |   Minimum special characters| 1 |

    """

    def __init__(self, minlen=6, maxlen=16, minuc=1, minlc=1, minnum=1, minsc=1):
        self.minlen = minlen
        self.maxlen = maxlen
        self.minuc = minuc
        self.minlc = minlc
        self.minnum = minnum
        self.minsc = minsc

        self.lower_chars = string.ascii_lowercase
        self.upper_chars = string.ascii_uppercase
        self.numbers_list = string.digits
        self._schars = [
            "_", "+", "=", "<", ">", "?", "!", "^", "&", "*", "(", "#", "$", "%", ")", ",", ".", "-",
        ]
        self._allchars = (
            list(self.lower_chars)
            + list(self.upper_chars)
            + list(self.numbers_list)
            + self._schars
        )

    def generate(self):
        if (
            self.minlen < 0
            or self.maxlen < 0
            or self.minuc < 0
            or self.minlc < 0
            or self.minnum < 0
            or self.minsc < 0
        ):
            raise ValueError("Cant take -ve numbers")

        if self.minlen > self.maxlen:
            raise ValueError(
                "manlen can not be greater than maxlen"
            )

        collectiveMinLength = (
            self.minuc + self.minlc + self.minnum + self.minsc
        )

        if collectiveMinLength > self.minlen:
            self.minlen = collectiveMinLength

        final_pass = [
            choice(list(set(self.lower_chars)))
            for i in range(self.minlc)
        ]
        final_pass += [
            choice(list(set(self.upper_chars)))
            for i in range(self.minuc)
        ]
        final_pass += [
            choice(list(set(self.numbers_list)))
            for i in range(self.minnum)
        ]
        final_pass += [
            choice(list(set(self._schars)))
            for i in range(self.minsc)
        ]

        currentpasslen = len(final_pass)
        all_chars = list(
            set(self._allchars)
        )

        if len(final_pass) < self.maxlen:
            randlen = randint(self.minlen, self.maxlen)
            final_pass += [choice(all_chars)
                           for i in range(randlen - currentpasslen)]

        shuffle(final_pass)
        return "".join(final_pass)
