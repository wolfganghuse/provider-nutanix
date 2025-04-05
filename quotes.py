import os
import re

# Function to add quotes around unquoted placeholders
def add_quotes_to_placeholders(content):
    # Regular expression to match placeholders like <uuid>, <username>, etc.
    pattern = r'<([^>]+)>'
    # Replace the placeholders with quoted version
    return re.sub(pattern, r'"\g<1>"', content)

# Function to traverse the directory and process files
def process_files_in_directory(directory):
    # Traverse all files in the given directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        print(f"Processing directory: {root}")
        # Iterate over all files in the current directory
        # and its subdirectories
        for file in files:
            # Process only files with specific extensions (optional)
            print(f"File found: {file}")
            if file.endswith('.markdown'):  # Adjust extensions as needed
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                
                # Read the content of the file
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Add quotes to unquoted placeholders
                new_content = add_quotes_to_placeholders(content)
                
                # Write the modified content back to the file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated file: {file_path}")

# Specify the directory to traverse
directory_to_process = '.work/nutanix/nutanix/website/docs/r'  # Change this to your target directory
process_files_in_directory(directory_to_process)

