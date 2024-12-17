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
        max_index = self._get_max_index(self.color)
        
        match max_index:
            case 0: return "f00"
            case 1: return "0f0"
            case 2: return "00f"
            case _: return ""  
    
    def _get_max_index(self, color: str) -> int:
        result: int = 0
        for i in range(1,len(color)):
            if color[i]>color[result]:
                result = i
                
        return result
