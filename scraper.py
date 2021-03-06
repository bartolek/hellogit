#import bibliotek
import requests
from bs4 import BeautifulSoup

#adres URL strony z opiniami
url = "https://www.ceneo.pl/85910996#tab=reviews"

#pobranie kodu HTML strony
page_respons = requests.get(url)
page_tree = BeautifulSoup(page_respons.text, "html.parser")

#wydobycie z kodu HTML fragmentów odpowiadających poszczególnym opiniom
opinions = page_tree.find_all("li", "review-box")

#wydobycie składowych dla pojedynczej opinii
opinion = opinions.pop()

opinion_id = opinion["data-entry-id"]
author = opinion.find("div", "reviewer-name-line").string
recomendation = opinion.find("div", "product-review-summary").find("em").string
stars = opinion.find("span","review-score-count").string
purchased = opinion.find("div", "product-review-pz").string

usefull = opinion.find("button", "vote-yes").find("span").string
useless = opinion.find("button", "vote-no").find("span").string
content = opinion.find("p", "product-review-body").get_text()
print(opinion_id, recomendation, usefull, useless, content, stars)

