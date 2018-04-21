from urllib import request, parse


def answerer(question, a1, a2, a3):
    question = question
    a1 = a1
    a2 = a2
    a3 = a3
    print('what the fuck')


def search(term):
    url = 'http://www.google.com/search?q={}'
    with request.urlopen(url.format(term)) as f:
        return f.read().decode('utf-8')

def split_results(results):
    pass

def request_pages(url):
    pass

def check_answer():
    pass

def score_answers():
    pass

print(search('test'))

