from note_builder import NoteBuilder
from tags import Tense, Subject, Gender
from usc_note import USCNote
from verb import Verb
import common


def verb_to_set_of_notes(verb: Verb, index: int) -> tuple[list[USCNote], int]:
    result: list[USCNote] = []

    [result.append(note) for note in __infinitive(verb)]
    [result.append(note) for note in __verbal_noun(verb)]
    [result.append(note) for note in __participles(verb)]
    [result.append(note) for note in __present(verb)]
    [result.append(note) for note in __past(verb)]
    if verb.infinitive == 'byť':
        [result.append(note) for note in __future(verb)]
    [result.append(note) for note in __imperative(verb)]
    [result.append(note) for note in __reminder(verb, index)]

    print(f'{str(index + 1).zfill(2)}. {verb.infinitive.capitalize()} ({verb.translation}): {len(result)} cards')

    return result, len(result)


def __infinitive(verb: Verb) -> list[USCNote]:
    return [
        NoteBuilder(verb)
        .set_conjugation(verb.present_on_ona_ono)
        .set_tense(Tense.Infinitive)
        .build()
    ]


def __verbal_noun(verb: Verb) -> list[USCNote]:
    if verb.verbal_noun is None:
        return []

    return [
        NoteBuilder(verb)
        .set_conjugation(verb.verbal_noun)
        .set_tense(Tense.VerbalNoun)
        .build()
    ]


def __participles(verb: Verb) -> list[USCNote]:
    result: list[USCNote] = []
    if verb.present_active_participle_on is not None:
        result.append(
            NoteBuilder(verb)
            .set_conjugation(verb.present_active_participle_on)
            .set_tense(Tense.PresentActiveParticiple)
            .build()
        )
    if verb.past_active_participle_on is not None:
        result.append(
            NoteBuilder(verb)
            .set_conjugation(verb.past_active_participle_on)
            .set_tense(Tense.PastActiveParticiple)
            .build()
        )
    if verb.past_passive_participle_on is not None:
        result.append(
            NoteBuilder(verb)
            .set_conjugation(verb.past_passive_participle_on)
            .set_tense(Tense.PastPassiveParticiple)
            .build()
        )

    return result


def __present(verb: Verb) -> list[USCNote]:
    return [
        NoteBuilder(verb)
        .set_conjugation(verb.present_ja)
        .set_tense(Tense.Present)
        .add_subject(Subject.Ja)
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.present_ty)
        .set_tense(Tense.Present)
        .add_subject(Subject.Ty)
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.present_on_ona_ono)
        .set_tense(Tense.Present)
        .add_subject(Subject.On)
        .add_subject(Subject.Ona)
        .add_subject(Subject.Ono)
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.present_my)
        .set_tense(Tense.Present)
        .add_subject(Subject.My)
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.present_vy)
        .set_tense(Tense.Present)
        .add_subject(Subject.Vy)
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.present_oni_ony)
        .set_tense(Tense.Present)
        .add_subject(Subject.Oni)
        .add_subject(Subject.Ony)
        .build()
    ]


def __past(verb: Verb) -> list[USCNote]:
    return [
        NoteBuilder(verb)
        .set_conjugation(verb.past_on)
        .set_tense(Tense.Past)
        .add_subject(Subject.On)
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_ona)
        .set_tense(Tense.Past)
        .add_subject(Subject.Ona)
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_ono)
        .set_tense(Tense.Past)
        .add_subject(Subject.Ono)
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_oni_ony)
        .set_tense(Tense.Past)
        .add_subject(Subject.Oni)
        .add_subject(Subject.Ony)
        .build()
    ]


def __future(verb: Verb) -> list[USCNote]:
    return [
        NoteBuilder(verb)
        .set_conjugation(verb.future_ja)
        .set_tense(Tense.Future)
        .add_subject(Subject.Ja)
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.future_ty)
        .set_tense(Tense.Future)
        .add_subject(Subject.Ty)
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.future_on_ona_ono)
        .set_tense(Tense.Future)
        .add_subject(Subject.On)
        .add_subject(Subject.Ona)
        .add_subject(Subject.Ono)
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.future_my)
        .set_tense(Tense.Future)
        .add_subject(Subject.My)
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.future_vy)
        .set_tense(Tense.Future)
        .add_subject(Subject.Vy)
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.future_oni_ony)
        .set_tense(Tense.Future)
        .add_subject(Subject.Oni)
        .add_subject(Subject.Ony)
        .build()
    ]


def __imperative(verb: Verb) -> list[USCNote]:
    result: list[USCNote] = []

    if verb.imperative_ty is not None:
        result.append(
            NoteBuilder(verb)
            .set_conjugation(verb.imperative_ty)
            .set_tense(Tense.Imperative)
            .add_subject(Subject.Ty)
            .build()
        )
    if verb.imperative_my is not None:
        result.append(
            NoteBuilder(verb)
            .set_conjugation(verb.imperative_my)
            .set_tense(Tense.Imperative)
            .add_subject(Subject.My)
            .build()
        )
    if verb.imperative_vy is not None:
        result.append(
            NoteBuilder(verb)
            .set_conjugation(verb.imperative_vy)
            .set_tense(Tense.Imperative)
            .add_subject(Subject.Vy)
            .build()
        )

    return result


def __reminder(verb: Verb, index: int) -> list[USCNote]:
    future: list[USCNote] = [
        NoteBuilder(verb)
        .set_conjugation(verb.future_ja)
        .set_tense(Tense.Future)
        .add_subject(Subject.Ja)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.future_ty)
        .set_tense(Tense.Future)
        .add_subject(Subject.Ty)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.future_on_ona_ono)
        .set_tense(Tense.Future)
        .add_subject(Subject.On)
        .add_subject(Subject.Ona)
        .add_subject(Subject.Ono)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.future_my)
        .set_tense(Tense.Future)
        .add_subject(Subject.My)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.future_vy)
        .set_tense(Tense.Future)
        .add_subject(Subject.Vy)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.future_oni_ony)
        .set_tense(Tense.Future)
        .add_subject(Subject.Oni)
        .add_subject(Subject.Ony)
        .is_reminder()
        .build()
    ]
    past: list[USCNote] = [
        NoteBuilder(verb)
        .set_conjugation(verb.past_ja_masculine)
        .set_tense(Tense.Past)
        .add_subject(Subject.Ja)
        .set_gender(Gender.Masculine)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_ja_feminine)
        .set_tense(Tense.Past)
        .add_subject(Subject.Ja)
        .set_gender(Gender.Feminine)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_ty_masculine)
        .set_tense(Tense.Past)
        .add_subject(Subject.Ty)
        .set_gender(Gender.Masculine)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_ty_feminine)
        .set_tense(Tense.Past)
        .add_subject(Subject.Ty)
        .set_gender(Gender.Feminine)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_my)
        .set_tense(Tense.Past)
        .add_subject(Subject.My)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_vy)
        .set_tense(Tense.Past)
        .add_subject(Subject.Vy)
        .is_reminder()
        .build()
    ]
    past_perfect: list[USCNote] = [
        NoteBuilder(verb)
        .set_conjugation(verb.past_perfect_on)
        .set_tense(Tense.PastPerfect)
        .add_subject(Subject.On)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_perfect_ona)
        .set_tense(Tense.PastPerfect)
        .add_subject(Subject.Ona)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_perfect_ono)
        .set_tense(Tense.PastPerfect)
        .add_subject(Subject.Ono)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_perfect_oni_ony)
        .set_tense(Tense.PastPerfect)
        .add_subject(Subject.Oni)
        .add_subject(Subject.Ony)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_perfect_ja_masculine)
        .set_tense(Tense.PastPerfect)
        .add_subject(Subject.Ja)
        .set_gender(Gender.Masculine)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_perfect_ja_feminine)
        .set_tense(Tense.PastPerfect)
        .add_subject(Subject.Ja)
        .set_gender(Gender.Feminine)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_perfect_ty_masculine)
        .set_tense(Tense.PastPerfect)
        .add_subject(Subject.Ty)
        .set_gender(Gender.Masculine)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_perfect_ty_feminine)
        .set_tense(Tense.PastPerfect)
        .add_subject(Subject.Ty)
        .set_gender(Gender.Feminine)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_perfect_my)
        .set_tense(Tense.PastPerfect)
        .add_subject(Subject.My)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_perfect_vy)
        .set_tense(Tense.PastPerfect)
        .add_subject(Subject.Vy)
        .is_reminder()
        .build()
    ]
    present_conditional: list[USCNote] = [
        NoteBuilder(verb)
        .set_conjugation(verb.present_conditional_on)
        .set_tense(Tense.PresentConditional)
        .add_subject(Subject.On)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.present_conditional_ona)
        .set_tense(Tense.PresentConditional)
        .add_subject(Subject.Ona)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.present_conditional_ono)
        .set_tense(Tense.PresentConditional)
        .add_subject(Subject.Ono)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.present_conditional_oni_ony)
        .set_tense(Tense.PresentConditional)
        .add_subject(Subject.Oni)
        .add_subject(Subject.Ony)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.present_conditional_ja_masculine)
        .set_tense(Tense.PresentConditional)
        .add_subject(Subject.Ja)
        .set_gender(Gender.Masculine)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.present_conditional_ja_feminine)
        .set_tense(Tense.PresentConditional)
        .add_subject(Subject.Ja)
        .set_gender(Gender.Feminine)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.present_conditional_ty_masculine)
        .set_tense(Tense.PresentConditional)
        .add_subject(Subject.Ty)
        .set_gender(Gender.Masculine)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.present_conditional_ty_feminine)
        .set_tense(Tense.PresentConditional)
        .add_subject(Subject.Ty)
        .set_gender(Gender.Feminine)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.present_conditional_my)
        .set_tense(Tense.PresentConditional)
        .add_subject(Subject.My)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.present_conditional_vy)
        .set_tense(Tense.PresentConditional)
        .add_subject(Subject.Vy)
        .is_reminder()
        .build()
    ]
    past_conditional: list[USCNote] = [
        NoteBuilder(verb)
        .set_conjugation(verb.past_conditional_on)
        .set_tense(Tense.PastConditional)
        .add_subject(Subject.On)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_conditional_ona)
        .set_tense(Tense.PastConditional)
        .add_subject(Subject.Ona)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_conditional_ono)
        .set_tense(Tense.PastConditional)
        .add_subject(Subject.Ono)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_conditional_oni_ony)
        .set_tense(Tense.PastConditional)
        .add_subject(Subject.Oni)
        .add_subject(Subject.Ony)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_conditional_ja_masculine)
        .set_tense(Tense.PastConditional)
        .add_subject(Subject.Ja)
        .set_gender(Gender.Masculine)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_conditional_ja_feminine)
        .set_tense(Tense.PastConditional)
        .add_subject(Subject.Ja)
        .set_gender(Gender.Feminine)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_conditional_ty_masculine)
        .set_tense(Tense.PastConditional)
        .add_subject(Subject.Ty)
        .set_gender(Gender.Masculine)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_conditional_ty_feminine)
        .set_tense(Tense.PastConditional)
        .add_subject(Subject.Ty)
        .set_gender(Gender.Feminine)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_conditional_my)
        .set_tense(Tense.PastConditional)
        .add_subject(Subject.My)
        .is_reminder()
        .build(),
        NoteBuilder(verb)
        .set_conjugation(verb.past_conditional_vy)
        .set_tense(Tense.PastConditional)
        .add_subject(Subject.Vy)
        .is_reminder()
        .build()
    ]
    imperative: list[USCNote] = []

    if verb.imperative_on_ona_ono is not None:
        imperative.append(
            NoteBuilder(verb)
            .set_conjugation(verb.imperative_on_ona_ono)
            .set_tense(Tense.Imperative)
            .add_subject(Subject.On)
            .add_subject(Subject.Ona)
            .add_subject(Subject.Ono)
            .is_reminder()
            .build()
        )

    if verb.imperative_oni_ony is not None:
        imperative.append(
            NoteBuilder(verb)
            .set_conjugation(verb.imperative_oni_ony)
            .set_tense(Tense.Imperative)
            .add_subject(Subject.Oni)
            .add_subject(Subject.Ony)
            .is_reminder()
            .build()
        )

    result: list[USCNote] = []

    if verb.infinitive != 'byť':
        result.append(future[index % len(future)])

    result.append(past[index % len(past)])
    result.append(past_perfect[index % len(past_perfect)])
    result.append(present_conditional[index % len(present_conditional)])
    result.append(past_conditional[index % len(past_conditional)])

    if len(imperative) > 0:
        result.append(imperative[index % len(imperative)])

    return result
