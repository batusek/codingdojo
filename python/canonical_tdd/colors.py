# based on https:#codingdojo.org/kata/NearestColor/
# Instructions:
# Implement the ColorEvaluator class with the following methods
# - nearestColor - returns one of the R, G, B
# - fartherstColor - returns one of the R, G, B
# - (optional) deal with the situation when there are multiple nearest or furthers colors
# - (optional) allow symbolic color names as inputs
#
# Constraints:
#  - practice canonical TDD preparing a list of testcases in advance and maintaining it
#  - choose a test naming convention and keep it for the whole exercise

class ColorEvaluator:
    def __init__(self, color: str):
        self.color = color
        
    def nearestColor(self) -> str:
        return "f00"
