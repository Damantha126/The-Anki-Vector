import os
import re

import requests
from bs4 import BeautifulSoup
from telethon import events

from AnkiVector.services.telethon import tbot


@tbot.on(events.NewMessage(pattern="^/book (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    lool = 0
    KkK = await event.reply("searching for the book...📚")
    lin = "https://b-ok.cc/s/"
    text = input_str
    link = lin + text

    headers = [
        "User-Agent",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0",
    ]
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    f = open("book.txt", "w")
    total = soup.find(class_="totalCounter")
    for nb in total.descendants:
        nbx = nb.replace("(", "").replace(")", "")
    if nbx == "0":
        await event.reply("No Books Found with that name.😞 ")
    else:

        for tr in soup.find_all("td"):
            for td in tr.find_all("h3"):
                for ts in td.find_all("a"):
                    title = ts.get_text()
                    lool = lool + 1
                for ts in td.find_all("a", attrs={"href": re.compile("^/book/")}):
                    ref = ts.get("href")
                    link = "https://b-ok.cc" + ref

                f.write("\n" + title)
                f.write("\nBook link:- " + link + "\n\n")

        f.write("✅ By @szrosebot.")
        f.close()
        caption = "Join with our channel -- @sl_bot_zone.\n Join Support @slbotzone ✳️"

        await tbot.send_file(
            event.chat_id,
            "book.txt",
            caption=f"**BOOKS GATHERED SUCCESSFULLY!📕📗📘\n\nBY @szrosebot . JOIN THE SUPPORT @slbotzone.**",
        )
        os.remove("book.txt")
        await KkK.delete()
