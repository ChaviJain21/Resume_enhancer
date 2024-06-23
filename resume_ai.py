import openai

# Replace 'your-openai-api-key' with your actual OpenAI API key
openai.api_key = 'your-openai-api-key'

def enhance_resume(resume_content, category):
    prompt = f"""
    You are a professional resume writer. Enhance the following resume content for a position in the {category} category. Make it compelling and relevant for the industry.
    
    Resume content:
    {resume_content}
    
    Enhanced resume content:
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.7,
    )

    enhanced_content = response.choices[0].text.strip()
    return enhanced_content

def generate_resume_content(category):
    prompt = f"""
    You are a professional resume writer. Generate compelling resume content for a position in the {category} category. Include sections for professional summary, skills, work experience, and education.
    
    Resume content:
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=600,
        n=1,
        stop=None,
        temperature=0.7,
    )

    new_content = response.choices[0].text.strip()
    return new_content

# Example usage
current_resume = """
John Doe
Software Engineer

Experience:
- Developed web applications using JavaScript, HTML, and CSS
- Collaborated with cross-functional teams to deliver projects on time
- Debugged and optimized code for performance

Skills:
- JavaScript, HTML, CSS
- React, Node.js
- Problem-solving, Teamwork
"""

category = "Software Engineering"

# Enhance existing resume content
enhanced_resume = enhance_resume(current_resume, category)
print("Enhanced Resume Content:")
print(enhanced_resume)

# Generate new resume content
new_resume_content = generate_resume_content(category)
print("\nNew Resume Content:")
print(new_resume_content)

"""Enhance Existing Resume Content:

The enhance_resume function takes the current resume content and the desired job category.
It constructs a prompt to instruct the GPT model to enhance the provided resume content.
The openai.Completion.create function generates the enhanced resume content.
Generate New Resume Content:

The generate_resume_content function takes the desired job category.
It constructs a prompt to instruct the GPT model to create a new resume from scratch.
The openai.Completion.create function generates new resume content based on the category.
Example Usage:

current_resume is a sample resume content.
The category is set to "Software Engineering".
The script then prints both the enhanced and newly generated resume content for demonstration.
Replace 'your-openai-api-key' with your actual API key, and adjust the current_resume and category variables as needed for your specific use case."""