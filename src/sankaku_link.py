import os

def make_link(pic_filename):
    offset = 0
    link_t = 'https://cs.sankakucomplex.com/data/%s/%s/%s'
    if pic_filename.startswith('sample'):
        offset = len('sample')+1
        link_t = 'https://cs.sankakucomplex.com/data/sample/%s/%s/%s'
    one = pic_filename[offset:offset+2]
    offset += 2
    two = pic_filename[offset:offset+2]
    
    link = link_t%(one, two, pic_filename)
    return link

def process_txt(src_txt):
    links = []
    with open(src_txt) as src_f:
        for filename in src_f.readlines():
            if len(filename) > 0:
                link = make_link(filename)
                links.append(link)
    dst_txt = '%s_%s.txt'%(src_txt[:-4], 'DONE')
    with open(dst_txt) as dst_f:
        for link in links:
            dst_txt.writeline(link)

def test1():
    file1 = 'sample-014e30624199554798cf1571b30dca43.jpg'
    file2 = '014e30624199554798cf1571b30dca43.jpg'
    print(make_link(file1))
    print(make_link(file2))


def process_dir(directory):
    directory = os.path.normpath(directory)
    url_lst = []
    file_lst = os.listdir(directory)
    for file in file_lst:
        if len(file) == 36 or len(file) == 43:
            url = make_link(file)
            url_lst.append(url)

    url_lst_file = os.path.basename(os.path.normpath(directory)) + '.txt'
    url_lst_file = os.path.join(directory, url_lst_file)

    with open(url_lst_file,'w') as f:
        for url in url_lst:
            f.write('%s\n'%(url))

def process():
    with open('dirlist.txt', newline='') as f:
        file_txt = f.read()
    dirs = file_txt.split(os.linesep)
    for dir_ in dirs:
        if len(dir_) > 0:
            print(dir_)
            process_dir(dir_)
        
#test1()
process()
