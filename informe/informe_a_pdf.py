from markdown_pdf import MarkdownPdf, Section

with open("informe.md", "r") as file:
    content = file.read()
    pdf = MarkdownPdf(toc_level=2, optimize=True)

    pdf.add_section(Section(content, toc=False))
    
    pdf.meta["title"] = "Modelación Numérica - 25C2 - Bungee Jumping"
    pdf.meta["author"] = "Tomás Cichero y Valeria Brzoza"

    pdf.save("informe.pdf")


