import { expect, test } from 'vitest'
import { IPv6Address } from "./ipv6validator"

test("happy path eight groups filled with non zero octets", () => {
    let input = "123f:123f:123f:123f:123f:123f:123f:123f"
    expect(new IPv6Address(input).contract()).toEqual(input);
});

