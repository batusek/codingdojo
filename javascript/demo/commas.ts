function formatGroup(group: number): string {
    return ('00' + group).slice(-3);
}
export function formatNumber(number: number): string {
    if (number < 1000)
        return number.toString();

    let result: string = "";
    while (number >= 1000) {
        result = "," + formatGroup(number%1000) + result;
        number = Math.floor(number/1000);
    }

    return number.toString() + result;
}
