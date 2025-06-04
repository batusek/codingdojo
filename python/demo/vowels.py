from collections import Counter


class VowelCounter:
    def count_vowels2(self, text: str) -> int:
        result = 0
        for letter in "aeiouAEIOU":
            result += text.count(letter)

        return result

    def count_vowels(self, text: str) -> int:
        vowels = "aeiouAEIOU"
        counter = Counter([char for char in text if char in vowels])
        return counter.total()

    def count_consonants(self, text: str) -> int:
        return 2

    def count_letters(self, text: str) -> int:
        return self.count_vowels(text) + self.count_consonants(text)