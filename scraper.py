import requests
from bs4 import BeautifulSoup
import json

def get_citations_needed_count(url):
    """
    Retrieves a Wikipedia page and counts the number of citations needed.

    Args:
        url (str): The URL of the Wikipedia page.

    Returns:
        int: The number of citations needed.

    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citation_needed_tags = soup.find_all('sup' , class_='noprint Inline-Template Template-Fact')
    return len(citation_needed_tags)

def get_citations_needed_report(url):
    """
    Retrieves a Wikipedia page and generates a report of passages that need citations.

    Args:
        url (str): The URL of the Wikipedia page.

    Returns:
        list: A list of text statements for each citation.

    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citation_needed_tags = soup.find_all('sup' , class_='noprint Inline-Template Template-Fact')
    statements = " "

    for citation in citation_needed_tags:
        statement = citation .find_previous('p')
        # statements.append(statement.text)
        statements += statement.text

    return statements

url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
count = get_citations_needed_count(url)
statements = get_citations_needed_report(url)


print(f"Number of citations needed: {count}")
print("Citations needed report:")
print(statements)

# report = {
#     "number_of_citations_needed": count,
#     "citations": statements
# }

# with open('report.json', 'w') as file:
#     json.dump(report, file)

# print(json.dumps(report, indent=4))
