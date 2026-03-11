class Stream():
    def __init__(self, string):
        self.offset = 0
        self.string = string

    def has_more(self):
        return self.offset < len(self.string)

    def peek(self):
        if self.has_more():
            return self.string[self.offset]

    def read(self):
        if self.has_more():
            c = self.string[self.offset]
            self.offset += 1
            return c
        
class Token():
    def __init__(self, type, value):
        self.type = type
        self.value = value
        
def digit_value(c):
    #this returns the unicode string of the character - 48
    return ord(c) - 48

def lex_number(stream, c):
    n = digit_value(c)
    while (stream.has_more() and stream.peek().isdigit()):
        n *= 10
        n += digit_value(stream.read())
    return Token("NUMBER", n)

def lex_string(stream, c):
    n = str(c)
    while (stream.has_more() and stream.peek().isalpha()):
        n += stream.read()
    return Token("STRING", n)

def lex(stream):
    c = stream.read()
    if not c:
        return None
    if c == '[':
        return Token("OPEN", "[")
    if c == ']':
        return Token("CLOSE", "]")
    if c.isdigit():
        return lex_number(stream, c)
    if c.isalpha():
        return lex_string(stream, c)

def lex_all(string):
    s = Stream(string)
    lexed = []
    sym = lex(s)
    while (sym):
        lexed.append(sym)
        sym = lex(s)
    return lexed

class Literal():
    def __init__(self, value, count):
        self.value = value
        self.count = count

    def render(self):
        return self.count * self.value
        
class Sequence():
    def __init__(self, count):
        self.items = []
        self.count = count

    def render(self):
        value = ""
        for item in self.items:
            value += item.render()
        return self.count * value
        
def parse(tokens):
    stack = [Sequence(1)]
    repeat = 1
    for token in tokens:
        match (token.type):
            case "NUMBER":
                repeat = token.value
            case "STRING":
                node = Literal(token.value, repeat)
                repeat = 1
                stack[-1].items.append(node)
            case "OPEN":
                node = Sequence(repeat)
                repeat = 1
                stack.append(node)
            case "CLOSE":
                collected = stack.pop()
                if (len(stack) == 0):
                    raise ValueError("Unmatched close ']'")
                stack[-1].items.append(collected)
    if len(stack) > 1:
        raise ValueError("Unmatched open '['")
    return stack[0]

TESTS = [
    ["3[a]2[bc]", "aaabcbc",],
    ["2[abc]3[cd]ef", "abcabccdcdcdef"],
    ["3[a2[c]]", "accaccacc"]
]

if __name__ == "__main__":
    for test in TESTS:
        input = test[0]
        expect = test[1]
        print(f"pattern: {input}")
        lexed = lex_all(input)
        print(f"tokens: {[x.value for x in lexed]}")
        result = parse(lexed).render()
        print(f"evaluated to: {result}")
        if not result == expect:
            print(f"Expected {expect}, saw {result}")
        else:
            print("OK")