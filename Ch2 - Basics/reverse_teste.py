def is_palindrome(teststr):
    # Convert to lower case
    temp = teststr.lower()

    # Strip spaces and punctuation
    newstr = ''
    for c in temp:
        if c.isalnum():
            newstr += c

    # Calculate the reversed string
    reversed_str = newstr[::-1]

    return newstr == reversed_str

