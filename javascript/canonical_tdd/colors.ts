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
        let highest = this.findHighestIndex(this.input);

        switch (highest) {
            case 0: return "f00";
            case 1: return "0f0";
            case 2: return "00f";
        }

        throw "Unexpected input";
    }

    private findHighestIndex(input: string): number {
        let highestIndex: number = 0
        for (let i = 1; i < 3; i++) {
            if (parseInt(input[i],16) > parseInt(input[highestIndex],16)) {
              highestIndex = i;
            }
        }

        return highestIndex;
    }

    farthestColor(): string {
        let highest = this.findLowestIndex(this.input);

        switch (highest) {
            case 0: return "f00";
            case 1: return "0f0";
            case 2: return "00f";
        }

        throw "Unexpected input";
    }
 
    private findLowestIndex(input: string): number {
        let highestIndex: number = 0
        for (let i = 1; i < 3; i++) {
            if (parseInt(input[i],16) < parseInt(input[highestIndex],16)) {
              highestIndex = i;
            }
        }

        return highestIndex;
    }
    
}