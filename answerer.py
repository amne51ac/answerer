from urllib.request import Request, urlopen

from urllib.request import Request, urlopen
import ssl

from urllib.request import Request, urlopen


def answerer(question, a1, a2, a3):
    question = question
    a1 = a1
    a2 = a2
    a3 = a3


def search(term):
    url = "https://www.google.com/search?q={}"
    key = 'User-Agent'
    value = 'Mozilla/5.0'
    req = Request(url.format(term), headers={key: value})
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  # Only for gangstars
    web_bin = urlopen(req, context=gcontext).read()
    web_html = web_bin.decode('utf-8')
    return web_html


def split_results(results):
    pass


def request_pages(url):
    pass


def check_answer():
    pass


def score_answers():
    pass


print(search('test'))
