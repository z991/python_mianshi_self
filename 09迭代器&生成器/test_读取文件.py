def myreadlines(f, newline):
    buf = ""
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        chunck = f.read(10)

        if not chunck:
            #说明已经读取到了文件末尾
            yield buf
            break
        buf = buf + chunck

with open("input.txt") as f:
    for line in myreadlines(f, "{|}"):
        print (line)