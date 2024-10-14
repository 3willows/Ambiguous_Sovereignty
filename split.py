from bs4 import BeautifulSoup
import os

def split_by_h2(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all H2 tags
    h2_tags = soup.find_all('h2')
    
    # Create a list to store section content
    sections = []
    
    # Extract content between H2 tags
    for i in range(len(h2_tags)):
        start = h2_tags[i]
        end = h2_tags[i+1] if i+1 < len(h2_tags) else None
        
        section_content = []
        for sibling in start.next_siblings:
            if sibling == end:
                break
            section_content.append(str(sibling))
        
        sections.append({
            'title': start.text,
            'content': ''.join(section_content)
        })
    
    return sections

def create_html_files(sections):
    # Create index.html
    index_content = "<h1>Table of Contents</h1>\n<ul>"
    for i, section in enumerate(sections):
        filename = f"section_{i+1}.html"
        index_content += f'<li><a href="{filename}">{section["title"]}</a></li>'
    index_content += "</ul>"
    
    with open("index.html", "w") as f:
        f.write(index_content)
    
    # Create individual section files
    for i, section in enumerate(sections):
        filename = f"section_{i+1}.html"
        content = f"<h2>{section['title']}</h2>\n{section['content']}\n<p><a href='index.html'>Back to Table of Contents</a></p>"
        
        with open(filename, "w") as f:
            f.write(content)

# Read the input HTML file
with open("index.html", "r") as f:
    html_content = f.read()

# Split the content by H2 tags
sections = split_by_h2(html_content)

# Create HTML files
create_html_files(sections)

print("HTML files created successfully!")