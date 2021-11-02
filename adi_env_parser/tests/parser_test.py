from adi_env_parser import EnvironmentParser
from os import environ as env

TEST_DATA_DIR = "adi_env_parser/test_data"


class TestParser:
    def test_parser_empty(self):
        env_prefix = "TEST"

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
        env["TEST_work_tasks__task_two"] = "done"
        env["TEST_work_inventory__0"] = "keyboard"
        env["TEST_home__kitchen_inventory__0"] = "cuttlery"
        env["TEST_home__kitchen_inventory__1"] = "pots"
        env["TEST_games__4__title"] = "Scythe"
        env["TEST_games__4__publisher"] = "Stonemaier Games"
        env["TEST_games__0__title"] = "Unfathomable"
        env["TEST_games__0__publisher"] = "Fantasy Flight Games"
        env["TEST_games__1__title"] = "Cartographers"
        env["TEST_games__1__publisher"] = "Thunderworks Games"
        env["TEST_games__3__title"] = "Anachrony"
        env["TEST_games__3__publisher"] = "Mindclash Games"

        parser = EnvironmentParser(env_prefix)
        assert parser.configuration == expected
        print(parser.configuration)

    def test_parser_empty_invalid_key(self):
        env_prefix = "TEST2"

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
        env["TEST2_work_tasks__task_two"] = "done"
        env["TEST2_work_inventory__0"] = "keyboard"
        env["TEST2_home__kitchen_inventory__0"] = "cuttlery"
        env["TEST2_home__kitchen_inventory__1"] = "pots"
        env["TEST2_games__invalid_key"] = "Not valid list key"
        env["TEST2_games__0__title"] = "Unfathomable"
        env["TEST2_games__0__publisher"] = "Fantasy Flight Games"
        env["TEST2_games__1__title"] = "Cartographers"
        env["TEST2_games__1__publisher"] = "Thunderworks Games"
        env["TEST2_games__3__title"] = "Anachrony"
        env["TEST2_games__3__publisher"] = "Mindclash Games"

        parser = EnvironmentParser(env_prefix)
        assert parser.configuration == expected
        print(parser.configuration)

    def test_parser_empty_invalid_prefixes(self):
        env_prefix = "TEST3"

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
            }
        }

        # Set environment for tests
        env["TEST3"] = "just base of prefix"
        env["TEST3_"] = "just prefix"
        env["TEST3__"] = "prefix with additional underline"
        env["TEST3__not_valid"] = "prefix with additional underline and " \
            "key word"
        env["TEST3_work_tasks__task_two"] = "done"
        env["TEST3_work_inventory__0"] = "keyboard"
        env["TEST3_home__kitchen_inventory__0"] = "cuttlery"
        env["TEST3_home__kitchen_inventory__1"] = "pots"

        parser = EnvironmentParser(env_prefix)
        assert parser.configuration == expected
        print(parser.configuration)

    def test_parser_empty_underscore_key(self):
        env_prefix = "TEST4"

        expected = {
            "employee": {
                "surname": "Smith"
            },
            "work_task_one": "done"
        }

        # Set environment for tests
        env["TEST4_employee___name"] = "John"
        env["TEST4_employee__surname"] = "Smith"
        env["TEST4_work_task_one"] = "done"

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
