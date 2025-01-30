
class Scrabble:
    def score(self, word: str) -> int:
        alphabet: dict[str,int] = {
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
        result = 0
        last_letter = ""
        last_letter_score = 0
        for char in word:
            if char in alphabet:
                result += last_letter_score
                last_letter = char
                last_letter_score = alphabet[last_letter]
                continue

            if char=="*":
                last_letter_score += alphabet[last_letter]

            if char=="^":
                result -= last_letter_score

            if char=="(":
                break

        result += alphabet[last_letter]
        return self._apply_word_bonuses(word, result)

    def _apply_word_bonuses(self, word: str, raw_count: int) -> int:
        if word[-3:]=="(d)":
            return raw_count * 2

        if word[-3:]=="(t)":
            return raw_count * 3

        return raw_count
