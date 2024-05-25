# Function to read lines from a file and return a set of lines
def read_file_to_set(filename):
    with open(filename, 'r') as file:
        return set(file.readlines())

# Read lines from both files
links = read_file_to_set('links.txt')
links_old = read_file_to_set('links_old.txt')

# Compute the difference between the sets
unique_links = links - links_old

# Write the unique lines to a new file
with open('links_unique.txt', 'w') as file:
    file.writelines(unique_links)
