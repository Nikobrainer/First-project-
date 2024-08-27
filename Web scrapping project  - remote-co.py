#!/usr/bin/env python
# coding: utf-8

# In[10]:


### Webscrapping of the job search platform *Remote.co* 
## scrapping cards of the jobs of developpers 


# In[4]:


import requests


# In[5]:


from bs4 import BeautifulSoup


# In[6]:


URL = 'https://remote.co/remote-jobs/developer/'

r = requests.get (URL)


# In[7]:


### Printing the website in html version using the beautiful Soup 


# In[21]:


soup = BeautifulSoup(r.text, 'html.parser')


# In[22]:


print(soup.prettify())


# In[11]:


### Extracting all the cards that hold job position details 


# In[35]:


webpage = soup.find('div', class_= "card-body p-0")
print(webpage)


# In[ ]:


## list all the developer's job positions 


# In[39]:


job_cards = soup.find_all("a", class_= "card m-0 border-left-0 border-right-0 border-top-0 border-bottom") 
for index, jobs in enumerate(job_cards, start=1):
    job_position = jobs.find("span", class_="font-weight-bold larger")
    print(index, job_position.text)


# In[ ]:


### extracting the list of all companies that are positing developpers job offers


# In[61]:


for comp in job_cards:
    firm_name = comp.find('p', class_="m-0 text-secondary")
    firma = firm_name.get_text().split("|")[0]
    print(firma.strip())
                


# In[ ]:


### links to the job offers 


# In[63]:


for links in job_cards:
    print(links["href"])


# In[77]:


for pub in job_cards:
    pubdate = pub.find("span", class_= "float-right d-none d-md-inline text-secondary")
    print(pubdate.text)


# In[83]:


for emp in job_cards:
    typ = emp.find("span", class_="badge badge-success")
    print(typ.text)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


# extract job cards that include information on each develop job offer


# In[113]:


for details in job_cards: 
    job_title = details.find('span', class_= "font-weight-bold larger").text.strip()
    company_info = details.find('p', class_="m-0 text-secondary").get_text(strip=True).split("|")[0].strip()
    emp_type = details.find('span', class_= "badge badge-success").text.strip()
    pub_date =details.find("date").text.strip()
    links = details.get("href")
        
        
    

    if job_title:
        print (f"Job Title : {job_title}")
    if company_info:
        print(f"Company name : {company_info}")
    if emp_type : 
        print(f"employment Type : {emp_type}")
    if pub_date:
        print(f"Publication date : {pub_date}")
    if links:
        print(f"Link : {links}")
        
    print("-"* 40)
              
          


# In[117]:


import pandas as pd


# In[123]:


headers = ["Job_title" , "Company Name", "employment Type", "Publication Date", "Links"]

df = pd.DataFrame(columns = headers)


# In[130]:


job_table  = []

for details in job_cards: 
    job_title = details.find('span', class_= "font-weight-bold larger").text.strip()
    company_info = details.find('p', class_="m-0 text-secondary").get_text(strip=True).split("|")[0].strip()
    emp_type = details.find('span', class_= "badge badge-success").text.strip()
    pub_date =details.find("date").text.strip()
    links = details.get("href")
        
        
    

    if job_title:
        job_table.append(job_title)
    if company_info:
        job_table.append(company_info)
    if emp_type : 
        job_table.append(emp_type)
    if pub_date:
        job_table.append(pub_date)
    if links:
        job_table.append(links)
        


               


# In[131]:


df = pd.DataFrame(job_table, columns=["Job_title", "Company Name", "employment Type", "Publication Date", "Links"])


# In[ ]:


df


# In[132]:


job_table = []

for details in job_cards:
    job_title = details.find('span', class_="font-weight-bold larger").text.strip()
    company_info = details.find('p', class_="m-0 text-secondary").get_text(strip=True).split("|")[0].strip()
    emp_type = details.find('span', class_="badge badge-success").text.strip()
    pub_date = details.find('span', class_="float-right d-none d-md-inline text-secondary").text.strip()  # Corrected this part
    links = details.get("href")
    
    # Append a list containing all the job details as a row
    job_table.append([job_title, company_info, emp_type, pub_date, links])

# Creating a DataFrame
df = pd.DataFrame(job_table, columns=["Job_title", "Company Name", "employment Type", "Publication Date", "Links"])

# Display the DataFrame
print(df)


# In[142]:


import pandas as pd

# Step 1: Initialize an empty list to hold the job data
job_data = []

# Step 2: Loop through each job card and collect the data
job_cards = soup.find_all('a', class_='card m-0 border-left-0 border-right-0 border-top-0 border-bottom')

for job_card in job_cards:
    job_info = {}  # Dictionary to hold job info
    
    job_title = job_card.find('span', class_="font-weight-bold larger")
    pub_date = job_card.find('span', class_="float-right d-none d-md-inline text-secondary")
    company_info = job_card.find('p', class_="m-0 text-secondary")
    emp_type = job_card.find('span', class_="badge badge-success")
    link = job_card.get('href')
    
    if job_title:
        job_info["Job_title"] = job_title.text.strip()
    else:
        job_info["Job_title"] = None
    
    if pub_date:
        job_info["Publication Date"] = pub_date.text.strip()
    else:
        job_info["Publication Date"] = None
    
    if company_info:
        company_name = company_info.get_text(separator=' ', strip=True).split('|')[0].strip()
        job_info["Company Name"] = company_name
    else:
        job_info["Company Name"] = None
    
    if emp_type:
        job_info["employment Type"] = emp_type.text.strip()
    else:
        job_info["employment Type"] = None
    
    if link:
        job_info["Links"] = link
    else:
        job_info["Links"] = None
    
    # Add the job_info dictionary to the job_data list
    job_data.append(job_info)

# Step 3: Create a DataFrame from the list of dictionaries
df = pd.DataFrame(job_data, columns=["Job_title", "Company Name", "employment Type", "Publication Date", "Links"])

# Display the DataFrame
print(df)


# In[143]:


import pandas as pd

# Step 1: Initialize an empty list to hold the job data
job_data = []

# Step 2: Loop through each job card and collect the data
job_cards = soup.find_all('a', class_='card m-0 border-left-0 border-right-0 border-top-0 border-bottom')

for job_card in job_cards:
    job_info = {}  # Dictionary to hold job info
    
    job_title = job_card.find('span', class_="font-weight-bold larger")
    pub_date = job_card.find('span', class_="float-right d-none d-md-inline text-secondary")
    company_info = job_card.find('p', class_="m-0 text-secondary")
    emp_type = job_card.find('span', class_="badge badge-success")
    link = job_card.get('href')
    
    if job_title:
        job_info["Job_title"] = job_title.text.strip()
    else:
        job_info["Job_title"] = None
    
    if pub_date:
        job_info["Publication Date"] = pub_date.text.strip()
    else:
        job_info["Publication Date"] = None
    
    if company_info:
        company_name = company_info.get_text(separator=' ', strip=True).split('|')[0].strip()
        job_info["Company Name"] = company_name
    else:
        job_info["Company Name"] = None
    
    if emp_type:
        job_info["employment Type"] = emp_type.text.strip()
    else:
        job_info["employment Type"] = None
    
    if link:
        job_info["Links"] = link
    else:
        job_info["Links"] = None
    
    # Add the job_info dictionary to the job_data list
    job_data.append(job_info)

# Step 3: Create a DataFrame from the list of dictionaries
df = pd.DataFrame(job_data, columns=["Job_title", "Company Name", "employment Type", "Publication Date", "Links"])

# Display the DataFrame
print(df)


# In[ ]:




