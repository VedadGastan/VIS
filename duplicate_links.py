def remove_duplicate_lines(file_path):
    try:
        # Read the file and get all lines
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Remove duplicates while preserving order
        seen = set()
        unique_lines = []
        for line in lines:
            if line not in seen:
                unique_lines.append(line)
                seen.add(line)

        # Write the unique lines back to the file
        with open(file_path, 'w') as file:
            file.writelines(unique_lines)

        print(f"Duplicate lines removed successfully from {file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'links.txt'
remove_duplicate_lines(file_path)