#Leonardo Alvarado -1949295
import requests
from bs4 import BeautifulSoup
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
    )
python_jobs_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
    ]
for job_element in python_jobs:
    tittle_element = job_element.find("h2", class_="tittle")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    links_url = job_element.find_all("a")[1]["href"]
    print(company_element.text.strip())
    print(location_element.text.strip())
    print(tittle_element.text.strip())
    print(f"Apply Here: {link_url}\n")
    print()
