import { expect, test } from 'vitest'
import { ColorEvaluator } from './colors'

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

test("a near-green color given returns red", () => {
    expect(new ColorEvaluator("de0").nearestColor()).toBe("0f0");
})
