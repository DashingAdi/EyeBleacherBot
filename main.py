import praw
import bot
import time
reddit = bot.authenticate()
while True:
        try:
                bot.run(reddit)
        except Exception as e:
                print(e)
                continue
