# Test-driven development training

# Instructions

## Prerequisites

- Install Docker
- Install a git client
- Install Visual Studio Code
- Install Remote-Containers extension

## Steps

- Checkout repo `git clone https://github.com/batusek/tddtraining.git`
- Start Visual Studio Code
- Command Palette (F1): Select **Remote-Containers: Open Folder in Container...** and Select folder where you cloned the git repo

### Python
- Command Palette (F1): **Python: Run All Tests** or go to Test Explorer and click on the green arrow icon
The only existing test in `exercise1/leapyeartest.py` should fail

### .Net
- Type "dotnet test" in terminal
The only existing test in `exercise1/LeapYearTest.cs` should fail

# Exercises

## Exercise 1 - Embrace the tooling
The first exercise is trivial from the programming point of view and its main purpose is to get acquainted with the tooling.
The exercise comes from http://codingdojo.org/kata/LeapYears/
To finish it it should be enough to write 4 tests and appropriate code inside one function. Please write the production code one test at a time!

## Exercise 2  TDD on a new code (almost no refactor)
E.g. http://codingdojo.org/kata/Mastermind/ or http://codingdojo.org/kata/NumbersInWords/


## Exercise X Refactor and existing class/method
E.g. http://codingdojo.org/kata/GildedRose/

## Exercise X Get rid of dependency
E.g. https://github.com/sandromancuso/trip-service-kata



