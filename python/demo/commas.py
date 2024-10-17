class NumberFormatter:
    def format(self, number: int) -> str:
        if number<1000:
            return str(number)
        
        temp: int = number
        result: str = ""
        while temp >= 1000:
            result = f",{temp%1000:03d}{result}"
            temp = temp // 1000
        
        result = f"{temp}{result}"
        return result