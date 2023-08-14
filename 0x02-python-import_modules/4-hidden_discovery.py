#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Get the list of names defined by the module
    names = dir(hidden_4)

    # Sort the names in alphabetical order
    sorted_names = sorted(name for name in names if not name.startswith("__"))
    # Loop through the names
    for name in sorted_names:
        print(name)
