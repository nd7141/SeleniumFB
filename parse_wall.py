# -- coding: utf-8 --
from __future__ import division
import os

def find_beginning(text):
    flag1 = False
    idx = 0

    for line in text:
        if line.startswith("Highlights"):
            flag1 = True
        if flag1 and "News Feed" in line:
            idx += 2
            break
        idx += 1
    return idx

def find_end_of_next_post(text, beginning):
    idx = 0
    while True:
        idx += 1
        line = text[beginning+idx]
        if line.startswith("    <#>"):
            break
    return beginning+idx

#TODO find end of posts

if __name__ == "__main__":

    with open("dump_folder/my_friends_walls/Анатолий Коротков.html") as f:
        # text = [line for line in f]
        text = []
        for line in f:
            text.append(line.split(os.linesep)[0])
    # for i, line in enumerate(text):
    #     print i, line[:20]
    beginning = find_beginning(text)
    end = find_end_of_next_post(text, beginning)
    print beginning
    print end
    print text[beginning]
    print text[beginning:end]


    console = []