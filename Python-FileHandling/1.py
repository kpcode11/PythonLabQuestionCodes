import os
from pathlib import Path

def approach_1_read():
    """Approach 1: Using read() method"""
    print("\n=== Approach 1: Using read() ===")
    try:
        with open('user_file.txt', 'r') as file:
            content = file.read()
        print("File content:")
        print(content)
    except FileNotFoundError:
        print("File not found. Please create the file first using Approach 3.")

def approach_2_readlines():
    """Approach 2: Using readlines() method"""
    print("\n=== Approach 2: Using readlines() ===")
    try:
        with open('user_file.txt', 'r') as file:
            lines = file.readlines()
        print("File content (line by line):")
        for i, line in enumerate(lines, 1):
            print(f"Line {i}: {line.strip()}")
    except FileNotFoundError:
        print("File not found. Please create the file first using Approach 3.")

def approach_3_pathlib():
    """Approach 3: Using pathlib (create file and read)"""
    print("\n=== Approach 3: Using pathlib ===")
    print("Enter your file content (press Enter on an empty line to finish):")
    content_lines = []
    while True:
        line = input()
        if line == "":
            break
        content_lines.append(line + "\n")  # Add newline character
    
    # Write to file using pathlib
    file_path = Path('user_file.txt')
    file_path.write_text(''.join(content_lines))
    print(f"File saved to: {file_path.absolute()}")
    
    # Read back using pathlib
    print("\nFile content from pathlib:")
    print(file_path.read_text())

def main():
    while True:
        print("\n=== File Content Reader ===")
        print("1. Display using read()")
        print("2. Display using readlines()")
        print("3. Create file and read using pathlib")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            approach_1_read()
        elif choice == '2':
            approach_2_readlines()
        elif choice == '3':
            approach_3_pathlib()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()