// based on https://codingdojo.org/kata/NearestColor/
// Instructions:
// Implement the ColorEvaluator class with the following methods
// - nearestColor - returns one of the R, G, B
// - furtherstColor - returns one of the R, G, B
// - deal with the situation when there are multiple nearest or furthers colors
// - allow symbolic color names as inputs
//
// Constraints:
//  - practice canonical TDD maintaining a list of testcases in advance
//  - choose a test naming convention and keep it for the whole exercise

export class ColorEvaluator {
    input: string;

    constructor(input: string) {
        this.input = input;
    }

    nearestColor(): string {
        let highest = this.findHighest(this.input);

        switch (highest) {
            case 0: return "f00";
            case 1: return "0f0";
            case 2: return "00f";
        }

        throw "Unexpected input";
    }

    private findHighest(input: string): number {
        let red = parseInt(input[0],16);
        let green = parseInt(input[1],16);
        let blue = parseInt(input[2],16);

        if (red>green)
            if (red>blue)
                return 0;
            else
                return 2;
        else
            if (green>blue)
                return 1;
            else
                return 2;
    }
}