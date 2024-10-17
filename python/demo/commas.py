class NumberFormatter:
    def format(self, number: int) -> str:
        if number < 1000:
            return str(number)
        else:
            return f"{number//1000},{number%1000:03d}"