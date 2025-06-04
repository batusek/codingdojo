import { expect, test } from 'vitest'
import { IPv6Address } from "./ipv6validator"

// Kata instructions: https://www.codewars.com/kata/54fa4e210609868fce0002bf

test("happy path eight groups filled with non zero octets", () => {
    let input = "123f:123f:123f:123f:123f:123f:123f:123f"
    expect(new IPv6Address(input).contract()).toEqual(input);
});

