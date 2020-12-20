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

    def next(self, num):
        if(num<1):
            return self.generate()
        shuffle = ""
        for i in range(num):
            shuffle = self.generate()
        return shuffle

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
        # add min added lowercase character 
        generated_password = [
            choice(list(set(self.lower_chars)))
            for i in range(self.minlc)
        ]
        # add min added upper character 
        generated_password += [
            choice(list(set(self.upper_chars)))
            for i in range(self.minuc)
        ]
        # add min added number character 
        generated_password += [
            choice(list(set(self.numbers_list)))
            for i in range(self.minnum)
        ]
        # add min added special character 
        generated_password += [
            choice(list(set(self._schars)))
            for i in range(self.minsc)
        ]

        pass_len_so_far = len(generated_password)
        all_chars = list(
            set(self._allchars)
        )

        if len(generated_password) < self.maxlen:
            randlen = randint(self.minlen, self.maxlen)
            result = []
            for i in range(randlen - pass_len_so_far):
                result.append(choice(all_chars))
            generated_password += result

        shuffle(generated_password)
        return "".join(generated_password)
