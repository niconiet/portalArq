import dokuwiki
import time
from .credentials import login


class WikiNews:
    def __init__(self, name, last_modified=None, author=None):
        self._name = name
        self._last_modified = last_modified
        self._author = author
        self._url = "http://sisarqwiki.corp.cablevision.com.ar/doku.php?id=soluciones:" + name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def last_modified(self):
        return self._last_modified

    @last_modified.setter
    def last_modified(self, value):
        self.last_modified = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self.author = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


def wiki_news():
    """Returns list of last week WikiNews object"""
    result = []
    wiki = dokuwiki.DokuWiki("http://sisarqwiki.corp.cablevision.com.ar", login["user"], login["password"])
    changes = wiki.pages.changes(int(time.time() - 604800))
    for value in changes:
        print(value["lastModified"])
        if ":" in value["name"]:
            new = WikiNews(name=value["name"].split(":")[-1], last_modified=str(value["lastModified"]).split("T")[0], author=value["author"])
        else:
            new = WikiNews(name=value["name"], last_modified=str(value["lastModified"]).split("T")[0],
                           author=value["author"])
        result.append(new)
    return result

