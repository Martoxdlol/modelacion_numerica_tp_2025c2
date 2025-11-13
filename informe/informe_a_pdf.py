import markdown2
import pdfkit
import sys
import os

def markdown_to_pdf(input_path: str, output_path: str):
    """Convert a Markdown file to a PDF file."""
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # Read markdown content
    with open(input_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    # Convert markdown to HTML
    html_content = markdown2.markdown(markdown_content)

    # Convert HTML to PDF
    pdfkit.from_string(html_content, output_path)
    print(f"PDF created successfully at {output_path}")

if __name__ == "__main__":
    markdown_to_pdf('informe.md', 'informe.pdf')