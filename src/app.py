from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from .pdf_generator import generate_pdf
from .database import Database

app = Flask(
    __name__, 
    template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'),
    static_folder=os.path.join(os.path.dirname(__file__), '..', 'static')
)


# Directory for storing generated PDFs
PDF_STORAGE = "generated_pdfs"
os.makedirs(PDF_STORAGE, exist_ok=True)

DB_PATH = "app_data.db"
db = Database(DB_PATH)

# Routes
@app.route('/')
def index():
    return render_template('index.html')   

@app.route('/pdf_templates')
def pdf_templates():
    templates = db.fetch_templates()
    return render_template('pdf_templates.html', templates=templates)

@app.route('/pdf_header_templates')
def pdf_header_templates():
    headers = db.fetch_headers()
    return render_template('pdf_header_templates.html', headers=headers)

@app.route('/pdf_footer_templates')
def pdf_footer_templates():
    footers = db.fetch_footers()
    return render_template('pdf_footer_templates.html', footers=footers)

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        settings_data = request.json
        db.update_settings(settings_data)
        return jsonify({"message": "Settings updated successfully!"})
    else:
        settings = db.fetch_settings()
        return render_template('settings.html', settings=settings)

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf_route():
    try:
        # Extract data from request
        data = request.json
        content = data.get('content')
        header = data.get('header')
        footer = data.get('footer')
        filename = data.get('filename', 'document.pdf')

        # Generate PDF
        file_path = os.path.join(PDF_STORAGE, filename)
        generate_pdf(content=content, header=header, footer=footer, output_path=file_path)

        # Save PDF metadata to database
        db.save_pdf_metadata(filename, file_path)

        return jsonify({"message": "PDF generated successfully!", "file_path": file_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/download_pdf/<filename>')
def download_pdf(filename):
    try:
        return send_from_directory(PDF_STORAGE, filename, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 404

if __name__ == '__main__':
    app.run(debug=False)
