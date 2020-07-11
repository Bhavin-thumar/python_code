# Always use context manager 'with' statement for file operation as it automatically close the file after the
# indentation block gets over.
# file can be used as iterable. It can be converted to other iterable(list,set,tuple) also, except dictionary.

with open(r"C:\Users\hardip thummar\Documents\Python Scripts\test.txt", mode='r+', encoding='utf-8') as f:
    with open(r"C:\Users\hardip thummar\Documents\Python Scripts\test2.txt", mode='r+', encoding='utf-8') as nf:
        # print(f.readline(), end='')                           # It read one line
        # print(f.readline(), end='')                           # It read another line
        # print(f.read())                                       # It read rest of file
        # cursor_position = f.tell()                            # It tells current position of cursor
        # f.write("11. This is end of file.")                   # It writes to file
        # f.truncate(cursor_position)                           # It delete file content from that position
        # f.write('\n11. This is end of file....')
        # print(f.seek(cursor_position))                        # It bring cursor back to that position
        # f.write('hi')
        for line in f:
            for word in line.split():
                if word == 'is':
                    nf.write(f' {word} it')
                else:
                    nf.write(f' {word}')
            nf.write('\n')