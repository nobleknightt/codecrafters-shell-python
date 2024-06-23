import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        command = input().split()
        if command[0] == "exit":
            sys.exit(0)

        sys.stdout.write(f"{command[0]}: command not found\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
