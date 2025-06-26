import requests
from bs4 import BeautifulSoup
import json
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

#data retrived from Investopedia
urls = [
    "https://www.investopedia.com/terms/r/rothira.asp",
    "https://www.investopedia.com/terms/1/401kplan.asp",
    "https://www.investopedia.com/terms/c/creditscore.asp"
]

def extract_text_func(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser') #this gets the raw bytes of the html of the website

    #retrive all the paragraphs in the main content section
    paragraphs = soup.find_all('p')

    #specific for investopedia articles
    '''
    This narrows the text to the main content. Investopedia articles house 
    the main content within the base class 'mntl-sc-block'
    '''
    filtered = [p for p in paragraphs if 'mntl-sc-block' in p.get('class', [])]

    #this joins the clean text into arrays of strings.
    text = "\n".join([p.get_text() for p in filtered])
    return text

def chunk_text(text, max_words = 100):
    sentences = sent_tokenize(text=text)
    chunks = []
    current_chunk = []

    for sentence in sentences:
        words = sentence.split()
        if len(current_chunk) + len(words) <= max_words:
            current_chunk.extend(words)
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = words
    
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
    
