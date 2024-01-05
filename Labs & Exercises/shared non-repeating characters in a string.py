def solution(s1, s2):
    nrc_one= set()
    rc_one= set()
    nrc_two= set()
    rc_two= set()
    shared_nrc= set()
    for i in s1:
        if i in rc_one:
            continue # Skip repeated characters
        if i in nrc_one:
            nrc_one.remove(i)
            rc_one.add(i)
        else:
            nrc_one.add(i)
    for j in s2:
        if j in rc_two:
            continue # Skip repeated characters
        if j in nrc_two:
            nrc_two.remove(j)
            rc_two.add(j)
        else:
            nrc_two.add(j)

    shared_nrc=nrc_one.intersection(nrc_two)

    return set(shared_nrc)
