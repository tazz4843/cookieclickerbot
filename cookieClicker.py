# The module file behind the cookie clicker bot (u/CookieClickerBOT)!
# Copyright (C) 2020 u/tazz4843
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

version = '0.0.0alpha'

import praw, pickle, os

# Just a function to declutter the main file
def init(user, password, id, secret):
    print('Logging in to reddit, please wait... ')
    # Tries to log in to reddit
    try:
        reddit = praw.Reddit(client_id=id,
                         client_secret=secret,
                         password=password,
                         user_agent='web:' + id + ':' + version + ' (created by u/tazz4843)',
                         username=user)
    # If it fails, a friendly error is given to the user
    except OAuthException:
        print('\nFailed to log in!\nCheck the username and password!')
    print('Success!')
    # Checks the authorized user against the user that's supposed to be logged in, just in case
    authUser = reddit.user.me()
    if authUser != user:
        raise LoginException('Authorized user is unequal to the inputted user!')

def getNewPosts():
    print('Getting any new mentions... ')
    mentions = reddit.inbox.mentions(limit=150)
    if len(mentions) > 0:
        read = open('messages.txt', 'a+')
        read_mentions = read.readlines()
        for message in mentions:
            # Gets current mention id
            mention_id = message.id
            # Checks if mention id is in the mentions file, and if it is, skips the loop and exits
            for line in read_mentions:
                if line == mention_id:
                    break
            if line == mention_id:
                break
            # But if it isn't, it writes the id to the file and begins checking that post
            else:
                file.write(mention_id)
                # This simplifies the function code, so plz don't be angry about my questionable practices
                postsToCheck = open('posts.txt', 'a')
                postsToCheck.write(mention_id)
                postsToCheck.close()
            message.mark_read()
        read.close()

# Posts a comment in reply to another comment
def replyComment(text, idToReplyTo):
    comment = reddit.comment(id=idToReplyTo)
    try:
        comment.reply(text)
    except prawcore.exceptions.Forbidden:
        print('Failed to reply to ' + idToReplyTo + '! Do you have permissions?')

# Posts a comment in reply to a submission
def replySubmission(text, idToReplyTo):
    submission = reddit.submission(id=idToReplyTo)
    try:
        submission.reply(text)
    except prawcore.exceptions.Forbidden:
        print('Failed to reply to ' + idToReplyTo + '! Do you have permissions?')

def checkMod(subName):
    subreddit = reddit.subreddit(subName)
    mod = subreddit.user_is_moderator
    return mod

def initUser(user):
    if not os.path.isfile(user + '.txt'):
        user = open(user + '.txt', 'w')
        user.close()
        print('initalized u/' + user + "'s profile!")
    else:
        print('user u/' + user + "'s profile already exists!")

def getNewCommands():
    post = open('posts.txt', 'r')
    posts = post.readlines()
    post.close()
    replied = open('replied.txt', 'r')
    ids = replied.readlines()
    replied.close()
    for item in posts:
        submission = reddit.submission(id=item)
        submission.comments.replace_more(limit=None)
        for comment in submission.comments:
            commentId = comment.id
            for id in ids:
                if commentId = id:
                    success = True
                    break
            if not success:
                for string in commands:
                    if string[0] in comment.body:
                        runFunc(string[1], commentId)
                        file.write(comment.id + "\n")
                        break
    print('Finished checking all new posts!')

# Creates a class for users
class user:
    def __init__(user):
        data = open(user + '.txt', 'r')
        lines = data.readlines()
        self.username = user
        # I have a feeling this first line's gonna take a while once we get users that have over 100 undecillion cookies
        self.cookies = lines[0]
        self.cPC = lines[1]
        self.cPS = lines[2]
        # Cursor id is 0
        self.cursor = lines[3]
        # Grandma id is 1
        self.grandma = lines[4]
        # Farm id is 2, you should get the point.
        self.farm = lines[5]
        self.mine = lines[6]
        self.factory = lines[7]
        self.bank = lines[8]
        self.temple = lines[9]
        self.wizard_tower = lines[10]
        self.shipment = lines[11]
        self.alchemy_lab = lines[12]
        self.portal = lines[13]
        self.time_machine = lines[14]
        self.antimatter_condenser = lines[15]
        self.prisim = lines[16]
        self.chancemaker = lines[17]
        self.fractal_engine = lines[18]
        self.python_ide = lines[19]
        # Just to keep file I/0 and RAM usage to a minimum, the file is closed early
        data.close()
        # Creates a list that makes it MUCH easier to give the building id and count
        self.buildings = []
        j = 0
        i = 3
        while i < 20:
            self.buildings[j] = lines[i]
            i = i + 1
            j = j + 1

    # I know it's big. But it's fundamental to having happy users
    def save():
        output = self.cookies + '\n' + self.cPC + '\n' + self.cPS + '\n' + self.buildings[0] + '\n' + self.buildings[1] + '\n' + self.buildings[2] + '\n' + self.buildings[3] + '\n' + self.buildings[4] + '\n' + self.buildings[5] + '\n' + self.buildings[6] + '\n' + self.buildings[7] + '\n' + self.buildings[8] + '\n' + self.buildings[9] + '\n' + self.buildings[10] + '\n' + self.buildings[11] + '\n' + self.buildings[12] + '\n' + self.buildings[13] + '\n' + self.buildings[14] + '\n' + self.buildings[15] + '\n' + self.buildings[16]
        print('Saving u/' + self.username + "'s profile")
        outFile = open(self.username + '.txt', 'w')
        outFile.write(output)
        outFile.close()
        print('Saved!')

    # I really don't know why I need this function, but whatever.
    def clickCookie():
        self.cookies = self.cookies + self.cookiesPerClick

    # Returns a reddit-ready stats comment
    def stats():
        message = 'Hello, u/' + self.username + '!\n\n You have ' + str(self.cookies) + ' cookies, and are getting ' + str(self.cPS) + ' cookies per second. You gain ' + str(self.cPC) + ' cookies per click.\n\n^I\'m ^u/CookieClickerBOT, ^created ^by ^u/tazz4843 ^to ^bring ^cookie ^happines ^to ^reddit!''
        return message

    # Input is the id of the building
    def getUpgradePrice(id):
        upgrades = self.buildings[id] + 1
        for i in range(upgrades):
            # Actual cookie clicker algorithim (simple, right?)
            price = price * 1.15
        return price

    # Upgrades the building with the id number once. to upgrade more times, this function must be called multiple times
    def upgrade(id):
        price = self.getUpgradePrice(id)
        self.cookies = self.cookies - price
        if self.cookies < 0:
            self.cookies = self.cookies + price
            return 1
        else:
            self.buildings[id] = self.buildings[id] + 1
            return 0

    # Returns the CPS of the person
    def calculateCPS():
        # I know static variables are not the way to go, but don't forget I'm trying to get a release out with just basic functions
        cps = cps + (self.buildings[0] * 0.1)
        cps = cps + (self.buildings[1] * 1)
        cps = cps + (self.buildings[2] * 8)
        cps = cps + (self.buildings[3] * 47)
        cps = cps + (self.buildings[4] * 260)
        cps = cps + (self.buildings[5] * 1400)
        cps = cps + (self.buildings[6] * 7800)
        cps = cps + (self.buildings[7] * 44000)
        cps = cps + (self.buildings[8] * 260000)
        cps = cps + (self.buildings[9] * 1600000)
        cps = cps + (self.buildings[10] * 10000000)
        cps = cps + (self.buildings[11] * 65000000)
        cps = cps + (self.buildings[12] * 430000000)
        cps = cps + (self.buildings[13] * 2900000000)
        cps = cps + (self.buildings[14] * 21000000000)
        cps = cps + (self.buildings[15] * 150000000000)
        cps = cps + (self.buildings[16] * 1100000000000)
        return cps

    # Adds the cps to the person's total (designed to be called once per second)
    def addCPS():
        cps = calculateCPS()
        self.cookies = self.cookies + cps
