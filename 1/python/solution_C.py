import ply.lex as lex
import ply.yacc as yacc

W_DIGIT_DICT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def duplicate_w_digits(text: str):
    # we duplicate written digits to be sure
    # to always parse the last and first, even
    # if they overlap
    for k in W_DIGIT_DICT.keys():
        text = text.replace(k, k + k)
    return text


def extract_number_from_line(line_digits: list[str]):
    return int(line_digits[0] + line_digits[-1])


class MyLexer(object):
    tokens = ("DIGIT", "W_DIGIT", "LETTER", "NEWLINE")

    t_LETTER = r"[a-z]"
    t_DIGIT = r"\d"
    t_NEWLINE = r"\n"

    def t_W_DIGIT(self, t):
        "(one|two|three|four|five|six|seven|eight|nine)"
        t.value = str(W_DIGIT_DICT[t.value])
        return t

    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def t_error(self, t):
        print("Token error:", t)


class MyParser(object):
    tokens = MyLexer.tokens

    def p_expression_lines(self, t):
        """
        expression : expression NEWLINE line
                   | line
        """
        if len(t) == 2:
            t[0] = extract_number_from_line(t[1])
        elif len(t) == 4:
            t[0] = t[1] + extract_number_from_line(t[3])

    def p_line_digit(self, t):
        """
        line : line digit
             | digit
        """
        if len(t) == 2:
            t[0] = [t[1]]
        elif len(t) == 3:
            t[0] = t[1] + [t[2]]

    def p_line_letter(self, t):
        """
        line : line LETTER
             | LETTER
        """
        if len(t) == 2:
            t[0] = []
        elif len(t) == 3:
            t[0] = t[1]

    def p_digit_digit(self, t):
        """
        digit : DIGIT
              | W_DIGIT
        """
        t[0] = t[1]

    def __init__(self):
        self.lexer = MyLexer()
        self.parser = yacc.yacc(module=self, debug=True)


p = MyParser()

with open("input.txt", "r") as f:
    text = f.read()
    text = duplicate_w_digits(text)
    res = p.parser.parse(text)
    print(res)
