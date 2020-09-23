import praw
import bot

reddit = bot.authenticate()
while True:
        try:
                bot.run(reddit)
        except Exception as e:
                print(e)
                continue
