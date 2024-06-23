import sys
import os

from pathlib import Path


shell_builtins = {"exit", "echo", "type", "pwd", "cd"}

def find_command(command):
    paths = os.environ.get('PATH') or ""    
    for path in map(lambda s: f"{s}/{command}", paths.split(":")):
        if Path(path).exists():
            return path
                    
    return None

def main():
    
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        command = input().split()
        is_program = False
        
        if command[0] == "exit":
            sys.exit(0)

        if command[0] == "echo":
            sys.stdout.write(" ".join(command[1:]))    
        elif command[0] == "type":
            if command[1] in shell_builtins:
                sys.stdout.write(f"{command[1]} is a shell builtin")
            else:
                path = find_command(command[1])
                if path:
                    sys.stdout.write(f"{command[1]} is {path}")
                else:
                    sys.stdout.write(f"{command[1]}: not found")
        elif command[0] == "pwd":
            sys.stdout.write(os.getcwd())
        elif command[0] == "cd":
            path = Path(command[1])
            if path.exists() and path.is_dir():
                is_program = True
                os.chdir(command[1])
            else:
                sys.stdout.write(f"{command[0]}: {command[1]}: No such file or directory")
        else:
            program = find_command(command[0])
            if program:
                is_program = True
                os.system(" ".join([program, *command[1:]]))                
            else:
                sys.stdout.write(f"{command[0]}: command not found")
        if not is_program:
            sys.stdout.write("\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
