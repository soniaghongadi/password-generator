# Random password Generator
[![PyPI version](https://img.shields.io/badge/PYPI-V%200.0.4-blue.svg)](https://pypi.org/project/easy-password-generator)
[![Build Status](https://travis-ci.com/soniaghongadi/password-generator.svg?branch=master)](https://travis-ci.com/soniaghongadi/password-generator.svg)

##### A strong but super simple to use library to generate passwords 
 * Supports Flask, Django 
 * Generate a simple password of default length 6-16.

## Usage
 * Install the library.
 * Import the library.
 * Modify the default properties. (Optional)
 * Generate strong password (Default length of password 6-16 unless specified via properties).

``` bash
  pip install easy-password-generator
```

``` python
  from easy_password_generator import PassGen

  pwo = PassGen()
  pwo.generate()
```


## Configuration

| property   |                          Description                 | Default |
| ---------- |------------------------------------------------------| ------- |
| minlen     |   Minimum length of the password                     | 6 |
| maxlen     |   Maximum length of the password                     | 16 |
| minuc  |   Minimum upper case characters  | 1 |
| minlc  |   Minimum lower case characters  | 1 |
| minnum |   Minimum numerical characters | 1 |
| minsc  |   Minimum special characters| 1 |

## Examples:
``` python
  pwo = PasswordGenerator()
  pwo.generate()
```

### Generate a custom password
``` python
  pwo = PasswordGenerator(minlen = 30, maxlen=20, min)

  pwo.generate()
```

### Generate Non Duplicate Password
``` python
  pwo = PasswordGenerator()

  # length of required password
  pwo.next(20)
```

## Update V1.0.0
From version 1.0.0, Initial library launch

## Contributions
Contributions can be made with PR or contact sghongadi@gmail.com 

## License
 * [MIT](LICENSE)