import pandas as pd
import requests
from requests.auth import HTTPBasicAuth

df = pd.read_excel('data.xlsx')

def login(username, password):
    login_url = 'https://example.com/login'
    session = requests.Session()
    response = session.post(login_url, auth=HTTPBasicAuth(username, password))
    return session

def get_school(session, member_number):
    search_url = 'https://example.com/search?member_number=' + member_number
    response = session.get(search_url)
    school = response.json()['school']
    return school

session = login('your_username', 'your_password')

df['school'] = df['member_number'].apply(get_school, args=(session,))

df.to_excel('data_with_school.xlsx', index=False)
