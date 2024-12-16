import { expect, test } from 'vitest'
import { ColorEvaluator } from './colors'

test("a red color given returns red", () => {
    expect(ColorEvaluator.nearestColor("f00")).toBe("red");
})