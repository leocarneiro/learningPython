def text_analyzer(string=None):
    """
    This function counts the number of upper characters, lower characters, 
    punctuation and spaces in a given text.
    """
    if string is None:
        print("What is the text to analyse?")
        string = str(input())
    character = len(string)
    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0
    for i in string:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isspace():
            spaces += 1
        elif not i.isdigit():
            punctuation += 1
    print(f"The text contains {character} characters:\n- {upper} upper letters\
            \n- {lower} lower letters\n- {punctuation} punctuation marks\
            \n- {spaces} spaces")
