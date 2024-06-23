import sys
import os

from pathlib import Path


shell_builtins = {"exit", "echo", "type"}

def find_command(command):
    PATH = os.environ.get('PATH')
    if PATH is not None:
        paths = PATH.split(":")
        for path in paths:
            dir = Path(path)
            if dir.exists() and dir.is_dir():                       
                for file in Path(path).iterdir():
                    if str(file).endswith(f"/{command}"):
                        return path, str(file)
                    
    return None, None

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
                path, _ = find_command(command[1])
                if path:
                    sys.stdout.write(f"{command[1]} is {path}/{command[1]}")
                else:
                    sys.stdout.write(f"{command[1]}: not found")
        else:
            path, program = find_command(command[0])
            if path:
                is_program = True
                os.system(" ".join([program, *command[1:]]))                
            else:
                sys.stdout.write(f"{command[0]}: command not found")
        if not is_program:
            sys.stdout.write("\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
