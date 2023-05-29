import genanki

from common import USCModel


class USCNote(genanki.Note):
    @staticmethod
    def create(uuid: str, prompt: str, notes: str, tags: list[str],
               similar: str = "") -> 'USCNote':
        return USCNote(model=USCModel, fields=[uuid, prompt, similar, notes], tags=tags, guid=uuid)
