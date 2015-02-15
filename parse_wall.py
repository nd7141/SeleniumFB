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

# TODO parse each post: date, content, author, likes

def get_likes(snippet):
    number_of_likes = 0
    previous_line = ""
    for line in snippet:
        if "You" in line or "you" in line:
            number_of_likes += 1
        if "<http" in line:
            number_of_likes += 1
        if "people" in line or "others" in line:
            splitted = line.split()
            for idx, word in enumerate(splitted):
                if (word == "people" or word == "others"):
                    if idx != 0:
                        number_of_likes += int(splitted[idx - 1])
                    else:
                        number_of_likes += int(previous_line.split()[-1])
        # print line, number_of_likes
        if "like this." in line or "likes this." in line:
            break
        if "this." in line:
            if "like" == previous_line.split(">")[-1] or "likes" == previous_line.split(">")[-1]:
                break
        previous_line = line
    else:
        number_of_likes = 0
    return number_of_likes

#TODO transform date to datetime object
#TODO check is it works for other walls
def get_date_and_link(post):
    post_spl = post.split("\n")
    prev_line = ""
    for line in post_spl:
        if line.startswith("    //"):
            try:
                link_idx1 = prev_line.index("<") + 1
                link_idx2 = prev_line.index(">")
                link = "https://facebook.com" + prev_line[link_idx1:link_idx2]
            except ValueError:
                print "Cannot find link for a post"
                link = ""
            try:
                line_strpd = prev_line.strip()
                date_idx = line_strpd.index("<")
                date = line_strpd[:date_idx]
            except ValueError:
                print "Cannot find date for a post"
                date = ""
            return date, link
        elif line.startswith("    <https://www.facebook.com/photo.php?"):
            try:
                link_idx1 = line.index("<") + 1
                link_idx2 = line.index(">")
                link = line[link_idx1:link_idx2]
                date = prev_line
            except ValueError:
                print "Cannot find link for a post"
                link = ""
                date = ""
            return date, link
        prev_line = line
    else:
        print "Cannot find date and link..."
        return "", ""

def get_author_page(post, author):
    post_spl = post.split("\n")
    for i, line in enumerate(post_spl):
        if author in line:
            try:
                idx1 = line.index("<") + 1
                idx2 = line.index(">")
                return line[idx1:idx2]
            except ValueError:
                next_line = post_spl[i+1]
                try:
                    idx1 = next_line.index("<") + 1
                    idx2 = next_line.index(">")
                    return next_line[idx1:idx2]
                except ValueError:
                    print "Cannot find a page link..."
                    return ""
    else:
        print "Cannot find a page link..."
        return ""



def get_like_snippet(post):
    post = post.split("\n")
    second = False
    likes_snippet_start = False
    start_likes = 0
    for idx, line in enumerate(post):
        if "ike <#> ·" in line:
            start_likes = idx
            likes_snippet_start = True
        elif "*" in line and likes_snippet_start:
            if not second:
                second = True
                start_likes = idx
            else:
                end_likes = idx
                # print start_likes, end_likes
                break
    else:
        end_likes = idx
        # print start_likes, end_likes
    like_snippet = post[start_likes:end_likes]
    return like_snippet


if __name__ == "__main__":

    author = "Никита Пестров"

    with open("dump_folder/my_friends_walls/%s.html" %(author)) as f:
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
    for idx, post in enumerate(posts):
        print post
        date, link = get_date_and_link(post)
        page = get_author_page(post, author)
        print "The date is: ", date
        print "The link is: ", link
        print "The page is: ", page
        snippet = get_like_snippet(post)
    #     # print "\n".join(snippet)
        print "Post %s has %s likes" %(idx + 1, get_likes(snippet))
        print '*************************'
        print

    # get_date(posts[1])

    console = []