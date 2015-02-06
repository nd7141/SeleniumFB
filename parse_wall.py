# -- coding: utf-8 --
from __future__ import division
import os

def find_beginning_of_posts(text):
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

def find_end_of_posts(text, start):
    idx = 0
    for line in text[start:]:
        if line.startswith(" 1."):
            break
        idx += 1
    return start + idx

def find_end_of_next_post(text, beginning):
    idx = 0
    for line in text[beginning+1:]:
        if line.startswith("    <#>"):
            break
        idx += 1
    return beginning + idx + 1

def extract_posts(text):
    start = find_beginning_of_posts(text)
    finish = find_end_of_posts(text, start)
    it = 0
    posts = []

    start_post = start
    end_post = find_end_of_next_post(text, start_post)
    post = text[start_post:end_post+1]
    posts.append("\n".join(post))

    last_end_post = end_post # sanity check
    while True:
        it += 1
        start_post = end_post
        end_post = find_end_of_next_post(text, start_post)

        # check that we don't stuck
        if last_end_post == end_post:
            break
        else:
            last_end_post = end_post
        # check until we reach finish line
        if end_post < finish:
            post = text[start_post:end_post+1]
            posts.append("\n".join(post))
        else:
            post = text[start_post:finish]
            posts.append("\n".join(post))
            break
    return posts







if __name__ == "__main__":

    with open("dump_folder/my_friends_walls/Анатолий Коротков.html") as f:
        # text = [line for line in f]
        text = []
        for line in f:
            text.append(line.split(os.linesep)[0])
    # for i, line in enumerate(text):
    #     print i, line[:20]
    start= find_beginning_of_posts(text)
    finish = find_end_of_posts(text, start)
    end = find_end_of_next_post(text, start)
    # print start
    # print finish
    # print end
    # print text[finish]
    # print '\n'.join(text[start:end])
    posts = extract_posts(text)
    for post in posts:
        print post
        print '*************************'
        print


    console = []