# ccwc - Coding Challenge Word Counter

A simple Python script to count bytes, lines, words, and characters in a file. Supports reading from standard input if no filename is specified.

[Link to challenge]("https://codingchallenges.fyi/challenges/challenge-wc")

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
- [Examples](#examples)
- [License](#license)

### Installation

Clone the repository or download the script directly.

```bash
git clone https://github.com/your-username/ccwc.git
cd wc-tool
```

### Usage

```bash
python3 solution.py [OPTIONS] [FILE]
```

### Options

    -c: Print byte counts
    -l: Print line counts
    -w: Print word counts
    -m: Print character counts

If no option is specified, it's equivalent to using -c, -l, and -w together.

### Examples

Counting from a file:

```bash

python3 solution.py -l test.txt
```

###### Output:

```
7145
```

Counting multiple metrics:

```bash

python3 solution.py -l -w -c test.txt
```

###### Output:

```
7145   58164  339292 test.txt
```

### Note

Feel free to modify this template based on your project's specific details and needs. Include any additional information or usage instructions that you find relevant.