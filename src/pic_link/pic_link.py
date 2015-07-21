import re
import os

## extracting direct picture links from html webpages
## full-size pictures only, not thumbnail images!
##
## supported:
## abload.de
## flickr.com
## bayimg.com
##
## just put .html files into one folder with program and run
## it creates %htmlfilename%_links.txt file with direct links to pics

# if you want save links from all .html files in one large .txt file switch to True
# if you want save links for each .html file in separate .txt file switch to False
ONE_FILE = True

def extract(text):
    extracted_pics = []
    regex_lst = (
        ##abload
        # example
        #"http://abload.de/img/bbd12a92d3407d857f536wgq1d.jpg"
        '"(http://abload.de/img/.*?[.].{3,4})"',
        
        ##flickr
        # example
        #'http://farm8.staticflickr.com/7562/16066039928_a060372f66_o.jpg',
        "'(http://farm\d{1,}[.]staticflickr[.]com/\d{4}/\d*?_.*?_o[.].{3,4})'",
        
        ##bayimg
        # example
        #"http://image.bayimg.com/457db6fab7283798721101fbf5897d9fd6b150a1.jpg"
        '"(http://image[.]bayimg[.]com/.*?[.].{3,4})"',
        
        ##vk.com (pictures on the wall), but cannot extract gif urls
        # examples
        #<img src="http://cs14110.vk.me/c7008/v7008985/49103/H62hkPsDN9k.jpg"
        #<img src="http://cs540108.vk.me/v540108985/73d0/b3P4ktpCvxY.jpg"
#        '<img src="(http[:]//cs\d*?[.]vk[.]me(?:/[c]\d*?){0,1}/[v]\d*?/.*?/.*?[.](?:jpg|png))"',
        
        ##vk.com gif docpages (not real .gif direct links)
        # examples
        #<a href="/doc148898272_202039868?hash=cc6163f293290abb68&dl=f2db9b209c751e987f"
        #'<a href="(/doc\d*?_\d*?[?]hash=.*?[&]dl=.*?)"',
        )

    #uniq = {}
    #uniq2 = []
    for regex in regex_lst:
        lst = re.compile(regex).findall(text)

        uniq = list(set(lst))
        # unique check
     #   for item in lst:
      #      if item not in uniq2:
       #         uniq2.append(item)
        #    uniq[item] = 1
        
        #extracted_pics.extend(uniq.keys())
        extracted_pics.extend(uniq)
        
    return extracted_pics

def process_file(file_fullpath):
        enc = 'utf-8'
        try:
            with open(file_fullpath, encoding=enc) as f:
                text = f.read()
        except UnicodeDecodeError:
            enc = 'cp1251'
            with open(file_fullpath, encoding=enc) as f:
                text = f.read()
                
        #text = text.decode(enc, errors='replace')
        
        links = extract(text)
        return links


def find_pics(path, files):
    links_all = []

    total_files = len(files)
    i = 0
    for html_file in files:
        file_fullpath = os.path.join(path, html_file)
        i += 1
        links = process_file(file_fullpath)
        
        percent = round(i / total_files * 100, 4)
        print('%s : %s links [%s'%(html_file, len(links), percent), '%]')

        if not ONE_FILE:
            links_filepath = os.path.join(path, html_file + '_links.txt')
            save_links(links, links_filepath)
        else:
            links_all.extend(links)
            #save_links(links_all, 'LINKS_ALL.txt')

    if ONE_FILE:
        links_all_uniq = list(set(links_all))
        save_links(links_all_uniq, 'LINKS_ALL.txt')

def save_links(links, filename):
    with open(filename, 'w') as lf:
        for link in links:
            lf.write('%s\n'%link)    


def curr_dir():
    dir_ = os.path.abspath(os.curdir)
    dir_items = os.listdir(dir_)

    html_files = list(filter(lambda f: f.endswith('.htm') or f.endswith('.html'),
                             dir_items))
    find_pics(dir_, html_files)

def test():
    lst = []
    lst2 = []
    i = 0
    with open('LINKS_ALL.txt', 'r') as f:
        for line in f.readlines():
            i += 1
            if i % 500 == 0:
                print(i, len(lst), len(lst2))
            lst.append(line)
            if line not in lst2:
                lst2.append(line)
    print('=======================')
    print(len(lst))
    print(len(lst2))

if __name__ == '__main__':
    curr_dir()
    #test()
    
