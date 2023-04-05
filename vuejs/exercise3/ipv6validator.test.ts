import { expect, test } from 'vitest'
import { IPv6Validator } from "./ipv6validator"

test("happy path eight groups filled with non zero octets", () => {
    let input = "123f:123f:123f:123f:123f:123f:123f:123f"
    expect(IPv6Validator.contract(input),input);
});

test("double colon is a valid address that cannot be contracted", () => {
    let input = "::"
    expect(IPv6Validator.contract(input),input);
});
