# Environment parser

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
