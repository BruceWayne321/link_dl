#!/usr/bin/python3
from multiprocessing import Process
import subprocess
import os
import sys
import fileinput
# import wget
def get_input(filename):
    lines = []
    for line in fileinput.input(files=filename):
        lines.append(line.strip()) #strip() will remove all trailing whitespaces
    return lines
    ''' # this is to get input in terminal line-by-line
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else: break
    '''
def download(link):
    # using subprocess to download using systems wget
    # when using wget we dont have to worry about file-type
    name = link.split('/')[-1]
    subprocess.run(['wget', '-O', './downloads/'+name, link,])
    '''
    r = requests.get(link)
    with open(name, 'wb') as f:
        f.write(r.content)
    '''
    ''' 
    name = link[-10:]
    wget.download(link, out=name,)   # this results in error so work on this
    '''
    
if __name__ == '__main__':
    ''' # sys.argv is the arguments passed while execution
    filename = sys.argv[1]
    contents = get_input(filename)'''

    list_dir = os.listdir("./")

    if sys.argv[1] == '-h':
        print("Hey!! this is a link-dl \nif you want to download files off of a link add the links in the url.txt file line-by-line and run this tool \nthanks")

    elif sys.argv[1] not in list_dir:
        print("No file found\nTry '-h' for help")
    
    elif sys.argv[1] in list_dir:
        contents = get_input(sys.argv[1])
        
        for i in contents:
            p = Process(target=download, args=(i,))
            p.start()
            # p.join()
        
    