# Test excellence training

# Instructions

## Prerequisites

- Install Docker
- Install a git client
- Install Visual Studio Code
- Install Remote-Containers extension

## Steps

- Checkout repo `git clone https://github.com/batusek/codingdojo.git`
- Start Visual Studio Code
- Command Palette (F1): Select **Remote-Containers: Open Folder in Container...** and Select subfolder with your language of choice

### Python
- Command Palette (F1): **Python: Run All Tests** or 
- Go to Test Explorer and click on the green arrow icon or
- Run Ctrl+F5 in VS Code
The only existing test in `tooling/test_leapyear.py` should fail

### .Net
- Type "dotnet test" in terminal
The only existing test in `tooling/LeapYearTest.cs` should fail

### Javascript / Vue.js
- Type "npm test" in terminal or
- Run Ctrl+F5 in VS Code
The only existing test in `tooling/test/leapyear.test.ts` should fail

# Exercises

## Embrace the tooling
The first exercise is trivial from the programming point of view and its main purpose is to get acquainted with the tooling.
To finish it, it should be enough to write 4 tests and appropriate code inside one function. Please write the production code one test at a time!

Instructions: [Leap year](http://codingdojo.org/kata/LeapYears/)

## Practice baby steps
Try to do as many Red-Green-Refactor cycles as you can. One cycle should not take more than a couple of minutes.

Instructions: [Numbers in words](http://codingdojo.org/kata/NumbersInWords/)

## Grow my code
Start from scratch and grow your code with Red-Green-Refactor cycles. This exercise is a bit longer than the previous one. You probably start with only Red-Green for the first few tests. Over time you will observe that you added -Refactor to your flow - you code will call for it.

Instructions: [IPv6 address validator](https://www.codewars.com/kata/54fa4e210609868fce0002bf)

## Canonical TDD
The given kata is deliberately easy so that you can practice canonical TDD and naming your tests

Instructions: [Nearest color](https://codingdojo.org/kata/NearestColor/)


## Getting rid of external dependencies
An existing code that calls some infrastructure code inside is available including an integration test. Rewrite the code 3 times using various techniques for getting rid of dependencies and using tiny and safe refactorings before you write more focused tests. The three methods:
- Use mocks/stubs
- Use a virtual method and subclassing
- Make dependency explicit

## Refactoring alphabet
Practice a number of basic refactorings on focused examples.

## Monster method
Try this external kata on your language of choice 

Instructions: [Gilded rose](http://codingdojo.org/kata/GildedRose/) 

## Getting rid of a global dependency
Deal with a global dependency. Use incremental steps to create testable code.

## Testing a method with an irritating parameter
Try two methods of testing an irritating parameter
- pass null
- extract interface

## Testing a blob construction
Try two methods to deal with a blob
- a setter method
- subclass and override

## Testing a method with a side effect
Eliminate a side effect so that a method can be tested





[//]: <> (After start)
# TODO
## Exercise X Get rid of dependency
E.g. https://github.com/sandromancuso/trip-service-kata

[//]: <> (After end)
