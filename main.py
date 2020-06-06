import praw
import bot

cr = bot.getReplies()

reddit = bot.authenticate()

while True:
	bot.run(reddit, cr)
