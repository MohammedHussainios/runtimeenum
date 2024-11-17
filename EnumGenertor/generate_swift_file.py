import os

def generate_swift_from_file(input_file, output_file, enum_name):
    # Read values from the file
    values = {}
    with open(input_file, "r") as file:
        for line in file:
            line = line.strip()
            if line.endswith(";"):
                line = line[:-1]  # Remove the trailing semicolon
            if "=" in line:
                key, value = line.split("=")
                key = key.strip().strip("\"")  # Remove whitespace and quotes
                values[key] = value

    # Generate Swift code
    swift_code = f"""
// {output_file}

import Foundation

enum {enum_name}: String {{
"""
    for key, value in values.items():
        swift_code += f"    case {key} = \"{key}\" \n"

    swift_code += f"""\
}}
""".replace("{enum_name}", enum_name)

    # Write to the Swift file
    with open(output_file, "w") as file:
        file.write(swift_code)

    print(f"{output_file} generated successfully!")

if __name__ == "__main__":
    # Automatically detect the script's directory
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Define input and output file paths relative to the script's directory
    input_file = os.path.join(script_dir, "en.lproj/Localizable-en.strings")
    output_file = os.path.join(script_dir, "ExampleEnum.swift")
    enum_name = "ExampleEnum"  # You can change this as needed

    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        print("Please create 'Localizable-en.string' in the same directory as this script.")
        exit(1)

    # Generate the Swift file
    generate_swift_from_file(input_file, output_file, enum_name)
