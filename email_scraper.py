import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore
import pandas as pd # type: ignore
import json
import re

def fetch_emails(url):
    # Send an HTTP request to the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract all text content from the page
    page_text = soup.get_text()
    
    # Regular expression to find email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Find all matches of the email pattern in the page text
    emails = re.findall(email_pattern, page_text)
    
    # Remove duplicates by converting the list to a set, then back to a list
    emails = list(set(emails))
    
    # Format the results as a list of dictionaries
    data = [{'email': email} for email in emails]
    
    return data

def export_to_csv(data, filename='emails.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data exported to {filename}")

def export_to_json(data, filename='emails.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data exported to {filename}")

def main():
    url = input("Enter the URL to scrape: ")
    data = fetch_emails(url)
    
    if not data:
        print("No emails found. Please check the URL and try again.")
        return
    
    export_format = input("Choose export format (csv/json): ").strip().lower()
    if export_format == 'csv':
        export_to_csv(data)
    elif export_format == 'json':
        export_to_json(data)
    else:
        print("Invalid format selected.")

if __name__ == '__main__':
    main()
