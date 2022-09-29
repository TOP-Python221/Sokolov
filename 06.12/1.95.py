def isspace(iter_text: iter) -> iter:
    for s in iter_text:
        if s.isspace():
            yield s
        else:
            yield s.upper()
            break

def upper_text(text: str) -> iter:
    iter_text = iter(text)
    yield from isspace(iter_text)
    for s in iter_text:
        yield s
        if s == '.':
            yield from isspace(iter_text)

text = " what time do i haveto be there? what’s the address? this time i’ll try to be on time!"
result = ''.join(upper_text(text))

print(result)