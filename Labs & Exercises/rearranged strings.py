# DO NOT MODIFY THE FUNCTION HEADER
# This is autograded. If the autograder cannot run your code, you will get a zero.
# Your final submission should contain no print statements as this might cause the autograder to crash.
def solution(s, t):
    s = s.replace(" ", "").lower()
    t = t.replace(" ", "").lower()         # Remove spaces and convert both strings to lowercase (assuming case doesn't matter)

    # Sort both strings and compare
    return sorted(s) == sorted(t)

