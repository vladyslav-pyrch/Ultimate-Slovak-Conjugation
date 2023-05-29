from common import get_verbs, USCDeck
from verb_to_set_of_notes import verb_to_set_of_notes


if __name__ == '__main__':
    [USCDeck.add_note(anki_note) for verb in get_verbs() for anki_note in verb_to_set_of_notes(verb)]

    USCDeck.write_to_file('Ultimate Slovak Conjugation.apkg')
