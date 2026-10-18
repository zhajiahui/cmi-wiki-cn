"""Resolve HTML video attributes relative to the rendered page URL."""
import posixpath
from urllib.parse import urlsplit
from bs4 import BeautifulSoup
from mkdocs.utils import get_relative_url

def on_page_content(html,*,page,config,files):
    if '<video ' not in html:return html
    soup=BeautifulSoup(html,'html.parser')
    for node in soup.find_all(['video','source']):
        for attr in ['src','poster']:
            value=node.get(attr)
            if value and not urlsplit(value).scheme and not value.startswith('/'):
                target=posixpath.normpath(posixpath.join(posixpath.dirname(page.file.src_uri),value))
                node[attr]=get_relative_url(target,page.url)
    return str(soup)
