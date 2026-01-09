from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')

# Try to find the heading-financier element
heading_elements = doc.select('.heading-financier')
print(f"Found {len(heading_elements)} elements with .heading-financier")

if heading_elements:
    print(heading_elements[0].contents)
    print(heading_elements[0].contents[0].strip())
else:
    print("No elements found with .heading-financier class")

# Example of scraping courses from the courses page
print("\n--- Scraping courses ---")
courses_html = requests.get("https://flatironschool.com/our-courses/", headers=headers)
courses_doc = BeautifulSoup(courses_html.text, 'html.parser')

courses = courses_doc.select('.heading-60-black.color-black.mb-20')
print(f"Found {len(courses)} course elements")

for course in courses:
    if course.contents:
        print(course.contents[0].strip())
