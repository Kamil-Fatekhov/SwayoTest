from command_parser import *
import sys

def main():
    try:
        handling()
    except Exception as error:
        print(f"Error: {error}")
        sys.exit(1)

if __name__ == "__main__":
    main()


