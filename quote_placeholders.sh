#!/bin/bash

TARGET_DIR="${1:-.}"

find "$TARGET_DIR" -type f -name "*.markdown" | while read -r file; do
  echo "Processing $file"

  awk '
    BEGIN { inside_hcl = 0 }

    # Entering fenced hcl code block
    /^\s*```hcl\s*$/ { inside_hcl = 1; print; next }

    # Exiting code block
    /^\s*```/ && inside_hcl == 1 { inside_hcl = 0; print; next }

    # If inside HCL, replace <placeholder> with "placeholder"
    inside_hcl {
      gsub(/<([^">]+)>/, "\"\\1\"")
      print
      next
    }

    # Else, print as is
    { print }

  ' "$file" > "$file.tmp" && mv "$file.tmp" "$file"
done
