import random
import config
import praw
import time



def authenticate():
	reddit = praw.Reddit(username = config.username,
		password = config.password,
		client_id = config.client_id,
		client_secret = config.client_secret,
		user_agent = config.user_agent)
	return reddit

def getReplies():
	with open("replies.txt", 'r') as file:
		cr = file.read()
		cr2 = list(cr)
		cr2 = (cr2)
		cr = (cr)
		#cr2 = cr2.split("\n")
		cr = cr.split("\n")
		cr = filter(None, cr)
	return cr


def run(reddit, cr2):


	with open('bleach.txt') as b:

	    a = b.readlines()
	    msg = "\n^beep ^boop! ^I ^am ^a ^bot. ^Please ^contact ^[u/cyanidesuppository](https://reddit.com/user/cyanidesuppository) ^with ^any ^issues."

	    #rb = a[rn] + msg

	for comment in reddit.subreddit('testingground4bots').stream.comments(skip_existing=True):
		if "!eyebleacherbot" in comment.body and comment.id not in cr2 and not comment.saved:
			print("Bot called")
			comment.save()
			comment.reply(random.choice(a) + msg)
			print("Bot replied")
			list(cr2).append(comment.id)

			with open("replies.txt", "a") as file:
				file.write(comment.id + "\n")

	time.sleep(60)
