import genanki

from common import USCModel


class USCNote(genanki.Note):
    @staticmethod
    def create(uuid: str, prompt: str, notes: list[str], tags: list[str],
               similar: list[str] | None = None) -> "USCNote":
        similar: str = "" if similar is None else "".join(similar)
        notes: str = "".join(notes)

        return USCNote(model=USCModel, fields=[uuid, prompt, similar, notes], tags=tags, guid=uuid)
