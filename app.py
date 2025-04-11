# app.py
from flask import Flask, render_template, request, redirect, url_for, send_file, session
import pdfkit
import os
import uuid
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'resume_builder_secret_key'

# Create uploads directory if it doesn't exist
if not os.path.exists('static/uploads'):
    os.makedirs('static/uploads')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Get form data
        form_data = {
            'full_name': request.form.get('full_name', ''),
            'job_title': request.form.get('job_title', ''),
            'phone': request.form.get('phone', ''),
            'email': request.form.get('email', ''),
            'linkedin': request.form.get('linkedin', ''),
            'location': request.form.get('location', ''),
            'summary': request.form.get('summary', ''),
            'skills': request.form.getlist('skills'),
            'skills_tech': request.form.getlist('skills_tech'),
            
            # Experience entries
            'company_names': request.form.getlist('company_name'),
            'job_positions': request.form.getlist('job_position'),
            'job_locations': request.form.getlist('job_location'),
            'job_start_dates': request.form.getlist('job_start_date'),
            'job_end_dates': request.form.getlist('job_end_date'),
            'job_descriptions': request.form.getlist('job_description'),
            
            # Education entries
            'institution_names': request.form.getlist('institution_name'),
            'degree_names': request.form.getlist('degree_name'),
            'education_locations': request.form.getlist('education_location'),
            'education_start_dates': request.form.getlist('education_start_date'),
            'education_end_dates': request.form.getlist('education_end_date'),
            
            # Certifications
            'certification_names': request.form.getlist('certification_name'),
            'certification_issuers': request.form.getlist('certification_issuer'),
            'certification_dates': request.form.getlist('certification_date'),
            
            # Interests & Hobbies
            'interests': request.form.getlist('interest'),
            'interest_descriptions': request.form.getlist('interest_description')
        }
        
        # Store data in session
        session['resume_data'] = form_data
        
        # Redirect to preview
        return redirect(url_for('preview', template='template1'))
    
    return render_template('create.html')

@app.route('/preview/<template>')
def preview(template):
    if 'resume_data' not in session:
        return redirect(url_for('create'))
    
    resume_data = session['resume_data']
    
    # Process data to create structured resume
    resume = {
        'personal_info': {
            'full_name': resume_data['full_name'],
            'job_title': resume_data['job_title'],
            'phone': resume_data['phone'],
            'email': resume_data['email'],
            'linkedin': resume_data['linkedin'],
            'location': resume_data['location']
        },
        'summary': resume_data['summary'],
        'skills': {
            'business': resume_data['skills'],
            'technical': resume_data['skills_tech']
        },
        'experience': [],
        'education': [],
        'certifications': [],
        'interests': []
    }
    
    # Process experience entries
    for i in range(len(resume_data['company_names'])):
        if resume_data['company_names'][i]:
            experience = {
                'company': resume_data['company_names'][i],
                'position': resume_data['job_positions'][i],
                'location': resume_data['job_locations'][i],
                'start_date': resume_data['job_start_dates'][i],
                'end_date': resume_data['job_end_dates'][i],
                'description': resume_data['job_descriptions'][i].split('\n')
            }
            resume['experience'].append(experience)
    
    # Process education entries
    for i in range(len(resume_data['institution_names'])):
        if resume_data['institution_names'][i]:
            education = {
                'institution': resume_data['institution_names'][i],
                'degree': resume_data['degree_names'][i],
                'location': resume_data['education_locations'][i],
                'start_date': resume_data['education_start_dates'][i],
                'end_date': resume_data['education_end_dates'][i]
            }
            resume['education'].append(education)
    
    # Process certifications
    for i in range(len(resume_data['certification_names'])):
        if resume_data['certification_names'][i]:
            certification = {
                'name': resume_data['certification_names'][i],
                'issuer': resume_data['certification_issuers'][i],
                'date': resume_data['certification_dates'][i]
            }
            resume['certifications'].append(certification)
    
    # Process interests
    for i in range(len(resume_data['interests'])):
        if resume_data['interests'][i]:
            interest = {
                'name': resume_data['interests'][i],
                'description': resume_data['interest_descriptions'][i]
            }
            resume['interests'].append(interest)
    
    # Store template choice
    session['template_choice'] = template
    
    # Render appropriate template
    template_file = f'{template}.html'
    return render_template(template_file, resume=resume)

@app.route('/download')
def download():
    if 'resume_data' not in session or 'template_choice' not in session:
        return redirect(url_for('create'))
    
    resume_data = session['resume_data']
    template = session['template_choice']
    
    # Process data to create structured resume (same as in preview)
    resume = {
        'personal_info': {
            'full_name': resume_data['full_name'],
            'job_title': resume_data['job_title'],
            'phone': resume_data['phone'],
            'email': resume_data['email'],
            'linkedin': resume_data['linkedin'],
            'location': resume_data['location']
        },
        'summary': resume_data['summary'],
        'skills': {
            'business': resume_data['skills'],
            'technical': resume_data['skills_tech']
        },
        'experience': [],
        'education': [],
        'certifications': [],
        'interests': []
    }
    
    # Process experience entries
    for i in range(len(resume_data['company_names'])):
        if resume_data['company_names'][i]:
            experience = {
                'company': resume_data['company_names'][i],
                'position': resume_data['job_positions'][i],
                'location': resume_data['job_locations'][i],
                'start_date': resume_data['job_start_dates'][i],
                'end_date': resume_data['job_end_dates'][i],
                'description': resume_data['job_descriptions'][i].split('\n')
            }
            resume['experience'].append(experience)
    
    # Process education entries
    for i in range(len(resume_data['institution_names'])):
        if resume_data['institution_names'][i]:
            education = {
                'institution': resume_data['institution_names'][i],
                'degree': resume_data['degree_names'][i],
                'location': resume_data['education_locations'][i],
                'start_date': resume_data['education_start_dates'][i],
                'end_date': resume_data['education_end_dates'][i]
            }
            resume['education'].append(education)
    
    # Process certifications
    for i in range(len(resume_data['certification_names'])):
        if resume_data['certification_names'][i]:
            certification = {
                'name': resume_data['certification_names'][i],
                'issuer': resume_data['certification_issuers'][i],
                'date': resume_data['certification_dates'][i]
            }
            resume['certifications'].append(certification)
    
    # Process interests
    for i in range(len(resume_data['interests'])):
        if resume_data['interests'][i]:
            interest = {
                'name': resume_data['interests'][i],
                'description': resume_data['interest_descriptions'][i]
            }
            resume['interests'].append(interest)
    
    # Render template to HTML string
    template_file = f'{template}.html'
    html_content = render_template(template_file, resume=resume)
    
    # Generate a unique filename
    filename = f"resume_{uuid.uuid4().hex}.pdf"
    output_path = os.path.join('static/uploads', filename)
    
    # Convert HTML to PDF
    pdfkit.from_string(html_content, output_path, options={
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'enable-local-file-access': None
    })
    
    # Return file for download
    return send_file(output_path, as_attachment=True, download_name=f"{resume['personal_info']['full_name'].replace(' ', '_')}_Resume.pdf")

@app.route('/switch_template/<template>')
def switch_template(template):
    return redirect(url_for('preview', template=template))

if __name__ == '__main__':
    app.run(debug=True)