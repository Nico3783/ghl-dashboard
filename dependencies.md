# Project Dependencies

## Frontend Dependencies

### CSS
1. **Bootstrap** (v5.3.0): For responsive design and components like modals, buttons, and dropdowns.
   ```html
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
   ```

2. **Font Awesome** (v6.0.0): For adding icons to the UI.
   ```html
   <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
   ```

### JavaScript
1. **jQuery** (v3.6.0 - Optional): Simplifies DOM manipulation and event handling.
   ```html
   <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
   ```

2. **Bootstrap JavaScript** (v5.3.0): Provides interactivity for modals, dropdowns, and more.
   ```html
   <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
   ```

---

## Backend Dependencies

1. **Flask**: For serving web pages and handling requests.
2. **FPDF**: For generating PDFs.

### Installing Backend Dependencies
Run the following command in the project directory:
```bash
pip install -r requirements.txt
```

---

## Notes
- Include the CSS `<link>` tags in the `<head>` section of all HTML files.
- Include the JS `<script>` tags at the end of the `<body>` section for all HTML files.
- Ensure internet connectivity for CDN-hosted libraries.
