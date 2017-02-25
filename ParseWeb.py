import urllib2
from bs4 import BeautifulSoup

class Client(object):

    def get_web(self, page):
        """ download web """
        f = urllib2.urlopen(page)
        html = f.read()
        f.close()
        return html

    def search_text(self, html):
        """ Get the title of the book  """
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.find("div", class_="dotd-title").find("h2")
        return elements.get_text().strip()

    def main(self, website):
        web = self.get_web(website)
        resultat = self.search_text(web)
        return resultat
