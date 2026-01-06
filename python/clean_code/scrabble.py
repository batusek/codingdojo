
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
        word_multiplier, actual_word = self._parse_word_bonuses(word)
        base_score = self._calculate_base_score(actual_word)
        return base_score * word_multiplier

    def _parse_word_bonuses(self, word: str) -> tuple[int, str]:
        if word.endswith('(d)'):
            return 2, word[:-3]
        if word.endswith('(t)'):
            return 3, word[:-3]
        return 1, word

    def _calculate_base_score(self, word: str) -> int:
        score = 0
        i = 0
        last_score = 0
        while i < len(word):
            letter = word[i]
            if letter == '*':
                i += 1
                continue
            if letter == '^':
                score -= last_score
                last_score = 0
                i += 1
                continue

            letter_score = self.alphabet[letter]
            
            i += 1
            letter_multiplier = 1
            while i < len(word) and word[i] == '*':
                letter_multiplier += 1
                i += 1
            
            last_score = letter_score * letter_multiplier
            score += last_score
        return score
