import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        command = input().split()
        
        if command[0] == "exit":
            sys.exit(0)

        if command[0] == "echo":
            sys.stdout.write(" ".join(command[1:]))    
        else:
            sys.stdout.write(f"{command[0]}: command not found")
    
        sys.stdout.write("\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
