import sys

shell_builtins = {"exit", "echo", "type"}

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        command = input().split()
        
        if command[0] == "exit":
            sys.exit(0)

        if command[0] == "echo":
            sys.stdout.write(" ".join(command[1:]))    
        elif command[0] == "type":
            if command[1] in shell_builtins:
                sys.stdout.write(f"{command[1]} is a shell builtin")
            else:
                sys.stdout.write(f"{command[1]}: not found")
        else:
            sys.stdout.write(f"{command[0]}: command not found")
    
        sys.stdout.write("\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
