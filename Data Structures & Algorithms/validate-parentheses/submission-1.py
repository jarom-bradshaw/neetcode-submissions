class Solution:
    def isValid(self, s: str) -> bool:
        bracket_string = s
        while '()' in bracket_string or '{}' in bracket_string or '[]' in bracket_string:
            bracket_string = bracket_string.replace('()', '')
            bracket_string = bracket_string.replace('{}','')
            bracket_string = bracket_string.replace('[]','')
        return bracket_string == ''
        