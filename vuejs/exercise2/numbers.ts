export class NumbersInWords {
    static printNumber(number: number) {
        const ones = ["zero","one","two","threee","four","five","six","seven","eight","nine",
                    "ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"];
        return ones[number];
    }
}