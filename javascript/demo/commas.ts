function formatGroup(group: number): string {
    return ('00' + group).slice(-3);
}
export function formatNumber(number: number): string {
    if (number < 1000)
        return number.toString();

    let temp: number = number;
    let result: string = "";
    while (temp >= 1000) {
        result = "," + formatGroup(temp%1000) + result;
        temp = Math.floor(temp/1000);
    }

    return temp.toString() + result;
}
