from urllib.request import Request, urlopen

from urllib.request import Request, urlopen
import ssl
import re
from urllib.request import Request, urlopen


def answerer(question, a1, a2, a3):
    question = question
    a1 = a1
    a2 = a2
    a3 = a3


def search(term):
    url = "https://www.google.com/search?q={}"
    return http_query(url.format(term))


def http_query(address):
    key = 'User-Agent'
    value = 'Mozilla/5.0'
    req = Request(address, headers={key: value})
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  # Only for gangstars
    web_bin = urlopen(req, context=gcontext).read()
    web_html = web_bin.decode('utf-8')
    return web_html


def get_links(html):
    return re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', html)


def split_results(results):
    pass


def request_pages(url):
    pass


def check_answer():
    pass


def score_answers():
    pass


print(get_links(search('test')))
