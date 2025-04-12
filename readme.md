
# ResumeCraft - Easy PDF Resume Builder

![ResumeCraft Banner](https://via.placeholder.com/1200x300/0d6efd/ffffff?text=ResumeCraft+Easy+PDF+Resume+Builder)

## 📝 Overview

ResumeCraft is a powerful yet simple web application that allows users to create professional resumes with ease. Built with Flask, the application provides an intuitive form-based interface to input resume details and generates beautifully formatted PDF resumes from multiple templates.

## ✨ Features

- **User-friendly Form Interface**: Easy-to-use form to input all your resume details
- **Multiple Templates**: Choose from various professional resume templates
- **Real-time Preview**: Preview your resume before downloading
- **PDF Generation**: Download your resume as a professional PDF document
- **Section Management**: Add multiple entries for experience, education, certifications, and interests
- **Responsive Design**: Works on desktop and mobile devices

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **PDF Generation**: pdfkit (wkhtmltopdf)
- **Session Management**: Flask Session

## 🚀 Installation & Setup

### Prerequisites

- Python 3.6+
- pip (Python package installer)
- wkhtmltopdf (for PDF generation)

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/resumecraft.git
cd resumecraft
```

### Step 2: Set up a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### Step 3: Install required Python packages

```bash
pip install flask pdfkit
```

### Step 4: Install wkhtmltopdf

#### On Ubuntu/Debian:
```bash
sudo apt-get install wkhtmltopdf
```

#### On macOS:
```bash
brew install wkhtmltopdf
```

#### On Windows:
Download the installer from [wkhtmltopdf official website](https://wkhtmltopdf.org/downloads.html) and add it to your PATH.

### Step 5: Run the application

```bash
python app.py
```

The application will be available at `http://localhost:5000/`.

## 📋 Usage

1. **Start**: Visit the homepage and click "Create Resume"
2. **Fill Form**: Complete the resume form with your personal information, experiences, education, etc.
3. **Preview**: Review your resume with the default template
4. **Switch Templates**: Try different templates to find your preferred style
5. **Download**: Download your resume as a PDF file

## 🏗️ Project Structure

```
resumecraft/
│
├── app.py                 # Main Flask application
├── static/                # Static files (CSS, JS, images)
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript files
│   └── uploads/           # Generated PDFs (temporary storage)
│
├── templates/             # HTML templates
│   ├── index.html         # Homepage
│   ├── create.html        # Resume form page
│   ├── template1.html     # Resume template 1
│   ├── template2.html     # Resume template 2
│   └── ...                # Additional templates
│
└── README.md              # Project documentation
```

## 🔍 Key Components

### Routes

- **/ (index)**: Homepage
- **/create**: Form to input resume details
- **/preview/<template>**: Preview resume with specified template
- **/download**: Generate and download PDF resume
- **/switch_template/<template>**: Switch between different templates

### Data Structure

The application uses a structured JSON format to organize resume data:

```python
resume = {
    'personal_info': { ... },
    'summary': '...',
    'skills': { ... },
    'experience': [ ... ],
    'education': [ ... ],
    'certifications': [ ... ],
    'interests': [ ... ]
}
```

## 🔧 Customization

### Adding New Templates

1. Create a new HTML template in the templates directory (e.g., `template3.html`)
2. Use the existing templates as a reference for the data structure
3. Design your template using HTML and CSS
4. The new template will be automatically available in the application

### Modifying Fields

To add or modify resume fields:
1. Update the form in `create.html`
2. Modify the data processing in the `/create` route in `app.py`
3. Update the templates to display the new fields

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📬 Contact

Your Name - [your.email@example.com](mailto:your.email@example.com)

Project Link: [https://github.com/your-username/resumecraft](https://github.com/your-username/resumecraft)

---

Made with ❤️ by [Your Name]
