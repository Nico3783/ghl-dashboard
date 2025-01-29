from fpdf import FPDF

def generate_pdf(content, header, footer, output_path):
    """
    Generates a PDF with the given content, header, and footer.

    Args:
        content (str): The main content of the PDF.
        header (str): The header text to include in the PDF.
        footer (str): The footer text to include in the PDF.
        output_path (str): The file path where the PDF will be saved.

    Returns:
        None
    """
    try:
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)

        # To add a new page
        pdf.add_page()

        # Setting a header
        if header:
            pdf.set_font("Arial", size=12)
            pdf.cell(0, 10, header, ln=True, align='C')

        # Adding some contents
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, content)

        # Set footer
        if footer:
            pdf.set_y(-20)
            pdf.set_font("Arial", size=10)
            pdf.cell(0, 10, footer, ln=False, align='C')

        # Output PDF
        pdf.output(output_path)

    except Exception as e:
        raise Exception(f"Error generating PDF: {e}")
