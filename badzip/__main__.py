import os
import sys

from pathlib import Path
from importlib.resources.abc import Traversable
from importlib.resources import files

PATH = files(__name__)

def main() -> None:

    if len(sys.argv) != 2:
        sys.exit(f"USAGE: {sys.argv[0]} <processcount>")

    pcount = int(sys.argv[1])

    children = []
    try:
        for i in range(pcount):
            if child := os.fork():
                children.append(child)
                del child
            else:
                children = []
                del child
                break

        for i in range(10000):
            for f in PATH.iterdir():
                if f.is_file():
                    f.read_bytes()
    finally:
        for child in children:
            print(os.waitpid(child, 0))

if __name__ == "__main__":
    main()
