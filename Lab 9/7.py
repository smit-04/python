def ispalindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(ispalindrome("Nurses run"))