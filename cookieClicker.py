# The module file behind the cookie clicker bot (u/CookieClickerBOT)!

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
            mention_id = message.id + "\n"
            # Checks if mention id is in the mentions file, and if it is, skips the loop and exits
            for line in read_mentions:
                if line == mention_id:
                    break
            if line == mention_id:
                break
            # But if it isn't, it writes the id to the file and begins checking that post
            else:
                file.write(mention_id)
            message.mark_read()
        read.close()

def postComment(text, comment):
    # Posts a comment

def initUser(user):
    if not os.path.isfile(user + '.txt'):
        user = open(user + '.txt', 'w')
        user.close()
        print('initalized u/' + user + "'s profile!")
    else:
        print('user u/' + user + "'s profile already exists!")

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
        data.close()

    # I know it's big. But it's fundamental to having happy users
    def save():
        output = self.cookies + '\n' + self.cPC + '\n' + self.cPS + '\n' + self.cursor + '\n' + self.grandma + '\n' + self.farm + '\n' + self.mine + '\n' + self.factory + '\n' + self.bank + '\n' + self.temple + '\n' + self.wizard_tower + '\n' + self.shipment + '\n' + self.alchemy_lab + '\n' + self.portal + '\n' + self.time_machine + '\n' + self.antimatter_condenser + '\n' + self.prisim + '\n' + self.chancemaker + '\n' + self.fractal_engine + '\n' + self.python_ide
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

    # Takes one of the building counts as a input and the other input is the id of the building. that can be found in ./ids.txt
    def getUpgradePrice(item, id):
        upgrades = item + 1
        for i in range(upgrades):
            price = price * 1.15
        return price

    # Upgrades the building with the id number once. to upgrade more times, this function must be called multiple times
    def upgrade(id):
        self.getUpgradePrice(self.id)
