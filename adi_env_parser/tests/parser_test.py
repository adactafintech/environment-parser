from adi_env_parser import EnvironmentParser
from os import environ as env

TEST_DATA_DIR = "adi_env_parser/test_data"


class TestParser:
    def test_parser_empty(self):
        env_prefix = "EMPTY"

        expected = {
            "work_tasks": {
                "task_two": "done"
            },
            "work_inventory": [
                "keyboard"
            ],
            "home": {
                "kitchen_inventory": [
                    "cuttlery",
                    "pots"
                ]
            },
            "games": [
                {
                    "title": "Unfathomable",
                    "publisher": "Fantasy Flight Games"
                },
                {
                    "title": "Cartographers",
                    "publisher": "Thunderworks Games"
                }
            ]
        }

        # Set environment for tests
        env["EMPTY_work_tasks__task_two"] = "done"
        env["EMPTY_work_inventory__0"] = "keyboard"
        env["EMPTY_home__kitchen_inventory__0"] = "cuttlery"
        env["EMPTY_home__kitchen_inventory__1"] = "pots"
        env["EMPTY_games__4__title"] = "Scythe"
        env["EMPTY_games__4__publisher"] = "Stonemaier Games"
        env["EMPTY_games__0__title"] = "Unfathomable"
        env["EMPTY_games__0__publisher"] = "Fantasy Flight Games"
        env["EMPTY_games__1__title"] = "Cartographers"
        env["EMPTY_games__1__publisher"] = "Thunderworks Games"
        env["EMPTY_games__3__title"] = "Anachrony"
        env["EMPTY_games__3__publisher"] = "Mindclash Games"

        parser = EnvironmentParser(env_prefix)
        assert parser.configuration == expected
        print(parser.configuration)

    def test_parser_empty_invalid_key(self):
        env_prefix = "EMPTY2"

        expected = {
            "work_tasks": {
                "task_two": "done"
            },
            "work_inventory": [
                "keyboard"
            ],
            "home": {
                "kitchen_inventory": [
                    "cuttlery",
                    "pots"
                ]
            },
            "games": {
                "invalid_key": "Not valid list key"
            }
        }

        # Set environment for tests
        env["EMPTY2_work_tasks__task_two"] = "done"
        env["EMPTY2_work_inventory__0"] = "keyboard"
        env["EMPTY2_home__kitchen_inventory__0"] = "cuttlery"
        env["EMPTY2_home__kitchen_inventory__1"] = "pots"
        env["EMPTY2_games__invalid_key"] = "Not valid list key"
        env["EMPTY2_games__0__title"] = "Unfathomable"
        env["EMPTY2_games__0__publisher"] = "Fantasy Flight Games"
        env["EMPTY2_games__1__title"] = "Cartographers"
        env["EMPTY2_games__1__publisher"] = "Thunderworks Games"
        env["EMPTY2_games__3__title"] = "Anachrony"
        env["EMPTY2_games__3__publisher"] = "Mindclash Games"

        parser = EnvironmentParser(env_prefix)
        assert parser.configuration == expected
        print(parser.configuration)

    def test_parser_base(self):
        env_prefix = "BASE"

        expected = {
            "work_tasks": {
                "task_one": "done",
                "task_two": "done"
            },
            "work_inventory": [
                "laptop",
                "mouse",
                "keyboard"
            ],
            "home": {
                "garage_inventory": [
                    "tools",
                    "lawnmover"
                ],
                "kitchen_inventory": [
                    "cuttlery",
                    "pots"
                ]
            },
            "games": [
                {
                    "title": "Unfathomable",
                    "publisher": "Fantasy Flight Games"
                },
                {
                    "title": "Cartographers",
                    "publisher": "Thunderworks Games"
                }
            ]
        }

        # Set environment for tests
        env["BASE_work_tasks__task_two"] = "done"
        env["BASE_work_inventory__2"] = "keyboard"
        env["BASE_home__kitchen_inventory__0"] = "cuttlery"
        env["BASE_home__kitchen_inventory__1"] = "pots"
        env["BASE_games__0__title"] = "Unfathomable"
        env["BASE_games__0__publisher"] = "Fantasy Flight Games"
        env["BASE_games__1__title"] = "Cartographers"
        env["BASE_games__1__publisher"] = "Thunderworks Games"

        parser = EnvironmentParser(env_prefix, f"{TEST_DATA_DIR}/base.json")
        assert parser.configuration == expected
