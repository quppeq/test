from html.parser import HTMLParser
from html.entities import name2codepoint

token = "562189430:AAG9Gx26wRCvH8Jeb-mB11tEkWu2FjaLitU"

class Html(HTMLParser):
    url = ""
    def handle_starttag(self, tag, attrs):
        t = 0
        for attr in attrs:
            if "data-large-file-url" in attr:
                if "https" in attr[1]:
                    self.url = attr[1]
                else:
                    self.url = "https://danbooru.donmai.us/" + attr[1]




html = Html()
