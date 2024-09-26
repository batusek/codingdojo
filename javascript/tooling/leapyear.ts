export function leapYear(year: number) {
    // Uncomment:   throw {name : "NotImplementedError", message : "not started"}; 
    if (year % 400 == 0)
        return true;

    if (year % 100 == 0)
        return false;

    return year%4==0;
    // After end
}