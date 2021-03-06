def read(buf, n):
    ### buf: destination buffer
    ### n: maximum number of chars to read

    index = 0
    while index < n:
        buf4 = [" "]*4
        count = read4(buf4)
        if count == 0:
            break
        count = min(count, n-index)
        buf[index:] = buf4[:count]
        index += count
    return index
