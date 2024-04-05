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


def is_palindrome(str: str) -> bool:
    """
    Takes in an input string and checks whether it is a valid palindrome.

    Parameter
    ---------
    str: str

    Returns
    -------
    boolean
        True - if str is a valid palindrome
        False - if str is an invalid palindrome
    """
    #strip white spaces and punctuation
    str = str.strip().strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    #base case
    if (len(str) == 0) or (len(str) == 1):
        return True
        
    else:
      if str[0] == str[-1]:
        str = str.strip(str[0]).strip(str[-1])
        return is_palindrome(str)
          
      else:
        return False