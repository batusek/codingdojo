import { expect, test } from 'vitest'
import { ColorEvaluator } from './colors'

// Kata instructions: https://codingdojo.org/kata/NearestColor/

test("name and implement the first test", () => {
    // do nothing
})

// After start
test("a red color given returns red", () => {
    expect(new ColorEvaluator("f00").nearestColor()).toBe("f00");
})

test("a green color given returns green", () => {
    expect(new ColorEvaluator("0f0").nearestColor()).toBe("0f0");
})

test("a blue color given returns blue", () => {
    expect(new ColorEvaluator("00f").nearestColor()).toBe("00f");
})

test("a near-red color given returns red", () => {
    expect(new ColorEvaluator("d30").nearestColor()).toBe("f00");
})

test("a near-green color given returns green", () => {
    expect(new ColorEvaluator("de0").nearestColor()).toBe("0f0");
})

test("a near-blue color given returns blue", () => {
    expect(new ColorEvaluator("def").nearestColor()).toBe("00f");
})

test("a far-red color given returns red", () => {
    expect(new ColorEvaluator("678").farthestColor()).toBe("f00");
})

test("a far-green color given returns green", () => {
    expect(new ColorEvaluator("f04").farthestColor()).toBe("0f0");
})

test("a far-blue color given returns blue", () => {
    expect(new ColorEvaluator("ee0").farthestColor()).toBe("00f");
})
// After end
