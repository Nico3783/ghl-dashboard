# GHL Dashboard - Letter of Intent (LOI) Generator

## Overview
This project is a **Flask-based web application** that automates the creation, customization, and management of **Letters of Intent (LOI)** in PDF format. It provides a dashboard where users can generate LOIs based on property details, modify headers and footers, and track submissions.

## Features
- 📄 **PDF Generation**: Automatically calculates offer price and generates PDFs.
- ✏️ **Customizable Templates**: Users can edit LOI content, headers, and footers.
- 📤 **Direct Sending**: Send LOIs to contacts via email.
- 📂 **Database Integration**: Saves generated LOIs for future reference.
- 🌐 **Fully Deployable**: Works with **Render, GoDaddy, or VPS hosting**.

## Tech Stack
- **Backend**: Flask, Gunicorn
- **Frontend**: HTML, CSS, JavaScript (Bootstrap)
- **Database**: SQLite
- **PDF Generation**: FPDF

## Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Nico3783/ghl-dashboard.git
   cd ghl-dashboard
   ```
2. **Create a Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Application**
   ```bash
   python src/app.py
   ```
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Deployment to Render
1. Push your project to **GitHub**.
2. Sign in to **Render** and create a **new Web Service**.
3. Connect your repository and set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn src.app:app`
4. Deploy and get your **public URL**.

## API Endpoints
| Method | Endpoint           | Description          |
|--------|-------------------|----------------------|
| GET    | `/`               | Home Page           |
| GET    | `/pdf_templates`  | View PDF Templates  |
| POST   | `/generate_pdf`   | Generate LOI PDF    |
| GET    | `/download_pdf/<filename>` | Download PDF |

## Contribution
Feel free to fork and contribute! Create a PR with detailed documentation for any feature added.

## License
MIT License © 2025 Nico3783