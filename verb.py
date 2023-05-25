from typing import Any
from dataclasses import dataclass

@dataclass
class Verb:
    infinitive: str
    translation: str
    verbal_noun: str
    present_active_participle_on: str
    past_active_participle_on: str
    past_passive_participle_on: str
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
    imperative_ty: str
    imperative_on_ona_ono: str
    imperative_my: str
    imperative_vy: str
    imperative_oni_ony: str
    regular: bool
    modal: bool
    perfect: bool
    amount_of_cards: int

    @staticmethod
    def from_dict(obj: Any) -> 'Verb':
        _infinitive = str(obj.get("infinitive"))
        _translation = str(obj.get("translation"))
        _verbal_noun = str(obj.get("verbal_noun"))
        _present_active_participle_on = str(obj.get("present_active_participle_on"))
        _past_active_participle_on = str(obj.get("past_active_participle_on"))
        _past_passive_participle_on = str(obj.get("past_passive_participle_on"))
        _present_ja = str(obj.get("present_ja"))
        _present_ty = str(obj.get("present_ty"))
        _present_on_ona_ono = str(obj.get("present_on_ona_ono"))
        _present_my = str(obj.get("present_my"))
        _present_vy = str(obj.get("present_vy"))
        _present_oni_ony = str(obj.get("present_oni_ony"))
        _past_ja_masculine = str(obj.get("past_ja_masculine"))
        _past_ja_feminine = str(obj.get("past_ja_feminine"))
        _past_ty_masculine = str(obj.get("past_ty_masculine"))
        _past_ty_feminine = str(obj.get("past_ty_feminine"))
        _past_on = str(obj.get("past_on"))
        _past_ona = str(obj.get("past_ona"))
        _past_ono = str(obj.get("past_ono"))
        _past_my = str(obj.get("past_my"))
        _past_vy = str(obj.get("past_vy"))
        _past_oni_ony = str(obj.get("past_oni_ony"))
        _past_perfect_ja_masculine = str(obj.get("past_perfect_ja_masculine"))
        _past_perfect_ja_feminine = str(obj.get("past_perfect_ja_feminine"))
        _past_perfect_ty_masculine = str(obj.get("past_perfect_ty_masculine"))
        _past_perfect_ty_feminine = str(obj.get("past_perfect_ty_feminine"))
        _past_perfect_on = str(obj.get("past_perfect_on"))
        _past_perfect_ona = str(obj.get("past_perfect_ona"))
        _past_perfect_ono = str(obj.get("past_perfect_ono"))
        _past_perfect_my = str(obj.get("past_perfect_my"))
        _past_perfect_vy = str(obj.get("past_perfect_vy"))
        _past_perfect_oni_ony = str(obj.get("past_perfect_oni_ony"))
        _future_ja = str(obj.get("future_ja"))
        _future_ty = str(obj.get("future_ty"))
        _future_on_ona_ono = str(obj.get("future_on_ona_ono"))
        _future_my = str(obj.get("future_my"))
        _future_vy = str(obj.get("future_vy"))
        _future_oni_ony = str(obj.get("future_oni_ony"))
        _present_conditional_ja_masculine = str(obj.get("present_conditional_ja_masculine"))
        _present_conditional_ja_feminine = str(obj.get("present_conditional_ja_feminine"))
        _present_conditional_ty_masculine = str(obj.get("present_conditional_ty_masculine"))
        _present_conditional_ty_feminine = str(obj.get("present_conditional_ty_feminine"))
        _present_conditional_on = str(obj.get("present_conditional_on"))
        _present_conditional_ona = str(obj.get("present_conditional_ona"))
        _present_conditional_ono = str(obj.get("present_conditional_ono"))
        _present_conditional_my = str(obj.get("present_conditional_my"))
        _present_conditional_vy = str(obj.get("present_conditional_vy"))
        _present_conditional_oni_ony = str(obj.get("present_conditional_oni_ony"))
        _past_conditional_ja_masculine = str(obj.get("past_conditional_ja_masculine"))
        _past_conditional_ja_feminine = str(obj.get("past_conditional_ja_feminine"))
        _past_conditional_ty_masculine = str(obj.get("past_conditional_ty_masculine"))
        _past_conditional_ty_feminine = str(obj.get("past_conditional_ty_feminine"))
        _past_conditional_on = str(obj.get("past_conditional_on"))
        _past_conditional_ona = str(obj.get("past_conditional_ona"))
        _past_conditional_ono = str(obj.get("past_conditional_ono"))
        _past_conditional_my = str(obj.get("past_conditional_my"))
        _past_conditional_vy = str(obj.get("past_conditional_vy"))
        _past_conditional_oni_ony = str(obj.get("past_conditional_oni_ony"))
        _imperative_ty = str(obj.get("imperative_ty"))
        _imperative_on_ona_ono = str(obj.get("imperative_on_ona_ono"))
        _imperative_my = str(obj.get("imperative_my"))
        _imperative_vy = str(obj.get("imperative_vy"))
        _imperative_oni_ony = str(obj.get("imperative_oni_ony"))
        _regular = bool(obj.get("regular"))
        _modal = bool(obj.get("modal"))
        _perfect = bool(obj.get("perfect"))
        _amount_of_cards = int(obj.get("amount_of_cards"))
        return Verb(_infinitive, _translation, _verbal_noun, _present_active_participle_on, _past_active_participle_on,
                    _past_passive_participle_on, _present_ja, _present_ty, _present_on_ona_ono, _present_my,
                    _present_vy, _present_oni_ony, _past_ja_masculine, _past_ja_feminine, _past_ty_masculine,
                    _past_ty_feminine, _past_on, _past_ona, _past_ono, _past_my, _past_vy, _past_oni_ony,
                    _past_perfect_ja_masculine, _past_perfect_ja_feminine, _past_perfect_ty_masculine,
                    _past_perfect_ty_feminine, _past_perfect_on, _past_perfect_ona, _past_perfect_ono, _past_perfect_my,
                    _past_perfect_vy, _past_perfect_oni_ony, _future_ja, _future_ty, _future_on_ona_ono, _future_my,
                    _future_vy, _future_oni_ony, _present_conditional_ja_masculine, _present_conditional_ja_feminine,
                    _present_conditional_ty_masculine, _present_conditional_ty_feminine, _present_conditional_on,
                    _present_conditional_ona, _present_conditional_ono, _present_conditional_my,
                    _present_conditional_vy, _present_conditional_oni_ony, _past_conditional_ja_masculine,
                    _past_conditional_ja_feminine, _past_conditional_ty_masculine, _past_conditional_ty_feminine,
                    _past_conditional_on, _past_conditional_ona, _past_conditional_ono, _past_conditional_my,
                    _past_conditional_vy, _past_conditional_oni_ony, _imperative_ty, _imperative_on_ona_ono,
                    _imperative_my, _imperative_vy, _imperative_oni_ony, _regular, _modal, _perfect, _amount_of_cards)

