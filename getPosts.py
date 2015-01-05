import nltk
import os
import csv
import os
import itertools
import urllib2




filename=r'C:\Users\user\Downloads\Hoxton Jam.htm'
os.chdir(r'C:\Users\user\Downloads')
g = globals() # dynamic creation of arrays for each post

StartOfPosts=[] #Array that stores the line in the textfile that each post starts

posts=globals() # dynamic creation of arrays for each post (without blank lines)
postsInfo=globals() # dynamic creation of arrays for each post's info
f1=open(filename,'r')
numOfPosts=0
lines = f1.readlines()
for i in range(len(lines)):
	lines[i]=lines[i].strip()
	if "<#>" in lines[i] and lines[i][0]=="<":
		lines[i+1]=lines[i+1].strip()
		if "https://www.facebook.com" in lines[i+1] and len(lines[i+1])<100 and lines[i+1][0]=="<":
			numOfPosts+=1
			StartOfPosts.append(i+1)
			g['post_{}'.format(numOfPosts)] = []
			posts['post_{}_NoBlankLines'.format(numOfPosts)] = []
			postsInfo['post_{}_Info'.format(numOfPosts)] = [[0,"date"],"nameOfPersonWhoPosts","linkOfPersonWhoPosts","linkOfPageForPeopleWhoLikeThisPost","NumberOfComments",["Comments"],[],[0,0],["PostContents"]] #The comments have the same structure as the post. Info[0]: #["lineof date","date"] The empty [] array is a helper to distinguish the real comments, [0,0]=>[StartOfPost,EndOfPost]
f1.close()

numOfPosts=numOfPosts-2

f1=open(filename,'r')
lines = f1.readlines()

for i in range(0, len(StartOfPosts)-1):
	for j in range(StartOfPosts[i]-1,StartOfPosts[i+1]-1):
		lines[j]=lines[j].strip()
		g['post_{}'.format(i+1)].append(lines[j])


for i in range(1,numOfPosts):
	for j in range(0,len(g['post_{}'.format(i)])):
		if g['post_{}'.format(i)][j]!="":
			posts['post_{}_NoBlankLines'.format(i)].append(g['post_{}'.format(i)][j])


for i in range(1,numOfPosts):
	for j in range(0,len(g['post_{}_NoBlankLines'.format(i)])):
		if len(g['post_{}'.format(i)][j])<100:
			if ("https://www.facebook.com" in g['post_{}_NoBlankLines'.format(i)][j] and g['post_{}_NoBlankLines'.format(i)][j][0]=="<"): 
				g['post_{}_NoBlankLines'.format(i)][j] = g['post_{}_NoBlankLines'.format(i)][j].translate(None, '<>')
				postsInfo['post_{}_Info'.format(i)][2]=g['post_{}_NoBlankLines'.format(i)][j]  
				postsInfo['post_{}_Info'.format(i)][1]=g['post_{}_NoBlankLines'.format(i)][j+1]
				break

for i in range(1,numOfPosts):
	for j in range(0,len(g['post_{}_NoBlankLines'.format(i)])):
		if ("Today" in g['post_{}_NoBlankLines'.format(i)][j] or "Yesterday" in g['post_{}_NoBlankLines'.format(i)][j] or "January" in g['post_{}_NoBlankLines'.format(i)][j] or "February" in g['post_{}_NoBlankLines'.format(i)][j] or "March" in g['post_{}_NoBlankLines'.format(i)][j] or "April" in g['post_{}_NoBlankLines'.format(i)][j] or "May" in g['post_{}_NoBlankLines'.format(i)][j] or "June" in g['post_{}_NoBlankLines'.format(i)][j] or "July" in g['post_{}_NoBlankLines'.format(i)][j] or "August" in g['post_{}_NoBlankLines'.format(i)][j] or "September" in g['post_{}_NoBlankLines'.format(i)][j] or "October" in g['post_{}_NoBlankLines'.format(i)][j] or "November" in g['post_{}_NoBlankLines'.format(i)][j] or "December" in g['post_{}_NoBlankLines'.format(i)][j]):
			if "<" in g['post_{}_NoBlankLines'.format(i)][j]:
				postsInfo['post_{}_Info'.format(i)][0][1]=g['post_{}_NoBlankLines'.format(i)][j].split("<", 1)[0]	
			else:	
				postsInfo['post_{}_Info'.format(i)][0][1]=g['post_{}_NoBlankLines'.format(i)][j]
			postsInfo['post_{}_Info'.format(i)][0][0]=j
			break

for i in range(1,numOfPosts):
	for j in range(0,len(g['post_{}_NoBlankLines'.format(i)])):
		if (">like this" in g['post_{}_NoBlankLines'.format(i)][j]):
			g['post_{}_NoBlankLines'.format(i)][j]=g['post_{}_NoBlankLines'.format(i)][j].split("like this", 1)[0]	
			g['post_{}_NoBlankLines'.format(i)][j] = g['post_{}_NoBlankLines'.format(i)][j].translate(None, '<>')
			postsInfo['post_{}_Info'.format(i)][3]="https://www.facebook.com"+g['post_{}_NoBlankLines'.format(i)][j]
			break

# Find the number of comments
for i in range(1,numOfPosts):
	totalComments=0
	for j in range(0,len(g['post_{}_NoBlankLines'.format(i)])):
		if ("total_comments=" in g['post_{}_NoBlankLines'.format(i)][j]):
			g['post_{}_NoBlankLines'.format(i)][j]=g['post_{}_NoBlankLines'.format(i)][j].split("total_comments=", 1)[1]
			g['post_{}_NoBlankLines'.format(i)][j]=g['post_{}_NoBlankLines'.format(i)][j].split(">", 1)[0]
			totalComments=int(g['post_{}_NoBlankLines'.format(i)][j])
			postsInfo['post_{}_Info'.format(i)][4]=totalComments
			postsInfo['post_{}_Info'.format(i)][5]=[]
			break

#If there are comments find the lines that the comments start
for i in range(1,numOfPosts):
	if isinstance(postsInfo['post_{}_Info'.format(i)][4],int)==True:
		commentsStartLinesTest=[0]
		commentsStartLinesInverse=[]
		for j in range(0,len(g['post_{}_NoBlankLines'.format(i)])):
			if ("*" in g['post_{}_NoBlankLines'.format(i)][j]):
				postsInfo['post_{}_Info'.format(i)][5].append([j])

for i in range(1,numOfPosts):
	if isinstance(postsInfo['post_{}_Info'.format(i)][4], int)==True:
		a=-postsInfo['post_{}_Info'.format(i)][4]-1
		postsInfo['post_{}_Info'.format(i)][5]=postsInfo['post_{}_Info'.format(i)][5][a:]
		postsInfo['post_{}_Info'.format(i)][5].append([len(g['post_{}_NoBlankLines'.format(i)])-1])


# Put each comment in an array
for i in range(1,numOfPosts):
	if isinstance(postsInfo['post_{}_Info'.format(i)][4], int)==True:
		for k in range(0, len(postsInfo['post_{}_Info'.format(i)][5])-1):
			j=postsInfo['post_{}_Info'.format(i)][5][k][0]
			while j<=postsInfo['post_{}_Info'.format(i)][5][k+1][0]:
				postsInfo['post_{}_Info'.format(i)][5][k].append(g['post_{}_NoBlankLines'.format(i)][j])
				j+=1

# Find the real comments
for i in range(1,numOfPosts):
	postsInfo['post_{}_Info'.format(i)].append([])
	if isinstance(postsInfo['post_{}_Info'.format(i)][4], int)==True:
		for k in range(0, len(postsInfo['post_{}_Info'.format(i)][5])):
			for l in range(0,len(postsInfo['post_{}_Info'.format(i)][5][k])):
				if postsInfo['post_{}_Info'.format(i)][5][k][l]=="Remove":
					postsInfo['post_{}_Info'.format(i)][6].append(postsInfo['post_{}_Info'.format(i)][5][k])

for i in range(1,numOfPosts):
	del postsInfo['post_{}_Info'.format(i)][5]




#Find the (Start,End) of every post
for i in range(1,numOfPosts):

	StartOfPost=postsInfo['post_{}_Info'.format(i)][0][0]
	EndOfPost=0
	if len(postsInfo['post_{}_Info'.format(i)][5])>0:
		EndOfPost=postsInfo['post_{}_Info'.format(i)][5][0][0]
	else:
		EndOfPost=len(g['post_{}_NoBlankLines'.format(i)])-1 
	

	postsInfo['post_{}_Info'.format(i)][6][0]=StartOfPost #Start Of Post
	postsInfo['post_{}_Info'.format(i)][6][1]=EndOfPost #End Of Post

# Put the text contents of each post in an array
for i in range(1,numOfPosts):
	postsInfo['post_{}_Info'.format(i)][7]=[]
	j=postsInfo['post_{}_Info'.format(i)][6][0]
	while j<postsInfo['post_{}_Info'.format(i)][6][1]:
		#print postsInfo['post_{}_Info'.format(i)][7][k]
		postsInfo['post_{}_Info'.format(i)][7].append(g['post_{}_NoBlankLines'.format(i)][j])
		j+=1

# Clear the post
for i in range(1,numOfPosts):
	postsInfo['post_{}_Info'.format(i)].append([])
	for k in range(0, len(postsInfo['post_{}_Info'.format(i)][7])):
		if postsInfo['post_{}_Info'.format(i)][7][k]!="//" and postsInfo['post_{}_Info'.format(i)][7][k]!="*" and "<#>" not in postsInfo['post_{}_Info'.format(i)][7][k] and "/browse/likes" not in postsInfo['post_{}_Info'.format(i)][7][k] and "/shares/" not in postsInfo['post_{}_Info'.format(i)][7][k] and "/sharer/" not in postsInfo['post_{}_Info'.format(i)][7][k] and "youtube.com" not in postsInfo['post_{}_Info'.format(i)][7][k] and ("people" not in postsInfo['post_{}_Info'.format(i)][7][k] and len(postsInfo['post_{}_Info'.format(i)][7][k])!=8 and len(postsInfo['post_{}_Info'.format(i)][7][k])!=9 and len(postsInfo['post_{}_Info'.format(i)][7][k])!=10) and "Lefteris Ntaflos" not in postsInfo['post_{}_Info'.format(i)][7][k] and "Write a comment..." not in postsInfo['post_{}_Info'.format(i)][7][k] and "www.facebook.com/hashtag/" not in postsInfo['post_{}_Info'.format(i)][7][k] and "youtu.be" not in postsInfo['post_{}_Info'.format(i)][7][k] and "http://l.facebook.com/" not in postsInfo['post_{}_Info'.format(i)][7][k]:
			postsInfo['post_{}_Info'.format(i)][8].append(postsInfo['post_{}_Info'.format(i)][7][k])

for i in range(1,numOfPosts):
	del postsInfo['post_{}_Info'.format(i)][7]


print "------------------------"
print "POST_78_: "
print "------------------------"
for k in range(0, len(post_78_Info[7])):
	print post_78_Info[7][k]

#for i in range(0,len(post_78_NoBlankLines)):
#	print post_78_NoBlankLines[i]

print "\n"
print "DATE OF POST: ",
print post_78_Info[0][1]	
print "NAME OF PERSON WHO POSTS: ",
print post_78_Info[1]	
print "LINK OF PERSON WHO POSTS: ",
print post_78_Info[2]	
print "LINK OF LIKES: ",
print post_78_Info[3]
print "TOTAL COMMENTS: ",
print post_78_Info[4]
print "\n"
print "COMMENTS: "
for k in range(0, len(post_78_Info[5])):
	print "\n"
	likesLink="Noone likes this"
	commentorName="noName"
	print post_78_Info[5][k]
	print "Link of commentor: %s" %post_78_Info[5][k][2]
	if " <" in post_78_Info[5][k][4]:
		commentorName=post_78_Info[5][k][4]
		commentorName=commentorName.split(" <", 1)[0]
	else:
		commentorName=post_78_Info[5][k][4]
	print "Name of commentor: %s" %commentorName 
	print "Date of comment: ",
	for l in range(1, len(post_78_Info[5][k])-1):
		if "January" in post_78_Info[5][k][l] or "February" in post_78_Info[5][k][l] or "March" in post_78_Info[5][k][l] or "April" in post_78_Info[5][k][l] or "May" in post_78_Info[5][k][l] or "June" in post_78_Info[5][k][l] or "July" in post_78_Info[5][k][l] or "August" in post_78_Info[5][k][l] or "September" in post_78_Info[5][k][l] or "October" in post_78_Info[5][k][l] or "November" in post_78_Info[5][k][l] or "December" in post_78_Info[5][k][l]:
			commentDate= post_78_Info[5][k][l]
		if "/browse/likes" in post_78_Info[5][k][l]:
			likesLink=post_78_Info[5][k][l]
			likesLink=likesLink.split("</", 1)[1]
			likesLink=likesLink.translate(None, '<>')
			likesLink="https://www.facebook.com/"+likesLink
	print commentDate
	print "Link of likes for comment: %s" %likesLink

print "\n"
if numOfPosts>5:
	numOfPosts=numOfPosts-5

print "------------------------"
print "TOTAL NUMBER OF POSTS OF USER: ",
print numOfPosts 



















