def reverse(text: str) -> str:
    """
    Takes in a string (text) and reverses the text.

    Parameter
    ---------
    text: str

    Returns
    -------
    str
        text reversed
    """
    #base case
    if len(text) == 0:
      return ''
        
    else:
       return reverse(text[1:]) + text[0]


def is_palindrome(string: str) -> bool:
    """
    Takes in an input string and checks whether it is a valid palindrome.

    Parameter
    ---------
    string: str

    Returns
    -------
    boolean
        True - if str is a valid palindrome
        False - if str is an invalid palindrome
    """
    #strip white spaces and punctuation
    string = string.strip(' !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    #ensure case insesitivity
    string = string.upper()
    #base case
    if (len(string) == 0) or (len(string) == 1):
        return True
        
    else:
      if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
          
      else:
        return False