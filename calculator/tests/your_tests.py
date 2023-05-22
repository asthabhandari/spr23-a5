#!/usr/bin/env python3
from calculator_adapter import run

### EXAMPLE TESTS
# Checks that the program outputs "7" for an input of "5 + 2"
assert run("5 + 2").output == "7"
# Checks that the program outputs "4" for an input of "2 * 2"
assert run("2 * 2").output == "4"
# Checks that the program exists successfully (no error) for input "2 * 2"
assert run("2 * 2").exit_status == 0
# Checks that the program fails (correctly errors) for input "3 @ 3"
assert run("3 @ 3").exit_status != 0

print("All tests passed!")
