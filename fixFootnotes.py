from bs4 import BeautifulSoup
import os

# Function to update href attributes in an HTML file
def update_href(file_path):
    with open(file_path, 'r+', encoding='utf-8') as file:
        html_content = file.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        for link in soup.find_all('a', href="#Fn5"):
            link['href'] = "./section9/#Fn5"
        file.seek(0)
        file.write(str(soup))
        file.truncate()

# Directory containing your HTML files
html_dir = '.'

# Iterate through all HTML files in the directory
for filename in os.listdir(html_dir):
    if filename.endswith(".html"):
        file_path = os.path.join(html_dir, filename)
        update_href(file_path)
        print(f"Updated {filename}")