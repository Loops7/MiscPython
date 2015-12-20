import requests
import re
from lxml import html
from lxml.cssselect import CSSSelector
from contextlib import closing
import shutil
import os
#
API_KEY = 'AIzaSyAls-wjly8Mtf0qoXPzYo9e37HB5Eatoqo'
"""
f = open('headlines.txt', 'w+')
u = requests.get("http://nytimes.com")
tree = html.fromstring(u.text)
sel = CSSSelector('h2.story-heading, h3.story-heading, h2.story-heading a, h3.story-heading a')
lis = sel(tree)
clean = [x.text.strip() for x in lis if x.text is not None and x.text.strip()[:-1]]
for c in clean:
    print >> f, c.encode('utf8')

f.close()

url = 'http://www.bigboobguide.com/blog/wp-content/uploads/2011/12/gianna-michaels-12-tits-of-christmas-2011.jpg'
out_file = open('pic.jpg', 'wb')
with closing(requests.get(url, stream=True)) as r:
    shutil.copyfileobj(r.raw, out_file)
"""
"""
AH_URL = 'http://bbs.hitechcreations.com/smf/index.php/topic,359280.0.html'
cwd = os.getcwd()
IMAGES_DIR = os.path.join(cwd, 'AHimages/')
if not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)
       
payload = {
    'user': 'TonyJoey',
    'passwrd': 'moorhouse'
}


with requests.Session() as s:
    s.post('http://bbs.hitechcreations.com/smf/index.php?action=login2', data=payload)

    r = s.get(AH_URL)
    
    tree = html.fromstring(r.text)
    sel = CSSSelector('img')
    images = sel(tree)
    
    num = 1
    for img in images:
        f = open(IMAGES_DIR +'AH-img'+ str(num) +'.jpg', 'wb')
        url = img.get('src')
        with closing(requests.get(url, stream=True)) as r:
            shutil.copyfileobj(r.raw, f)
        num +=1
"""
AH_URL = 'http://www.pornhub.com/'
cwd = os.getcwd()
IMAGES_DIR = os.path.join(cwd, 'images/')
if not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)
r = requests.get(AH_URL)
    
tree = html.fromstring(r.text)
sel = CSSSelector('img')
images = sel(tree)
    
num = 1
for img in images:
    f = open(IMAGES_DIR +'img'+ str(num) +'.jpg', 'wb')
    
    url = img.get('data-smallthumb') if img.get('data-smallthumb') else img.get('src')
    
    print url
    with closing(requests.get(url, stream=True)) as r:
        shutil.copyfileobj(r.raw, f)
    num +=1         
        