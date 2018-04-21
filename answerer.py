from urllib.request import Request, urlopen


def answerer(question, a1, a2, a3):
    question = question
    a1 = a1
    a2 = a2
    a3 = a3


def search(term):
    url = "https://www.google.com/search?q={}"
    req = Request(url.format(term), headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req).read()
    response.decode('utf-8')


def split_results(results):
    pass


def request_pages(url):
    pass


def check_answer():
    pass


def score_answers():
    pass


print(search('test'))
