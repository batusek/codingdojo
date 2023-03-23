export class NumbersInWords {
    static printTensAndLower(number: number) {
        const ones = ["zero","one","two","threee","four","five","six","seven","eight","nine",
                    "ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"];
        const tens = ["", "", "twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"];

        if (number<20)
            return ones[number];

        var result = tens[Math.floor(number/10)];
        var remainder = number % 10;
        if (remainder>0)
            result += " " + ones[remainder];

        return result;
    }
    static printNumber(number: number) {
        if (number<100)
            return this.printTensAndLower(number);

        var result:string = "";
        if (number>=100)
            result = "one hundred";
            if (number>100)
                result += " and " + this.printTensAndLower(number%100);

        return result
    }
}