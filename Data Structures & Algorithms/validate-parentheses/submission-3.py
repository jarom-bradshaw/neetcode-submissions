class Solution:
    def isValid(self, s: str) -> bool:
        # The idea here is that we take a list and we only append opening brackets to the end of it. If we see a opening bracket, we add it to the list. And then the idea is that there should only be opening brackets at the beginnging  "[{]}" would be invalid, but "[{}]" would be valid if that makes sense, or "[]{}" would be valid, but in this case, we add the "[" to the end of the list and check for the next character to be a "]". If it is, we never added it in the first place, so we just remove the connected beginning bracket, which will be at the end of the list. And then if it doesn't match, but is an opening bracket, than we just add it to the end of the list. If it doesn't match and is a closing rbacket, than we return False, because it doesn't match.
        stack = []
        closeToOpen = { ")": "(", "]": "[", "}": "{" }
        bracket_str = s
        for char in bracket_str:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
                    