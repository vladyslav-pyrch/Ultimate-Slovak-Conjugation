from common import get_verbs, USCDeck
from usc_note import USCNote
from verb import Verb
from verb_to_set_of_notes import verb_to_set_of_notes


if __name__ == '__main__':
    verbs: list[Verb] = get_verbs()

    total_amount_of_cards: int = 0

    for verb in verbs:
        anki_notes: tuple[list[USCNote], int] = verb_to_set_of_notes(verb, verbs.index(verb))
        total_amount_of_cards += anki_notes[1]
        for anki_note in anki_notes[0]:
            USCDeck.add_note(anki_note)

    USCDeck.write_to_file('Ultimate Slovak Conjugation.apkg')

    print(f'Total amount of cards: {total_amount_of_cards}')
