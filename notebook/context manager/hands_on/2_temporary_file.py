import os

# ... write the `temp_textfile` context manager here

# This code tests your context manager: it creates a temporary file,
# reads its content, and verifies that the file is deleted at the
# end of the block.
with temp_textfile('to_be_deleted.txt') as f:
    f.write('Hello world!')
    f.seek(0)
    print(f.read(5))

assert not os.path.exists('to_be_deleted.txt')
