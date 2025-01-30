
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
        score: int = 0
        last_letter = ""
        last_letter_score = 0
        letters_used: int = 0
        for char in word:
            if char in alphabet:
                score += last_letter_score
                letters_used += 1
                last_letter = char
                last_letter_score = alphabet[last_letter]
                continue

            if char=="*":
                last_letter_score += alphabet[last_letter]

            if char=="^":
                score -= last_letter_score

            if char=="(":
                break

        score += alphabet[last_letter]
        temp = self._apply_word_bonuses(word, score)
        return temp if letters_used < 7 else temp + 50

    def _apply_word_bonuses(self, word: str, raw_count: int) -> int:
        if word[-3:]=="(d)":
            return raw_count * 2

        if word[-3:]=="(t)":
            return raw_count * 3

        return raw_count
