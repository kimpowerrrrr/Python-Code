def format_name(f_name, l_name):
    """
    This function is to format the name inputted into Title Case
    """
    firstName = f_name.title()
    lastName = l_name.title()
    fullName = firstName + " " + lastName
    return fullName


full_name = format_name(f_name = "kim", l_name = "fabic")
print(f"{full_name}")