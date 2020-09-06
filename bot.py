import random
import config
import praw
import time


def authenticate():
    reddit = praw.Reddit(username=config.username,
                         password=config.password,
                         client_id=config.client_id,
                         client_secret=config.client_secret,
                         user_agent=config.user_agent)
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
        msg = "\n*Beep Boop! I'm a bot! I'm active in* [*These*](https://www.reddit.com/user/EyeBleacherBot/comments/gy47ws/subs_im_currently_active_in/) *subreddits! Please contact* [*u/cyanidesuppository*](https://reddit.com/user/cyanidesuppository) *with any issues or suggestions.* [*Github*](https://github.com/getcake/EyeBleacherBot) "

        #msg = "\n*Beep Boop! I'm a bot! This bleach was delivered automatically, but you can call me with !eyebleacherbot too! I'm active in* [*THESE*](https://www.reddit.com/user/EyeBleacherBot/comments/gy47ws/subs_im_currently_active_in/) *subreddits! Please contact* [*u/cyanidesuppository*](https://reddit.com/user/cyanidesuppository) *with any issues or suggestions.* [*Github*](https://github.com/getcake/EyeBleacherBot) "

    for comment in reddit.subreddit('diwhy+ataae+cursedcursedcomments+casualuk+winstupidprizes+idiotswithguns+thatsinsane+abruptchaos+lifeprotips+aboringdystopia+blackpeoplegifs+whitepeoplegifs+europe+creepy+oddlyterrifying+prequelmemes+dankmemes+australia+tooktoomuch+cursedimages+combatfootage+politics+creepy+news+interestingasfuck+nononoyes+tifu+nosleep+copypasta+botchessurgeries+gifs+blackpeopletwitter+whitepeopletwitter+insaneparents+justiceserved+insanepeoplefacebook+pics+dankmemes+fightporn+tiktokcringe+iamatotalpieceofshit+actualpublicfreakouts+atbge+wtf+wtfdidijustread+weird+askreddit+prequelmemes+trashy+godweeps+makemesuffer+makemesuffermore+mrpresidentthebutton+memes+tihi+noahgettheboat+noahgetthedeathstar+cursedcomments+morbidreality+pewdiepiesubmissions+teenagers+awfuleverything+holup+cringetopia+blursedimages+cursed_images+botrights+testingground4bots+atbge+fiftyfifty').stream.comments(skip_existing=True):

        if "!eyebleacherbot" in comment.body.lower() or "u/eyebleacherbot" in comment.body.lower() and comment.id not in cr2 and not comment.saved:
            try:

                print("Bot called")
                comment.save()
                comment.reply(random.choice(a) + '\n' + msg)
                print("Bot replied")
                list(cr2).append(comment.id)

                with open("replies.txt", "a") as file:
                    file.write(comment.id + "\n")

            except Exception as e:
                print(e)
                time.sleep(30)

        elif "i need bleach" in comment.body.lower() or "unsee juice" in comment.body.lower() or "who's got the bleach" in comment.body.lower() or "where's the bleach" in comment.body.lower() or "bleach my eyes" in comment.body.lower() or "bleach please" in comment.body.lower() or "get the bleach" in comment.body.lower() or "i need eyebleach" in comment.body.lower() or "give me bleach" in comment.body.lower() or "i need eye bleach" in comment.body.lower() or "wheres the bleach" in comment.body.lower() or "i need some bleach" in comment.body.lower() or "i need some eye bleach" in comment.body.lower() or "who's got the bleach" in comment.body.lower() or "need eye bleach" in comment.body.lower() or "have eyebleach" in comment.body.lower() or "eyebleach needed" in comment.body.lower() or "who has the bleach" in comment.body.lower() and comment.id not in cr2 and not comment.saved:
            try:

                print("Bot called")
                comment.save()
                comment.reply(random.choice(a) + msg)
                print("Bot replied")
                list(cr2).append(comment.id)

                with open("replies.txt", "a") as file:
                    file.write(comment.id + "\n")

            except Exception as e:
                print(e)
                time.sleep(30)

        elif "[nsfl]" in comment.body.lower() and comment.id not in cr2 and not comment.saved:
            try:

                print("Bot called")
                comment.save()
                comment.reply(
                    "*Not Safe for Life content detected!*" + '\n\n' + random.choice(a) + msg)
                print("Bot replied")
                list(cr2).append(comment.id)

                with open("replies.txt", "a") as file:
                    file.write(comment.id + "\n")

            except Exception as e:
                print(e)
                time.sleep(30)

    time.sleep(60)
