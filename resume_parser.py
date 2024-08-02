import json

def parse_resume(resume_text):
    # This is a simplified example. You can enhance it based on your resume format.
    resume_json = {
  "Personal Information": {
    "Name": "John Doe",
    "Email": "john.doe@example.com",
    "Phone": "123-456-7890",
    "Address": "1234 Elm Street, Anytown, USA"
  },
  "Summary": "A brief summary of professional background and key achievements.",
  "Work Experience": [
    {
      "Job Title": "Software Engineer",
      "Company": "Tech Solutions Inc.",
      "Location": "New York, NY",
      "Start Date": "January 2020",
      "End Date": "Present",
      "Responsibilities": [
        "Developed and maintained web applications.",
        "Collaborated with cross-functional teams to define and design new features."
      ]
    },
    {
      "Job Title": "Junior Developer",
      "Company": "Web Innovators LLC",
      "Location": "San Francisco, CA",
      "Start Date": "June 2018",
      "End Date": "December 2019",
      "Responsibilities": [
        "Assisted in the development of client projects.",
        "Performed code reviews and testing."
      ]
    }
  ],
  "Education": [
    {
      "Degree": "Bachelor of Science in Computer Science",
      "University": "State University",
      "Location": "Los Angeles, CA",
      "Graduation Year": "2018"
    }
  ],
  "Skills": [
    "JavaScript",
    "Python",
    "React",
    "Node.js",
    "SQL"
  ],
  "Certifications": [
    {
      "Title": "Certified JavaScript Developer",
      "Issuing Organization": "Tech Certification Board",
      "Year": "2019"
    }
  ],
  "Projects": [
    {
      "Title": "Portfolio Website",
      "Description": "Developed a personal portfolio website to showcase projects and skills.",
      "Technologies": ["HTML", "CSS", "JavaScript"]
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
