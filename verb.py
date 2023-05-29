from dataclasses import dataclass
from typing import Any


@dataclass
class Verb:
    infinitive: str
    translation: str
    verbal_noun: str | None
    present_active_participle_on: str | None
    past_active_participle_on: str | None
    past_passive_participle_on: str | None
    present_ja: str
    present_ty: str
    present_on_ona_ono: str
    present_my: str
    present_vy: str
    present_oni_ony: str
    past_ja_masculine: str
    past_ja_feminine: str
    past_ty_masculine: str
    past_ty_feminine: str
    past_on: str
    past_ona: str
    past_ono: str
    past_my: str
    past_vy: str
    past_oni_ony: str
    past_perfect_ja_masculine: str
    past_perfect_ja_feminine: str
    past_perfect_ty_masculine: str
    past_perfect_ty_feminine: str
    past_perfect_on: str
    past_perfect_ona: str
    past_perfect_ono: str
    past_perfect_my: str
    past_perfect_vy: str
    past_perfect_oni_ony: str
    future_ja: str
    future_ty: str
    future_on_ona_ono: str
    future_my: str
    future_vy: str
    future_oni_ony: str
    present_conditional_ja_masculine: str
    present_conditional_ja_feminine: str
    present_conditional_ty_masculine: str
    present_conditional_ty_feminine: str
    present_conditional_on: str
    present_conditional_ona: str
    present_conditional_ono: str
    present_conditional_my: str
    present_conditional_vy: str
    present_conditional_oni_ony: str
    past_conditional_ja_masculine: str
    past_conditional_ja_feminine: str
    past_conditional_ty_masculine: str
    past_conditional_ty_feminine: str
    past_conditional_on: str
    past_conditional_ona: str
    past_conditional_ono: str
    past_conditional_my: str
    past_conditional_vy: str
    past_conditional_oni_ony: str
    imperative_ty: str | None
    imperative_on_ona_ono: str | None
    imperative_my: str | None
    imperative_vy: str | None
    imperative_oni_ony: str | None
    regular: bool
    modal: bool
    perfect: bool
    amount_of_cards: int

    def __init__(self, obj: Any):
        self.__dict__ = obj

