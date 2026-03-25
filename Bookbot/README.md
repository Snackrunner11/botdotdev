# BookBot

BookBot is a Python tool built to analyze text files like books to provide statistical insights. It is my first project for Boot.dev.

## Features

* Word Count Analysis: The application reads the provided text file and calculates the total word count.
* Character Frequency Tracking: It counts the occurrence of every letter in the alphabet. This process is case insensitive to ensure accuracy.
* Organized Reporting: Insights are displayed in the terminal with a clean report. Character data is sorted by frequency from most common to least common.

## Usage

To use this application, you will need Python installed. Run the main script from your terminal and provide the path to the book file as an argument.

Basic Command:
`python3 src/main.py <path_to_book>`

Example Command:
`python3 src/main.py books/frankenstein.txt`

## Code Overview

* `src/main.py`: Manages the terminal interface, processes arguments, and prints the final report.
* `src/stats.py`: Contains the logic for file reading, word counting, and letter frequency calculations.
