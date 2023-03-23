export class NumbersInWords {
    static printNumber(number: number) {
        const ones = ["zero","one","two","threee","four","five","six","seven","eight","nine",
                    "ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"];

        if (number<20)
            return ones[number];

        return "twenty";
    }
}