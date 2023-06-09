class Prompt:
    @staticmethod
    def infinitive(infinitive: str, present_on: str, context: str) -> str:
        with open('static/templates/misc/infinitive.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, present_on=present_on, context=context)

    @staticmethod
    def verbal_noun(infinitive: str, verbal_noun: str, context: str) -> str:
        with open('static/templates/misc/verbal noun.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, verbal_noun=verbal_noun, context=context)

    @staticmethod
    def present_active_participle(infinitive: str, present_active_participle: str) -> str:
        with open('static/templates/participles/present active participle.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, present_active_participle=present_active_participle)

    @staticmethod
    def past_active_participle(infinitive: str, past_active_participle: str, context: str) -> str:
        with open('static/templates/participles/past active participle.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, past_active_participle=past_active_participle,
                                          context=context)

    @staticmethod
    def past_passive_participle(infinitive: str, past_passive_participle: str) -> str:
        with open('static/templates/participles/past passive participle.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, past_passive_participle=past_passive_participle)

    @staticmethod
    def present_tense(infinitive: str, present: str, pronoun: str, context: str) -> str:
        with open('static/templates/present/present tense.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, present=present, pronoun=pronoun, context=context)

    @staticmethod
    def present_tense_on_ona_ono(infinitive: str, present: str, context: str) -> str:
        with open('static/templates/present/present tense (on, ona, ono).html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, present=present, context=context)

    @staticmethod
    def present_tense_ony_oni(infinitive: str, present: str, context: str) -> str:
        with open('static/templates/present/present tense (ony, oni).html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, present=present, context=context)

    @staticmethod
    def past_tense(infinitive: str, past: str, pronoun: str, context: str) -> str:
        with open('static/templates/past/past tense.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, past=past, pronoun=pronoun, context=context)

    @staticmethod
    def past_perfect_tense(infinitive: str, past_perfect: str, pronoun: str, context: str) -> str:
        with open('static/templates/past/past perfect tense.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, past_perfect=past_perfect, pronoun=pronoun,
                                          context=context)

    @staticmethod
    def past_tense_ony_oni(infinitive: str, past: str, context: str) -> str:
        with open('static/templates/past/past tense (ony, oni).html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, past=past, context=context)

    @staticmethod
    def past_perfect_tense_ony_oni(infinitive: str, past_perfect: str, context: str) -> str:
        with open('static/templates/past/past perfect tense (ony, oni).html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, past_perfect=past_perfect, context=context)

    @staticmethod
    def past_tense_gender(infinitive: str, past: str, pronoun: str, gender: str, context: str) -> str:
        with open('static/templates/past/past tense (gender).html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, past=past, pronoun=pronoun, gender=gender,
                                          context=context)

    @staticmethod
    def past_perfect_tense_gender(infinitive: str, past_perfect: str, pronoun: str, gender: str, context: str) -> str:
        with open('static/templates/past/past perfect tense (gender).html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, past_perfect=past_perfect, pronoun=pronoun,
                                          gender=gender, context=context)

    @staticmethod
    def future_tense(infinitive: str, future: str, pronoun: str, context: str) -> str:
        with open('static/templates/future/future tense.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, future=future, pronoun=pronoun, context=context)

    @staticmethod
    def future_tense_on_ona_ono(infinitive: str, future: str, context: str) -> str:
        with open('static/templates/future/future tense (on, ona, ono).html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, future=future, context=context)

    @staticmethod
    def future_tense_ony_oni(infinitive: str, future: str, context: str) -> str:
        with open('static/templates/future/future tense (ony, oni).html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, future=future, context=context)

    @staticmethod
    def present_conditional(infinitive: str, present_conditional: str, pronoun: str, context: str) -> str:
        with open('static/templates/conditional/present conditional tense.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, present_conditional=present_conditional,
                                          pronoun=pronoun, context=context)

    @staticmethod
    def past_conditional(infinitive: str, past_conditional: str, pronoun: str, context: str) -> str:
        with open('static/templates/conditional/past conditional tense.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, past_conditional=past_conditional, pronoun=pronoun,
                                          context=context)

    @staticmethod
    def present_conditional_ony_oni(infinitive: str, present_conditional: str, context: str) -> str:
        with open('static/templates/conditional/present conditional tense (ony, oni).html', 'r',
                  encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, present_conditional=present_conditional,
                                          context=context)

    @staticmethod
    def past_conditional_ony_oni(infinitive: str, past_conditional: str, context: str) -> str:
        with open('static/templates/conditional/past conditional tense (ony, oni).html', 'r',
                  encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, past_conditional=past_conditional, context=context)

    @staticmethod
    def present_conditional_gender(infinitive: str, present_conditional: str, pronoun: str, gender: str,
                                   context: str) -> str:
        with open('static/templates/conditional/present conditional tense (gender).html', 'r',
                  encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, present_conditional=present_conditional,
                                          pronoun=pronoun, gender=gender, context=context)

    @staticmethod
    def past_conditional_gender(infinitive: str, past_conditional: str, pronoun: str, gender: str, context: str) -> str:
        with open('static/templates/conditional/past conditional tense (gender).html', 'r',
                  encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, past_conditional=past_conditional, pronoun=pronoun,
                                          gender=gender, context=context)

    @staticmethod
    def imperative_tense(infinitive: str, imperative: str, pronoun: str, context: str) -> str:
        with open('static/templates/imperative/imperative tense.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, imperative=imperative, pronoun=pronoun,
                                          context=context)

    @staticmethod
    def imperative_tense_on_ona_ono(infinitive: str, imperative: str, context: str) -> str:
        with open('static/templates/imperative/imperative tense (on, ona, ono).html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, imperative=imperative, context=context)

    @staticmethod
    def imperative_tense_ony_oni(infinitive: str, imperative: str, context: str) -> str:
        with open('static/templates/imperative/imperative tense (ony, oni).html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, imperative=imperative, context=context)


class Notes:
    @staticmethod
    def comma() -> str:
        with open('static/templates/notes/comma.html', 'r', encoding="utf8") as template:
            return template.read()

    @staticmethod
    def imperfect() -> str:
        with open('static/templates/notes/imperfect.html', 'r', encoding="utf8") as template:
            return template.read()

    @staticmethod
    def perfect() -> str:
        with open('static/templates/notes/perfect.html', 'r', encoding="utf8") as template:
            return template.read()

    @staticmethod
    def irregular() -> str:
        with open('static/templates/notes/irregular.html', 'r', encoding="utf8") as template:
            return template.read()

    @staticmethod
    def regular() -> str:
        with open('static/templates/notes/regular.html', 'r', encoding="utf8") as template:
            return template.read()

    @staticmethod
    def modal() -> str:
        with open('static/templates/notes/modal.html', 'r', encoding="utf8") as template:
            return template.read()

    @staticmethod
    def verb_is_translated_as(infinitive: str, translation: str) -> str:
        with open('static/templates/notes/verb is translated as.html', 'r', encoding="utf8") as template:
            return template.read().format(infinitive=infinitive, translation=translation)
