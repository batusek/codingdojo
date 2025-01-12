from collections import Counter


class VowelCounter:
    def count_vowels2(self, text: str) -> int:
        vowels = "aeiouAEIOU"
        result = 0

        for vowel in vowels:
            result += text.count(vowel)

        return result


    def count_vowels(self, text: str) -> int:
        vowels = "aeiouAEIOU"
        counter = Counter([v for v in text if v in vowels])
        return counter.total()
