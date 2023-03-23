export class NumbersInWords {
    static printNumber(number: number) {
        const ones = ["zero","one","two","threee","four","five","six","seven","eight","nine",
                    "ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"];
        const tens = ["", "", "twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"];

        if (number<20)
            return ones[number];

        var ten:number = Math.floor(number/10);
        var result = tens[ten];
        var remainder = number - ten*10;
        if (remainder>0)
            result += " " + ones[remainder];

        return result;
    }
}