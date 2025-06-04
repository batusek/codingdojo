export class NumbersInWords {
    // After start
    static ones = ["zero","one","two","threee","four","five","six","seven","eight","nine",
    "ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"];

    static printTensAndLower(number: number) {
        const tens = ["", "", "twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"];

        if (number<20)
            return this.ones[number];

        var result = tens[Math.floor(number/10)];
        var remainder = number % 10;
        if (remainder>0)
            result += " " + this.ones[remainder];

        return result;
    }

    // After end
    static printNumber(number: number) {
        // Uncomment:       throw {name : "NotImplementedError", message : "not started"}; 
        // After start
        if (number<100)
            return this.printTensAndLower(number);

        var result:string = "";
        if (number>=100)
            result = this.ones[Math.floor(number/100)] + " hundred";
            if (number>100)
                result += " and " + this.printTensAndLower(number%100);

        return result
        // After end
    }
}