import tweepy
from time import sleep
from credentials import *
import csv
import random

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# get an artwork

# columns in Artworks.csv
# Title,Artist,ConstituentID,ArtistBio,Nationality,BeginDate,EndDate,Gender,Date,Medium,Dimensions,CreditLine,AccessionNumber,Classification,Department,DateAcquired,Cataloged,ObjectID,URL,ThumbnailURL,Circumference (cm),Depth (cm),Diameter (cm),Height (cm),Length (cm),Weight (kg),Width (cm),Seat Height (cm),Duration (sec.)


def post_tweet():
    list_of_artworks_url = []

    with open("collection/Artworks.csv", newline="") as artworks_csv:
        artworks_reader = csv.DictReader(artworks_csv)
        for row in artworks_reader:
            list_of_artworks_url.append(row["URL"])

    i = 0
    while i < 1000:
        res = random.choice(list_of_artworks_url)
        i += 1
        try:
            print(res)
            if res != "":
                api.update_status(res)
                sleep(3000)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(2)


post_tweet()
