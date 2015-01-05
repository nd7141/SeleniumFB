from __future__ import division
import os, json

DIR = "friends_htmls/"

# get all the users from the file
def parse_file(filename):
    friends_start = False
    names2ids = dict()
    with open(filename) as f:
        parsing = False
        for i, line in enumerate(f):
            # found trigger for a friend
            if "Search Facebook" in line:
            	line = next(f)
                try:
                    ix1 = filename.index("/")
                    ix2 = filename.index(".html")
                except:
                    continue
                names2ids[line.split(os.linesep)[0]] = filename[ix1+1:ix2]
                continue
            if "Search Friends" in line:
                friends_start = True
            if "Add FriendFriend Request" in line and friends_start:
                parsing = True
                continue
            # found friend's name
            if parsing and friends_start:
                # print 'Name:', line.split(os.linesep)[0]
                name = line.split(os.linesep)[0]
                # found friend id
                line = next(f)
                try:
                    ix1 = line.index('.com/')
                    ix2 = line.index('?')
                except:
                    continue
                if "profile.php" in line[ix1+5:ix2]:
                    ix1 += 15
                    ix2 = line.index('&')
                names2ids[name.strip()] = line[ix1+5:ix2]
                # print 'ID: ', line[ix1+5:ix2]
                parsing = False
            if "More About" in line:
                break
    return names2ids

if __name__ == "__main__":
    # names2ids = parse_file(DIR + "sergeykasatkin543.html")
    # with open(DIR + "sergeykasatkin543.json", "w+") as fp:
    #     json.dump(names2ids, fp)
    # # get all the filenames from the directory
    filenames = os.listdir(DIR)
    for fn in filenames:
        names2ids = parse_file(DIR + fn)
        # write users only to json file
        try:
            ix = fn.index(".html")
        except:
            print fn
            continue
            raise
        with open(DIR + fn[:ix] + ".json", "w+") as fp:
            json.dump(names2ids, fp)

