import csv
import sys

def is_empty(mystr):
    return (mystr == None or len(mystr) == 0 or mystr.isspace())

# Check if the user provided a command line argument for the CSV file path
if len(sys.argv) < 2:
    print("Usage: python script.py path_to_your_file.csv")
    sys.exit(1)

# The path to your CSV file is the first command line argument
csv_file_path = sys.argv[1]

try:
    # Open the CSV file and read its contents
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        # Start the HTML output
        html_output = ''
        
        wordcount = 0

        # Loop through each row in the CSV
        for row in reader:
            wordcount += 1

            definition_to_return = ""

            if not is_empty(row['definition']):
                splitted_definition = row['definition'].split(";")

                definition_to_return = splitted_definition[0]

            # Skip esoteric, undefined words
            if wordcount > 5000 and is_empty(row['definition']):
                continue

            # Only generate the first 6500 characters (99.99 percentile)
            if wordcount > 6500:
                break

            # Format each row as an HTML div containing the character, pinyin, and definition
            html_output += f'''
            <div class="character-box">
                <a href="http://hanzidb.org/character/{row['character']}"> <div class="chinese-char">{row['character']}</div> </a>
                <div class="pinyin">{row['pinyin']}</div>
                <div class="english">{definition_to_return}</div>
            </div>'''
            
    # Print the HTML output to the console
    print(html_output)
    
    # Write the HTML output to a file
    output_file_path = 'data/output.html'
    with open(output_file_path, 'w', encoding='utf-8') as htmlfile:
        htmlfile.write(html_output)

except FileNotFoundError:
    print(f"Error: The file '{csv_file_path}' was not found.")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
