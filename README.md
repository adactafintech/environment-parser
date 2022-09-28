# Environment parser

## Requirements

* Python - Minimum required version is 3.8

## Using the environment parser

EnvironmentParser class parses all environment variables with certain prefix and
creates a Python dictionary based on the structure of these variables.

General variable structure rules:

* variable name after prefix should not be empty
* first character of variable name after prefix should not be "_"
* different levels of depth within environment variables are specified by using
  "__" string.
* arrays can be specified by using numeric index as a key within particular level
* array numeric indices should be defined in order, variables with invalid index
  will be discarded

### Using the EnvironmentParser class

Example of instantiating of EnvironmentParser object using `MYPREFIX` as a prefix
for environment variables. Upon instantiation, the object will automatically parse
the current environment variables and store them in its `configuration` property.

```python
import json
from adi_env_parser import EnvironmentParser

parser = EnvironmentParser(prefix="MYPREFIX")
print(json.dump(json.dumps(parser.configuration, indent=4)))
```

It is possible to provide existing JSON formatted file as a configuration base.

```python
import json
from adi_env_parser import EnvironmentParser

parser = EnvironmentParser(prefix="MYPREFIX", config_file="configuration.json")
print(json.dump(json.dumps(parser.configuration, indent=4)))
```

### Examples

Examples use PYENV as environment variable prefix. This is default prefix used
when not specifying one explicitly when instatiating EnvironmentParser.

#### Creating dictionary

Environment variables:

```sh
PYENV_hotel_name="Blue Falcon"
PYENV_rooms__room_1="James Holden"
PYENV_rooms__room_2="Amos Burton"
PYENV_rooms__room_3="Naomi Nagata"
PYENV_rooms__room_4="Alex Kamal"
```

Resulting object:

```json
{
    "hotel_name": "Blue Falcon",
    "rooms": {
        "room_1": "James Holden",
        "room_2": "Amos Burton",
        "room_3": "Naomi Nagata",
        "room_4": "Alex Kamal"
    }
}
```

#### Creating array

Environment variables:

```sh
PYENV_hotel_name="Blue Falcon"
PYENV_room_1__inventory__0="Wardrobe"
PYENV_room_1__inventory__1="Table"
PYENV_room_1__inventory__2="Lamp"
```

Resulting object:

```json
{
    "hotel_name": "Blue Falcon",
    "room_1": {
        "inventory": [
            "Wardrobe",
            "Table",
            "Lamp"
        ]
    }
}
```

#### Dictionaries within list

Environment variables:

```sh
PYENV_hotel_name="Blue Falcon"
PYENV_rooms__0__name="Room 1"
PYENV_rooms__0__capacity="2"
PYENV_rooms__2__name="Room 2"
PYENV_rooms__2__capacity="2"
```

Resulting object:

```json
{
    "hotel_name": "Blue Falcon",
    "rooms": [
        {
            "name": "Room 1",
            "capacity": "2"
        },
        {
            "name": "Room 2",
            "capacity": "2"
        }
    ]
}
```

### Console utility

Module provides console utility which can be used for parsing of environment
variables. It also supports reading of existing JSON formatted file and setting
indentation for output of created configuration JSON object.

```sh
➜ adi-env-parser --help
usage: adi-env-parser -p <prefix> -j <base_json_file>

Parses environment variables with defined prefix and creates JSON output from the parsed structure.

optional arguments:
  -h, --help            show this help message and exit
  --prefix [PREFIX], -p [PREFIX]
                        Environment variable prefix. Default: PYENV
  --json [JSON], -j [JSON]
                        JSON formatted file to read as base configuration
  --indent [INDENT], -i [INDENT]
                        Number of spaces to use for indentation of output JSON string
```

## Development

### Install development packages

```sh
pip install -e ".[dev]"
pip install -e ".[test]
```

### Install pre-commit

```sh
pre-commit install
```
