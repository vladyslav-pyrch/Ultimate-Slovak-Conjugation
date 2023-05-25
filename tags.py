from enum import StrEnum


class Tense(StrEnum):
    Infinitive = "infinitive"
    VerbalNoun = "verbal_noun"
    PresentActiveParticiple = "present_active_participle"
    PastActiveParticiple = "past_active_participle"
    PastPassiveParticiple = "past_passive_participle"
    Present = "present"
    Past = "past"
    PastPerfect = "past_perfect"
    Future = "future"
    PresentConditional = "present_conditional"
    PastConditional = "past_conditional"
    Imperative = "imperative"


class Subject(StrEnum):
    Ja = "ja"
    Ty = "ty"
    On = "on"
    Ona = "ona"
    Ono = "ono"
    My = "my"
    Vy = "vy"
    Oni = "oni"
    Ony = "ony"


class Gender(StrEnum):
    Masculine = "masculine"
    Feminine = "feminine"


class VerbAttribute(StrEnum):
    Regular = "regular"
    Irregular = "irregular"
    Modal = "modal"
    Perfect = "perfect"
    Imperfect = "imperfect"
