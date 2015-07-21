# dobrochan pic downloader

import re

def find_pics(text):
    dobr_re = re.compile('Файл: <a href="(/src/.*?)" target="_blank">.*?</a>')
    dobr_pref = 'http://dobrochan.com'
    lst_ = dobr_re.findall(text)
    
    lst = []
    for url in lst_:
        lst.append('%s%s'%(dobr_pref, url))

    return lst

def save_pics(lst, url):
    with open('pics.txt', 'w') as pic_f:
        for line in lst:
            pic_f.write('%s\n'%(line))

def get_pics(url):
    text = get_html(url)
    pics = find_pics(text)
    save_pics(pics, url)

if __name__ == '__main__':
    #get_pics('http://dobrochan.com/a/res/710182.xhtml')
    get_pics('http://dobrochan.com/a/res/692138.xhtml')
