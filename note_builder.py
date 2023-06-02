import uuid

from tags import Tense, Subject, VerbAttribute, Gender, Misc
from templates import Prompt, Notes
from usc_note import USCNote
from verb import Verb


class NoteBuilder:
    infinitive: str
    translation: str
    conjugation: str
    tense: Tense
    subjects: list[Subject]
    verb_attributes: list[VerbAttribute]
    reminder: bool
    gender: Gender | None

    def __init__(self, verb: Verb):
        self.subjects = []
        self.verb_attributes = []
        self.reminder = False
        self.gender = None
        self.__set_infinitive(verb.infinitive)
        self.__set_translation(verb.translation)
        self.__set_attributes(verb.regular, verb.modal, verb.perfect)

    def set_conjugation(self, conjugation: str) -> 'NoteBuilder':
        self.conjugation = conjugation
        return self

    def set_tense(self, tense: Tense) -> 'NoteBuilder':
        self.tense = tense
        return self

    def add_subject(self, subject: Subject) -> 'NoteBuilder':
        self.subjects.append(subject)
        return self

    def is_reminder(self) -> 'NoteBuilder':
        self.reminder = True
        return self

    def set_gender(self, gender: Gender) -> 'NoteBuilder':
        self.gender = gender
        return self

    def build(self) -> USCNote:
        return USCNote.create(self.__uuid, self.__prompt, self.__notes, self.__tags)

    def __set_infinitive(self, infinitive: str):
        self.infinitive = infinitive

    def __set_translation(self, translation: str):
        self.translation = translation

    def __add_verb_attribute(self, verb_attribute: VerbAttribute):
        self.verb_attributes.append(verb_attribute)

    def __set_attributes(self, regular: bool, modal: bool, perfect: bool):
        if regular:
            self.__add_verb_attribute(VerbAttribute.Regular)
        else:
            self.__add_verb_attribute(VerbAttribute.Irregular)
        if modal:
            self.__add_verb_attribute(VerbAttribute.Modal)
        if perfect:
            self.__add_verb_attribute(VerbAttribute.Perfect)
        else:
            self.__add_verb_attribute(VerbAttribute.Imperfect)

    @property
    def __uuid(self) -> str:
        _tense: str = str(self.tense)
        _subjects: str = "".join([str(s) for s in self.subjects])
        _gender: str = "" if self.gender is None else str(self.gender)

        return str(uuid.uuid5(uuid.NAMESPACE_DNS, self.infinitive + _tense + _subjects + _gender))

    @property
    def __tags(self) -> list[str]:
        tags: list[str] = [self.infinitive, str(self.tense)]

        [tags.append(str(subject)) for subject in self.subjects]
        [tags.append(str(verb_attribute)) for verb_attribute in self.verb_attributes]
        if self.gender is not None:
            tags.append(str(self.gender))
        if self.reminder:
            tags.append(str(Misc.Reminder))

        return tags

    @property
    def __prompt(self) -> str:
        if self.tense is Tense.Infinitive:
            return Prompt.infinitive(self.infinitive, self.conjugation)

        if self.tense is Tense.VerbalNoun:
            return Prompt.verbal_noun(self.infinitive, self.conjugation)

        if self.tense is Tense.PresentActiveParticiple:
            return Prompt.present_active_participle(self.infinitive, self.conjugation)
        if self.tense is Tense.PastActiveParticiple:
            return Prompt.past_active_participle(self.infinitive, self.conjugation)
        if self.tense is Tense.PastPassiveParticiple:
            return Prompt.past_passive_participle(self.infinitive, self.conjugation)

        if self.tense is Tense.Present and Subject.On in self.subjects and Subject.Ona in self.subjects and Subject.Ono in self.subjects:
            return Prompt.present_tense_on_ona_ono(self.infinitive, self.conjugation)
        if self.tense is Tense.Present and Subject.Ony in self.subjects and Subject.Oni in self.subjects:
            return Prompt.present_tense_ony_oni(self.infinitive, self.conjugation)
        if self.tense is Tense.Present:
            return Prompt.present_tense(self.infinitive, self.conjugation, self.subjects[0])

        if self.tense is Tense.Past and Subject.Ony in self.subjects and Subject.Oni in self.subjects:
            return Prompt.past_tense_ony_oni(self.infinitive, self.conjugation)
        if self.tense is Tense.PastPerfect and Subject.Ony in self.subjects and Subject.Oni in self.subjects:
            return Prompt.past_perfect_tense_ony_oni(self.infinitive, self.conjugation)
        if self.tense is Tense.Past and self.gender is not None:
            return Prompt.past_tense_gender(self.infinitive, self.conjugation, self.subjects[0], self.gender)
        if self.tense is Tense.PastPerfect and self.gender is not None:
            return Prompt.past_perfect_tense_gender(self.infinitive, self.conjugation, self.subjects[0], self.gender)
        if self.tense is Tense.Past:
            return Prompt.past_tense(self.infinitive, self.conjugation, self.subjects[0])
        if self.tense is Tense.PastPerfect:
            return Prompt.past_perfect_tense(self.infinitive, self.conjugation, self.subjects[0])

        if self.tense is Tense.Future and Subject.On in self.subjects and Subject.Ona in self.subjects and Subject.Ono in self.subjects:
            return Prompt.future_tense_on_ona_ono(self.infinitive, self.conjugation)
        if self.tense is Tense.Future and Subject.Ony in self.subjects and Subject.Oni in self.subjects:
            return Prompt.future_tense_ony_oni(self.infinitive, self.conjugation)
        if self.tense is Tense.Future:
            return Prompt.future_tense(self.infinitive, self.conjugation, self.subjects[0])

        if self.tense is Tense.PresentConditional and Subject.Ony in self.subjects and Subject.Oni in self.subjects:
            return Prompt.present_conditional_ony_oni(self.infinitive, self.conjugation)
        if self.tense is Tense.PastConditional and Subject.Ony in self.subjects and Subject.Oni in self.subjects:
            return Prompt.past_conditional_ony_oni(self.infinitive, self.conjugation)
        if self.tense is Tense.PresentConditional and self.gender is not None:
            return Prompt.present_conditional_gender(self.infinitive, self.conjugation, self.subjects[0], self.gender)
        if self.tense is Tense.PastConditional and self.gender is not None:
            return Prompt.past_conditional_gender(self.infinitive, self.conjugation, self.subjects[0], self.gender)
        if self.tense is Tense.PresentConditional:
            return Prompt.present_conditional(self.infinitive, self.conjugation, self.subjects[0])
        if self.tense is Tense.PastConditional:
            return Prompt.past_conditional(self.infinitive, self.conjugation, self.subjects[0])

        if self.tense is Tense.Imperative and Subject.On in self.subjects and Subject.Ona in self.subjects and Subject.Ono in self.subjects:
            return Prompt.imperative_tense_on_ona_ono(self.infinitive, self.conjugation)
        if self.tense is Tense.Imperative and Subject.Ony in self.subjects and Subject.Oni in self.subjects:
            return Prompt.imperative_tense_ony_oni(self.infinitive, self.conjugation)
        if self.tense is Tense.Imperative:
            return Prompt.imperative_tense(self.infinitive, self.conjugation, self.subjects[0])

        raise Exception()

    @property
    def __notes(self) -> str:
        result = Notes.verb_is_translated_as(self.infinitive, self.translation)

        if VerbAttribute.Regular in self.verb_attributes:
            result = result + Notes.regular() + Notes.comma()
        if VerbAttribute.Irregular in self.verb_attributes:
            result = result + Notes.irregular() + Notes.comma()
        if VerbAttribute.Modal in self.verb_attributes:
            result = result + Notes.modal() + Notes.comma()
        if VerbAttribute.Perfect in self.verb_attributes:
            result = result + Notes.perfect()
        if VerbAttribute.Imperfect in self.verb_attributes:
            result = result + Notes.imperfect()

        return result
