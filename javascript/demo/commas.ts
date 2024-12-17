export function formatNumber(number: number): string {
    if (number < 1000)
        return number.toString();

    let thousands = number // 1000;
    let remainder = number % 1000;
    return thousands.toString + ";" + remainder.toString()
}
