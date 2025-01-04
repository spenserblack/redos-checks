#!/usr/bin/env python3
import json
import os
import re

def main():
    data_path = os.path.join(os.path.dirname(__file__), "..", "redos.json")
    with open(data_path, "r") as f:
        data = json.load(f)

    for catastrophe in data["catastrophes"]:
        re.match(catastrophe["regex"], catastrophe["input"])

    return 0

if __name__ == "__main__":
    import sys

    sys.exit(main())
