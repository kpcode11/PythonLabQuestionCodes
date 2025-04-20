def analyze_log_file(input_file, output_file):
    """
    Analyzes a log file for 'error' occurrences and saves results to a new file
    :param input_file: Path to the log file
    :param output_file: Path to save error information
    """
    error_count = 0
    error_lines = []
    
    try:
        with open(input_file, 'r', encoding='utf-8') as log_file:
            for line_num, line in enumerate(log_file, 1):
                # Case-insensitive search for 'error'
                if 'error' in line.lower():
                    error_count += 1
                    error_lines.append((line_num, line.strip()))
                    
        # Save results to error.txt
        with open(output_file, 'w', encoding='utf-8') as err_file:
            err_file.write(f"Total 'error' occurrences: {error_count}\n")
            err_file.write("=" * 50 + "\n")
            for line_num, line_content in error_lines:
                err_file.write(f"Line {line_num}: {line_content}\n")
                
        print(f"Analysis complete. Found {error_count} errors.")
        print(f"Results saved to {output_file}")
        
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    # File paths
    log_file = 'server.txt'  # Change to your log file path
    error_file = 'error.txt'
    
    print(f"Analyzing log file: {log_file}")
    analyze_log_file(log_file, error_file)

if __name__ == "__main__":
    main()