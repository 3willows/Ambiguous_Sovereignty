import os

def add_css_link(html_file_path, css_file_path):
    """
    Add a link to the CSS file in the given HTML file.

    Parameters:
    html_file_path (str): The path to the HTML file.
    css_file_path (str): The path to the CSS file.
    """
    with open(html_file_path, 'r') as file:
        html_content = file.read()

    # Check if the HTML file already has a <head> tag
    if '<head>' in html_content and '</head>' in html_content:
        head_start = html_content.find('<head>')
        head_end = html_content.find('</head>')
        new_content = html_content[:head_end] + f"<link rel='stylesheet' href='{css_file_path}'>" + html_content[head_end:]
    else:
        # If no <head> tag, add one after <html>
        html_start = html_content.find('<html>')
        if html_start!= -1:
            new_content = html_content[:html_start + 6] + "<head><link rel='stylesheet' href='" + css_file_path + "'></head>" + html_content[html_start + 6:]
        else:
            # If no <html> tag, add basic HTML structure
            new_content = "<html><head><link rel='stylesheet' href='" + css_file_path + "'></head><body>" + html_content + "</body></html>"

    with open(html_file_path, 'w') as file:
        file.write(new_content)

def main():
    # Specify the directory containing HTML files
    html_dir = '.'

    # Specify the path to the CSS file
    css_file_path = 'styles.css'

    # Iterate through all files in the directory
    for filename in os.listdir(html_dir):
        if filename.endswith(".html"):
            html_file_path = os.path.join(html_dir, filename)
            add_css_link(html_file_path, css_file_path)
            print(f"Added CSS link to {filename}")

if __name__ == "__main__":
    main()