import requests
from dotenv import load_dotenv
import os

# 1. GET "PASSWORDS"
load_dotenv()
PROGRAM_ID = os.getenv("program_id")
PROJECT_ID = os.getenv("project_id")

#2. YELP DELETE REQUEST (PRACTICE WITH THIS IN A SANDBOX)""
url = f"https://partner-api.yelp.com/program/{PROGRAM_ID}/portfolio/{PROJECT_ID}/photos/photo_id/v1"
headers = {"accept": "application/json"}
response = requests.delete(url, headers=headers)
print(response.text)

#3. Easy version (Other version for multiple deletes on 1 req is not given on their docu)
photo_id_start = ""
photo_id_stop = ""
### PSEUDO CODE use a [] or a for loop or while loop to delete multiple photos
### for i in range( ASK RONNY!!!
### level Data Analyst 1, use list comprehension