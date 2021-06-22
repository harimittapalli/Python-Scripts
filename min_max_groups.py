def group(L):
    first = last = L[0]
    for n in L[1:]:
        if n - 1 == last: # Part of the group, bump the end
            last = n
        else: # Not part of the group, yield current group and start a new
            yield first, last
            first = last = n
    yield first, last # Yield the last group


if __name__ == "__main__":
    x = [2, 3, 4, 5, 6, 6, 7, 12, 13, 14, 15, 16, 17, 22, 25, 26, 28, 51, 52, 57]
    print(list(group(x)))