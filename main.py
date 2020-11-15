import ssl
from time import sleep
from html.parser import HTMLParser
from http.client import HTTPSConnection

HOST = "www.southparkstudios.com"
conn = HTTPSConnection(HOST, context=ssl._create_unverified_context())


class LinkExtractor(HTMLParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__hrefs = set()

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.__hrefs.add(dict(attrs)["href"])

    @property
    def hrefs(self):
        return self.__hrefs


def get_season_urls(cartmn: HTTPSConnection):
    cartmn.request("GET", "/seasons/south-park")
    parser = LinkExtractor()
    resp = cartmn.getresponse()
    parser.feed(str(resp.read()))
    return (href for href in parser.hrefs if href.startswith("/seasons/south-park/"))


def get_episode_urls(cartmn: HTTPSConnection, season_url: str):
    cartmn.request("GET", season_url)
    parser = LinkExtractor()
    resp = cartmn.getresponse()
    parser.feed(str(resp.read()))
    return (href for href in parser.hrefs if href.startswith("/episodes"))


for url in get_season_urls(conn):
    sleep(1)
    for episode_url in get_episode_urls(conn, url):
        print(episode_url)
