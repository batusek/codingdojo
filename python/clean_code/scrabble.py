
class Scrabble:
    alphabet: dict[str, int] = {
        'a': 1,
        'b': 3,
        'c': 3,
        'd': 2,
        'e': 1,
        'f': 4,
        'g': 2,
        'h': 4,
        'i': 1,
        'j': 8,
        'k': 5,
        'l': 1,
        'm': 3,
        'n': 1,
        'o': 1,
        'p': 3,
        'q': 10,
        'r': 1,
        's': 1,
        't': 1,
        'u': 1,
        'v': 4,
        'w': 4,
        'x': 8,
        'y': 4,
        'z': 10
    }

    def score(self, word: str) -> int:
        word_multiplier = 1
        if word.endswith('(d)'):
            word_multiplier = 2
            word = word[:-3]
        if word.endswith('(t)'):
            word_multiplier = 3
            word = word[:-3]

        clean_word = word.replace('*', '').replace('^', '')
        bonus = 0
        if len(clean_word) == 7:
            bonus = 50

        total = 0
        word_iterator = iter(range(len(word)))
        for i in word_iterator:
            letter = word[i]
            score = self.alphabet.get(letter, 0)

            if i + 1 < len(word) and word[i + 1] == '*':
                if i + 2 < len(word) and word[i + 2] == '*':
                    score *= 3
                    next(word_iterator, None)
                    next(word_iterator, None)
                else:
                    score *= 2
                    next(word_iterator, None)
            
            if i + 1 < len(word) and word[i+1] == '^':
                score = 0
                next(word_iterator, None)

            total += score
        return total * word_multiplier + bonus