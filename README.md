# CLI-Student-Grade-Calculator
# CLI Student Grade Calculator

A simple command-line application built in Python that calculates a student's total marks, average, and letter grade based on subject-wise input.

## Overview

This project was built as a beginner-level exercise to practice core Python fundamentals — user input, loops, conditionals, and lists — through a small, practical program.

## Features

- Accepts student name and number of subjects
- Takes marks input for each subject
- Calculates total and average marks
- Assigns a letter grade based on average
- Displays a pass/fail result

## Requirements

- Python 3.x

## Installation

Clone the repository:
```bash
git clone https://github.com/ojaswip2828/CLI-Student-Grade-Calculator.git
cd CLI-Student-Grade-Calculator
```

## Usage

Run the script:
```bash
python grade_calculator.py
```

You will be prompted to enter:
1. Student name
2. Number of subjects
3. Marks for each subject (out of 100)

### Example

```
=== Student Grade Calculator ===
Enter student name: Asha
How many subjects? 5
Enter marks for subject 1 (out of 100): 85
Enter marks for subject 2 (out of 100): 90
Enter marks for subject 3 (out of 100): 78
Enter marks for subject 4 (out of 100): 88
Enter marks for subject 5 (out of 100): 92

--- Result ---
Name: Asha
Marks entered: [85.0, 90.0, 78.0, 88.0, 92.0]
Total: 433.0
Average: 86.6
Grade: A
Congratulations, you passed!
```

## Grading Scale

| Average Marks | Grade |
|----------------|-------|
| 90 and above   | A+    |
| 80 – 89        | A     |
| 70 – 79        | B     |
| 60 – 69        | C     |
| 50 – 59        | D     |
| Below 50       | F     |

## Project Structure

```
CLI-Student-Grade-Calculator/
├── grade_calculator.py
└── README.md
```

## Known Limitations

- No input validation (e.g., marks above 100 or negative values are accepted as-is)
- Marks are not saved anywhere; results only display on screen
- Code is written in a straightforward, linear style without functions or error handling

## Planned Improvements

- Add input validation for marks and subject count
- Refactor into functions
- Add option to save results to a file
- Handle invalid (non-numeric) input gracefully

## Author

Ojaswi — [GitHub](https://github.com/ojaswip2828)

This is one of my early projects while learning Python.
