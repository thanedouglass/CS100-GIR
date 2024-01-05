def solution(word):
    nrc= set()
    rc= set()
    for i in word:
        if i in rc:
            continue # Skip repeated characters
        if i in nrc:
            nrc.remove(i)
            rc.add(i)
        else:
            nrc.add(i)
    return nrc
