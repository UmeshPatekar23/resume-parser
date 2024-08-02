import json

def parse_resume(resume_text):
    # This is a simplified example. You can enhance it based on your resume format.
    resume_json = {
        "Personal Information": {
            "Name": "John Doe",
            "Contact": {
                "Email": "john.doe@example.com",
                "Phone": "123-456-7890"
            },
            "Address": "123 Main St, Anytown, USA"
        },
        "Education": [
            {
                "Degree": "B.Sc. in Computer Science",
                "Institution": "University of Example",
                "Year": "2020"
            }
        ],
        "Work Experience": [
            {
                "Job Title": "Software Engineer",
                "Company": "Tech Solutions",
                "Duration": "2020-2023",
                "Responsibilities": "Developed software solutions, collaborated with teams, etc."
            }
        ],
        "Skills": [
            "Python", "Java", "Machine Learning"
        ],
        "Certifications": [
            {
                "Certification": "Certified AI Specialist",
                "Institution": "AI Institute",
                "Year": "2021"
            }
        ]
    }
    return json.dumps(resume_json, indent=4)

# Example usage
resume_text = """
[Insert Resume Text Here]
"""
parsed_resume = parse_resume(resume_text)
print(parsed_resume)
