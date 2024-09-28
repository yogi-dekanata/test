
# Python Solutions - Cuti, Bracket Validator, and More

## Table of Contents
- [Introduction](#introduction)
- [Folder Structure](#folder-structure)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Unit Tests](#unit-tests)

## Introduction
This repository contains multiple Python solutions for different problems such as:
1. **String Matching (Case Insensitive Comparator)**
2. **Bracket Validation Without Regex**
3. **Leave Permission Validation for Employees**

Each problem has its respective Python solution along with unit tests to ensure correctness.

## Folder Structure

```
.
├── soal_1.py              # Solution for Case Insensitive String Matcher
├── soal_2.py              # Solution for Bracket Validator Without Regex
├── soal_3.py              # Solution for Leave Permission Validator
├── soal_4.py              # Another solution file for specific task
├── test_soal_1.py         # Unit tests for soal_1.py
├── test_soal_2.py         # Unit tests for soal_2.py
├── test_soal_3.py         # Unit tests for soal_3.py
├── test_soal_4.py         # Unit tests for soal_4.py
└── README.md              # This README file
```

## Requirements

Before running the program, make sure you have Python 3.x installed.

You can also install the required dependencies if any exist (depending on the libraries used in the code). However, the code provided here should run using the standard Python library.

## How to Run

### Running the main programs

Each Python solution can be run individually by executing the Python script. 

For example, to run `soal_1.py`, use the following command:

```bash
python soal_1.py
```

Repeat the same for other files like `soal_2.py`, `soal_3.py`, etc.

Each file is designed to accept dynamic input via the console when you run it. Here’s how the input/output looks like:

### Example for Leave Permission Validator (`soal_3.py`):
```
Jumlah Cuti Bersama = 7
Tanggal join karyawan (YYYY-MM-DD) = 2021-05-01
Tanggal rencana cuti (YYYY-MM-DD) = 2021-11-05
Durasi cuti (hari) = 3

Output:
• False
• Alasan: Karena hanya boleh mengambil 1 hari cuti.
```

You can replace the values according to your test cases.

## Unit Tests

Each solution has its corresponding unit test file to verify the correctness of the solution.

To run the tests, simply use the following command for each test file:

```bash
python -m unittest test_soal_1.py
python -m unittest test_soal_2.py
python -m unittest test_soal_3.py
python -m unittest test_soal_4.py
```

### Example Output for Running Unit Tests
```
Ran 4 tests in 0.002s

OK
```

Ensure all tests pass before confirming the validity of your solutions.

## Conclusion

This repository serves as a structured way to test and validate solutions for various common programming tasks. It uses a Pythonic approach along with SOLID principles in problem-solving.
