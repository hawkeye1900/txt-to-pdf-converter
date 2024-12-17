from pathlib import Path
import glob
from fpdf import FPDF

# Create a single pdf document
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Extract all relevant filepath names and save to a list
filepaths = glob.glob("resources/*.txt")

# Iterate over the list of filepaths
for filepath in filepaths:
    # Add one page to pdf for each text file
    pdf.add_page()

    # Extract the file name only, from full filepath
    filename = Path(filepath).stem.title()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=50, h=12, txt=f"{filename}", align="L", ln=1,
             border=0)

    # Get the content of each text file
    with open(filepath, "r") as text:
        content = text.read()
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("animals.pdf")
