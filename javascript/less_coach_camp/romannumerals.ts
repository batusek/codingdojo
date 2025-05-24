export function romanNumeral(input: number) : string {
  if (input == 4) {
    return "IV"
  }

  if (input == 5) {
    return "V"
  }
  return oneTwoThree(input);
}

function oneTwoThree(input: number) {
  let output = '';
  for (let i = 0; i < input; i++) {
    output += 'I';
  }
  return output;
}
