def process_string(text):
    """Throws an exception if the string contains other than alphabet
       letters and white spaces
       Converts all string letters to uppercase an returns the string
    """
    if not all(x.isalpha() or x.isspace() for x in text):
        raise ValueError("Only letters and white spaces are aloud")
    text = text.upper()
    return text
