# The main file behind u/CookieClickerBOT
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

# Saves me time with the coding
from cookieClicker import *

# Isn't it obvious?
cookieClicker.init('CookieClickerBOT', '', '_Y9tvLuZwxHntg', 'EVQB1heFRD9xmW8N7JIeGHTFa84')

# Creates 1 new user class
0 = user()

try:
    while True:
        getNewPosts()
        commands = getNewCommands()
        for item in commands:
            id = item[0]
            submitter = item[1]
            commentId = item[2]
            0.newUser(submitter)
            if id == 'click':
                0.clickCookie()
                continue
            elif id == 'up cursor':
                price = 0.getUpgradePrice(0)
                success = 0.upgrade(0)
                if success:
                    msg = 'You bought a building (id number 0) for ' + str(price) + ' cookies. You are now getting ' + str(cps) + ' CPS.'
                    replyComment(msg, commentId)
                else:
                    msg = "You don't have enough cookies! You need " + str(price) + " cookies to buy this building."
                    replyComment(msg, commentId)
            elif id == 'up grandma':
                price = 0.getUpgradePrice(1)
                success = 0.upgrade(1)
                if success:
                    msg = 'You bought a building (id number 1) for ' + str(price) + ' cookies. You are now getting ' + str(cps) + ' CPS.'
                    replyComment(msg, commentId)
                else:
                    msg = "You don't have enough cookies! You need " + str(price) + " cookies to buy this building."
                    replyComment(msg, commentId)
            elif id == 'up farm':
                price = 0.getUpgradePrice(2)
                success = 0.upgrade(2)
                if success:
                    msg = 'You bought a building (id number 2) for ' + str(price) + ' cookies. You are now getting ' + str(cps) + ' CPS.'
                    replyComment(msg, commentId)
                else:
                    msg = "You don't have enough cookies! You need " + str(price) + " cookies to buy this building."
                    replyComment(msg, commentId)
            elif id == 'up mine':
                price = 0.getUpgradePrice(3)
                success = 0.upgrade(3)
                if success:
                    msg = 'You bought a building (id number 3) for ' + str(price) + ' cookies. You are now getting ' + str(cps) + ' CPS.'
                    replyComment(msg, commentId)
                else:
                    msg = "You don't have enough cookies! You need " + str(price) + " cookies to buy this building."
                    replyComment(msg, commentId)
            elif id == 'up factory':
                price = 0.getUpgradePrice(4)
                success = 0.upgrade(4)
                if success:
                    msg = 'You bought a building (id number 4) for ' + str(price) + ' cookies. You are now getting ' + str(cps) + ' CPS.'
                    replyComment(msg, commentId)
                else:
                    msg = "You don't have enough cookies! You need " + str(price) + " cookies to buy this building."
                    replyComment(msg, commentId)
            elif id == 'up bank':
                price = 0.getUpgradePrice(5)
                success = 0.upgrade(5)
                if success:
                    msg = 'You bought a building (id number 5) for ' + str(price) + ' cookies. You are now getting ' + str(cps) + ' CPS.'
                    replyComment(msg, commentId)
                else:
                    msg = "You don't have enough cookies! You need " + str(price) + " cookies to buy this building."
                    replyComment(msg, commentId)
            elif id == 'up temple':
                price = 0.getUpgradePrice(6)
                success = 0.upgrade(6)
                if success:
                    msg = 'You bought a building (id number 6) for ' + str(price) + ' cookies. You are now getting ' + str(cps) + ' CPS.'
                    replyComment(msg, commentId)
                else:
                    msg = "You don't have enough cookies! You need " + str(price) + " cookies to buy this building."
                    replyComment(msg, commentId)
            elif id == 'up tower':
                price = 0.getUpgradePrice(7)
                success = 0.upgrade(7)
                if success:
                    msg = 'You bought a building (id number 7) for ' + str(price) + ' cookies. You are now getting ' + str(cps) + ' CPS.'
                    replyComment(msg, commentId)
                else:
                    msg = "You don't have enough cookies! You need " + str(price) + " cookies to buy this building."
                    replyComment(msg, commentId)
            elif id == 'up shipment':
                price = 0.getUpgradePrice(8)
                success = 0.upgrade(8)
                if success:
                    msg = 'You bought a building (id number 8) for ' + str(price) + ' cookies. You are now getting ' + str(cps) + ' CPS.'
                    replyComment(msg, commentId)
                else:
                    msg = "You don't have enough cookies! You need " + str(price) + " cookies to buy this building."
                    replyComment(msg, commentId)
            elif id == 'up lab':
                price = 0.getUpgradePrice(9)
                success = 0.upgrade(9)
                if success:
                    msg = 'You bought a building (id number 9) for ' + str(price) + ' cookies. You are now getting ' + str(cps) + ' CPS.'
                    replyComment(msg, commentId)
                else:
                    msg = "You don't have enough cookies! You need " + str(price) + " cookies to buy this building."
                    replyComment(msg, commentId)
            elif id == 'up portal':
                price = 0.getUpgradePrice(10)
                success = 0.upgrade(10)
                if success:
                    msg = 'You bought a building (id number 10) for ' + str(price) + ' cookies. You are now getting ' + str(cps) + ' CPS.'
                    replyComment(msg, commentId)
                else:
                    msg = "You don't have enough cookies! You need " + str(price) + " cookies to buy this building."
                    replyComment(msg, commentId)
            elif id == 'up time':
                price = 0.getUpgradePrice(11)
                success = 0.upgrade(11)
                if success:
                    msg = 'You bought a building (id number 11) for ' + str(price) + ' cookies. You are now getting ' + str(cps) + ' CPS.'
                    replyComment(msg, commentId)
                else:
                    msg = "You don't have enough cookies! You need " + str(price) + " cookies to buy this building."
                    replyComment(msg, commentId)
            elif id == 'up condenser':
                price = 0.getUpgradePrice(12)
                success = 0.upgrade(12)
                if success:
                    msg = 'You bought a building (id number 12) for ' + str(price) + ' cookies. You are now getting ' + str(cps) + ' CPS.'
                    replyComment(msg, commentId)
                else:
                    msg = "You don't have enough cookies! You need " + str(price) + " cookies to buy this building."
                    replyComment(msg, commentId)
            elif id == 'up prisim':
                price = 0.getUpgradePrice(13)
                success = 0.upgrade(13)
                if success:
                    msg = 'You bought a building (id number 13) for ' + str(price) + ' cookies. You are now getting ' + str(cps) + ' CPS.'
                    replyComment(msg, commentId)
                else:
                    msg = "You don't have enough cookies! You need " + str(price) + " cookies to buy this building."
                    replyComment(msg, commentId)
            elif id == 'up chancemaker':
                price = 0.getUpgradePrice(14)
                success = 0.upgrade(14)
                if success:
                    msg = 'You bought a building (id number 14) for ' + str(price) + ' cookies. You are now getting ' + str(cps) + ' CPS.'
                    replyComment(msg, commentId)
                else:
                    msg = "You don't have enough cookies! You need " + str(price) + " cookies to buy this building."
                    replyComment(msg, commentId)
            elif id == 'up engine':
                price = 0.getUpgradePrice(15)
                success = 0.upgrade(15)
                if success:
                    msg = 'You bought a building (id number 15) for ' + str(price) + ' cookies. You are now getting ' + str(cps) + ' CPS.'
                    replyComment(msg, commentId)
                else:
                    msg = "You don't have enough cookies! You need " + str(price) + " cookies to buy this building."
                    replyComment(msg, commentId)
            elif id == 'up ide':
                price = 0.getUpgradePrice(16)
                success = 0.upgrade(16)
                if success:
                    msg = 'You bought a building (id number 16) for ' + str(price) + ' cookies. You are now getting ' + str(cps) + ' CPS.'
                    replyComment(msg, commentId)
                else:
                    msg = "You don't have enough cookies! You need " + str(price) + " cookies to buy this building."
                    replyComment(msg, commentId)
            elif id == 'stats':
                stats = 0.stats()
                replyComment(stats, commentId)
            elif id == 'help':
                help = "*u/CookieClickerBOT Help*\n\nI have a good amount of functions, for only being a early alpha release.\n\nCreate a top level comment with the command you want.\n\n\*`click`: clicks your cookie once.\n\n*`stats`: gives you your current stats\n\n*`up <building>`: adds one building with the name. the list of names is avalible further down.\n\n*List Of Buildings*\n\n*cursor: cursor\n\n*grandma: grandma\n\n*farm: farm\n\n*mine: mine\n\n*factory: factory\n\n*bank: bank\n\n*temple: temple\n\n*tower: wizard tower\n\n*shipment: shipment\n\n*lab: alchemy lab\n\n*portal: portal\n\n*time: time machine\n\n*condenser: antimatter condenser\n\n*prisim: prisim\n\n*chancemaker: chancemaker\n\n*engine: fractal engine\n\n*ide: python ide/javascript console"
            0.save()
except KeyboardInterrupt:
    break


print('Saving profiles, please wait...')
0.save()
print('Saved!')
