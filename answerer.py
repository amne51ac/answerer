from urllib import request
import urllib.parse


def answerer(question, a1, a2, a3):
    question = question
    a1 = a1
    a2 = a2
    a3 = a3
    print('what the fuck')


def search(term):
    url = 'https://www.google.com/search?q={}'
    f = request.urlopen(url.format(term))
    return f.read().decode('utf-8')

def split_results(results):
    pass