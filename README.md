### SonarQube
[![QA SonarQube](https://sonarcloud.io/api/project_badges/measure?project=aasineln_python-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=aasineln_python-project-49&branch=main)

### Hexlet tests and linter status:
[![Actions Status](https://github.com/aasineln/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/aasineln/python-project-49/actions)


### Requirements
    - Python 3.12 или выше
    - Менеджер пакетов uv

### Installation
```bash
git clone https://github.com/aasineln/python-project-49.git
cd python-project-49
make build
make package-install
```

### Makefile
`make install` - Установка зависимостей проекта  
`make build` - Сборка дистрибутивов пакета  
`make package-install` - Установка собранного пакета глобально  
`make lint`	- Проверка кода линтером Ruff  
`make lint-fix` - Автоматическое исправление ошибок линтера  
`make black` - Форматирование кода с помощью Black  

### Run games 
```
brain-games  # игра "Приветствие игрока"
brain-even  # игра "Четность числа"
brain-calc  # игра "Математические операции"
brain-gcd  # игра "НОД" наибольший общий делитель
brain-progression  # игра "Прогрессия"
brain-prime  # игра "Простое число"
```

### Brain Games demo
[![asciicast](https://asciinema.org/a/KmBzdRWcPz4tbM6u.svg)](https://asciinema.org/a/KmBzdRWcPz4tbM6u)

