import sys
from bs4 import BeautifulSoup
from markdownify import markdownify as md

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py input.html")
        sys.exit(1)

    input_file = sys.argv[1]

    # Read the HTML content from the file
    with open(input_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Attempt to extract the main content
    # Adjust the selectors based on the actual HTML structure
    main_content = soup.find('div', class_='entry-content')
    if not main_content:
        main_content = soup.find('div', id='content')
    if not main_content:
        main_content = soup.body  # Fallback to entire body if specific div not found

    if not main_content:
        print("Main content not found.")
        sys.exit(1)

    # Convert the HTML content to Markdown
    markdown_content = md(str(main_content))

    # Save the Markdown content to a file
    output_file = input_file.rsplit('.', 1)[0] + '.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"Markdown content saved to {output_file}")

if __name__ == '__main__':
    main()