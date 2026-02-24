### Tests and linter status:   
[![Actions Status](https://github.com/aasineln/brain-games/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/aasineln/brain-games/actions)  [![QA SonarQube](https://sonarcloud.io/api/project_badges/measure?project=aasineln-brain-games&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=aasineln_aasineln-brain-games&branch=main)

## Brain Games
Brain Games is a collection of console mini-games designed to train logical thinking and test basic math skills. The project consists of five engaging mathematical challenges, each launched with a separate command.

🎮 Included Games:
```
* Brain Even — determine if a number is even
* Brain Calc — perform simple arithmetic operations
* Brain GCD — find the greatest common divisor of two numbers
* Brain Progression — find the missing element in an arithmetic progression
* Brain Prime — check if a number is prime
```

All games follow the same principle: the player is asked three questions in sequence and must provide correct answers to win.

### 🛠 Requirements

    Python 3.12 or higher
    uv package manager

### ⚙️ Installation
```bash
git clone https://github.com/aasineln/brain-games.git
cd brain-games
make build
make package-install
```

### 🚀 Available Game Commands

Once the package is installed, games are available as separate console commands:
bash
```
brain-games          # greet the player
brain-even           # even number check
brain-calc           # calculator
brain-gcd            # greatest common divisor
brain-progression    # arithmetic progression
brain-prime          # prime number check
```

### 📦 Makefile Commands

The project uses a Makefile to automate routine tasks:
```
make install — install project dependencies
make build — build package distributions
make package-install — install the built package globally
make lint — check code with Ruff linter
make lint-fix — automatically fix linter errors
make black — format code with Black
```

### 🎥 Demo
[![asciicast](https://asciinema.org/a/KmBzdRWcPz4tbM6u.svg)](https://asciinema.org/a/KmBzdRWcPz4tbM6u)

