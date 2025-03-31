import pdfplumber

def extract_invoice_data(pdf_path):
    extracted_text = ""
    data = {}

    # Open the PDF
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted_text += page.extract_text()

    # For now, print the whole text to understand structure
    print("PDF CONTENT:")
    print(extracted_text)

    # ➕ Later: We'll add regex or logic to extract specific fields
    return extracted_text

# Run a test
if __name__ == "__main__":
    pdf_file = "../data/sample_invoice.pdf"  # Add your invoice here
    extract_invoice_data(pdf_file)
