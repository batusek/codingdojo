import { expect, test } from 'vitest'
import { ColorEvaluator } from './colors'

test("a red color given returns red", () => {
    expect(ColorEvaluator.nearestColor("f00")).toBe("f00");
})

test("a green color given returns green", () => {
    expect(ColorEvaluator.nearestColor("0f0")).toBe("0f0");
})