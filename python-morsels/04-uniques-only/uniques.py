def uniques_only(it):
    uni = set()
    uni_add = uni.add
    for i in it:
        if i not in uni:
            uni_add(i)
            yield i
