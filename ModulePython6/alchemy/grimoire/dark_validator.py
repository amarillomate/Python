from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    lowed_ingredients = ingredients.lower()
    is_true = any(ing in lowed_ingredients for ing in allowed)
    if is_true:
        status = "VALID"
    else:
        status = "INVALID"
    return f"{ingredients} - {status}"
