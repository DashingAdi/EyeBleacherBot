import praw
import bot

comments_replied = bot.getReplies()

reddit = bot.authenticate()

while True:
	bot.run(reddit, cr)
