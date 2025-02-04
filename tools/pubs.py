import csv


def generate_html_from_csv(csv_file, output_html):
    # Start HTML structure
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Publications</title>
    </head>
    <body>
        <h1>Technical Articles</h1>
        <ul>
    """

    # Read the CSV file and add each publication as an <li> item
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            html_content += f"""
            <li>
                <p>{row['Name']}, {row['Publisher']},  {row['Published On']}, <a href="{row['Url']}" 
                target="_blank">Link</a></p>
            </li>
            """

    # End HTML structure
    html_content += """
        </ul>
    </body>
    </html>
    """

    # Write the HTML content to a file
    with open(output_html, 'w', encoding='utf-8') as file:
        file.write(html_content)

    print(f"HTML file '{output_html}' generated successfully.")


generate_html_from_csv('publications.csv', 'publications.html')
