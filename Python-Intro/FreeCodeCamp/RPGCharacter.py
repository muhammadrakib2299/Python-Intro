def create_character(name, strength, intelligence, charisma):
    # 1. Validate the Name
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"

    # 2. Validate Stat Types
    # We use type() to ensure they aren't booleans (True/False)
    if type(strength) is not int or type(intelligence) is not int or type(charisma) is not int:
        return "All stats should be integers"

    # 3. Validate Stat Ranges
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    
    # 4. Validate Point Total
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"

    # 5. Format the Output
    # Create the bars using string multiplication
    str_bar = "●" * strength + "○" * (10 - strength)
    int_bar = "●" * intelligence + "○" * (10 - intelligence)
    cha_bar = "●" * charisma + "○" * (10 - charisma)

    return f"{name}\nSTR {str_bar}\nINT {int_bar}\nCHA {cha_bar}"


print(create_character('ren', 4, 2, 1))