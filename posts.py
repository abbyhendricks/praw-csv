# https://praw.readthedocs.io/en/latest/
import praw
import csv
import datetime


def getChildComment(comment, list):
    row = constructRow(comment.name, comment.parent_id, comment.score,
                       comment.created, "COMMENT", comment.author, comment.body)
    list.append(row)
    if comment.replies.__len__() != 0:
        comment.replies.replace_more(limit=None)
        for reply in comment.replies:
            getChildComment(reply, list)


def constructRow(id, parent_id, score, date, rowType, author, body):
    return {
        "id": id,
        "parent_id": parent_id,
        "score": score,
        "date": millisToDate(date),
        "type": rowType,
        "author": author,
        "body": body
    }


def formatPostTitleText(title, text):
    return "Title:\n{}\n\nBody:\n{}".format(title, text)


def millisToDate(millis):
    return datetime.datetime.fromtimestamp(millis)

# https://praw.readthedocs.io/en/latest/getting_started/authentication.html
reddit = praw.Reddit(client_id="##replace_me##",
                        client_secret="##replace_me##",
                        user_agent="##replace_me##")

# https://www.reddit.com/r/sffpc/comments/jshxam/thought_you_might_appreciate_my_build/
linkIds = ['jshxam']

for linkId in linkIds:
    print("Extracting data for {}...".format(linkId))
    with open(linkId+'.csv', 'w', newline='\n') as csvfile:
        filewriter = csv.DictWriter(csvfile, fieldnames=['id', 'parent_id', 'score', 'date', 'type', 'author', 'body'],  delimiter='|',
                                    quotechar='\"', quoting=csv.QUOTE_ALL)

        filewriter.writeheader()
        post = reddit.submission(id=linkId)
        post._fetch()
        post.comments.replace_more(limit=None)
        row = constructRow(post.name, "<none>", post.score, post.created,
                           "POST", post.author, formatPostTitleText(post.title, post.selftext))
        filewriter.writerow(row)
        comments = list()
        for c in post.comments:
            getChildComment(c, comments)
        for c1 in comments:
            filewriter.writerow(c1)

print("Complete!")