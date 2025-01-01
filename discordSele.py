from cf import cf
import time

with cf() as bot:
    bot.accessToPage("https://discord.com")
    bot.clickElement("Login")
    time.sleep(10)