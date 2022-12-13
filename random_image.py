#coding=UTF-8

#Modules
import tweepy
import glob
import random
import os
import shutil

#Access
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit = True)

#Post random image
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def randomimage(folder):
    images = glob.glob(folder + "*")
    image_open = images[random.randint(0,len(images))-1]
    image_size = os.path.getsize(image_open)

    api.update_with_media(image_open)

    #Prevent duplicate images
    #shutil.copy(image_open, "Copias/")
    #os.remove(image_open)

randomimage("Images/")
