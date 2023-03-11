



import requests # to get the html page on linkedin
from bs4 import BeautifulSoup # to parse the html page



linkedin_data = requests.get('https://www.linkedin.com/jobs/search/?keywords=data%20engeering') # get the html page

soup = BeautifulSoup(linkedin_data.text, 'lxml') # parse the html page

jobs_cards = soup.find_all('div', class_ = 'base-card')
#print(jobs_cards)


def job_info(job_card):
    job_title = job_card.find('h3', class_ = 'base-search-card__title').text


    job_company = job_card.find('h4', class_ = 'base-search-card__subtitle').text
    job_location = job_card.find('span', class_ = 'job-search-card__location').text
    job_link = job_card.find('a', class_ = 'base-card__full-link')['href']
    
    #get rid of spaces  
    job_title = job_title.strip()
    job_company = job_company.strip()
    job_location = job_location.strip()
    job = {
        'title': job_title,
        'company': job_company,
        'location': job_location,
        'link': job_link
    }
    return job

def get_jobs():
    jobs = []
    for job_card in jobs_cards:
        job = job_info(job_card)
        jobs.append(job)
    return jobs



Get_Jobs = get_jobs()

