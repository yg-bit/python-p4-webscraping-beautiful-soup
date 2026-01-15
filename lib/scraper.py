from bs4 import BeautifulSoup
import requests

def scrape_flatiron_school():
    """Scrape data from Flatiron School website"""
    headers = {'user-agent': 'my-app/0.0.1'}
    
    # Get the main page
    html = requests.get("https://flatironschool.com/", headers=headers)
    doc = BeautifulSoup(html.text, 'html.parser')
    
    # Find the main heading (structure may have changed)
    main_headings = doc.select('h1')
    print("Main headings found:")
    for heading in main_headings[:3]:  # Show first 3 headings
        text = heading.get_text(strip=True)
        if text:
            print(f"- {text}")
    
    # Find navigation links
    nav_links = doc.select('nav a')
    print(f"\nFound {len(nav_links)} navigation links")
    
    # Get courses page
    courses_html = requests.get("https://flatironschool.com/courses/", headers=headers)
    courses_doc = BeautifulSoup(courses_html.text, 'html.parser')
    
    # Find course-related headings
    course_headings = courses_doc.select('h2, h3')
    print("\nCourse-related content:")
    for heading in course_headings[:5]:  # Show first 5 headings
        text = heading.get_text(strip=True)
        if text and len(text) > 5:  # Filter out very short text
            print(f"- {text}")

def demonstrate_beautiful_soup_methods():
    """Demonstrate key Beautiful Soup methods and concepts"""
    # Create sample HTML for demonstration
    sample_html = """
    <html>
        <head><title>Sample Page</title></head>
        <body>
            <div class="container">
                <h1 id="main-title">Welcome to Web Scraping</h1>
                <p class="intro">This is an introduction to Beautiful Soup.</p>
                <ul class="course-list">
                    <li class="course">Python Programming</li>
                    <li class="course">Web Development</li>
                    <li class="course">Data Science</li>
                </ul>
            </div>
        </body>
    </html>
    """
    
    print("\n=== Beautiful Soup Method Demonstrations ===")
    
    # Parse the HTML
    soup = BeautifulSoup(sample_html, 'html.parser')
    
    # 1. Select by CSS class
    print("\n1. Selecting by CSS class (.intro):")
    intro = soup.select('.intro')[0]
    print(f"Text: {intro.get_text()}")
    
    # 2. Select by ID
    print("\n2. Selecting by ID (#main-title):")
    title = soup.select('#main-title')[0]
    print(f"Text: {title.get_text()}")
    
    # 3. Select multiple elements and iterate
    print("\n3. Selecting multiple elements (.course):")
    courses = soup.select('.course')
    for course in courses:
        print(f"- {course.get_text()}")
    
    # 4. Access tag attributes
    print("\n4. Tag attributes:")
    print(f"Title tag name: {title.name}")
    print(f"Title tag attributes: {title.attrs}")
    
    # 5. Navigate the tree structure
    print("\n5. Tree navigation:")
    container = soup.select('.container')[0]
    print(f"Container has {len(list(container.children))} direct children")

if __name__ == "__main__":
    # Demonstrate Beautiful Soup concepts with sample HTML
    demonstrate_beautiful_soup_methods()
    
    # Scrape actual website (may vary due to site changes)
    print("\n" + "="*50)
    print("LIVE WEBSITE SCRAPING")
    print("="*50)
    scrape_flatiron_school()
