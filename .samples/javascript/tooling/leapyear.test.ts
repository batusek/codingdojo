import { expect, test } from 'vitest'
import { leapYear } from "./leapyear";

// Kata instructions: http://codingdojo.org/kata/LeapYears/

test("Normal year is not leap year", () => {
// Uncomment:    expect(true).toBeFalsy();
    // After start
    expect(leapYear(1993)).toBeFalsy();
    // After end
})

// After start
test("Every 4 years there is a leap year", () => {
    expect(leapYear(1996)).toBeTruthy();
})

test("Every 100 years there is not a leap year", () => {
    expect(leapYear(1900)).toBeFalsy();
})

test("Every 400 years there is not a leap year", () => {
    expect(leapYear(2000)).toBeTruthy();
})
// After end
