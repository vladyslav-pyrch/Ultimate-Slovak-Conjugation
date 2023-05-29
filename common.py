import json

import genanki

from verb import Verb


USCDeck = genanki.Deck(
    1946551571,
    "Ultimate Slovak Conjugation"
)

front_card = open("static/front card.html", "r")
back_card = open("static/back card.html", "r")
styles = open("static/styles.css", "r")


USCModel = genanki.Model(
    1812231381,
    "Ultimate Slovak Conjugation",
    fields=[
        {"name": "UUID"},
        {"name": "Prompt"},
        {"name": "Similar"},
        {"name": "Notes"}
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": front_card.read(),
            "afmt": back_card.read()
        }
    ],
    css=styles.read(),
    model_type=genanki.Model.CLOZE,
    sort_field_index=1
)

front_card.close()
back_card.close()
styles.close()


def get_verbs() -> list[Verb]:
    with open("Slovak Conjugation.json", "r", encoding="utf8") as file:
        verbs = [Verb(data) for data in json.loads(file.read())["Conjugation"]]
        return verbs
