from colorama import Back, Fore

DEFAULT_INDENT = 8
DEFAULT_PAD_CHAR = u'—'


def make_bracket(bracket, indent=8, pad_char=u'—'):
    """
    creates a bracket text from list of rounds formatted in:
    [['teamname', <int_score>], ['teamname2', <int_score>], ...]

    :param bracket: list of rounds
    :param indent: indent count
    :param pad_char: character used for displaying indent
    :return: formatted text
    """
    indent = DEFAULT_INDENT if indent is None else indent
    pad_char = DEFAULT_PAD_CHAR if pad_char is None else pad_char
    rounds = []
    for ri, r in enumerate(bracket):
        line = []
        # manage vertical position based on round number
        if ri == 1:
            line.extend([''] * 2)
        if ri == 2:
            line.extend([''] * 6)

        for li, l in enumerate(r):
            # manage vertical position based on round order
            if not li % 2 and li:
                if ri == 0:
                    line.extend([''] * 2)
                if ri == 1:
                    line.extend([''] * 6)
            line.append(l)
        rounds.append(line)

    rows = [['', '', ''] for i in rounds[0]]
    for ri, r in enumerate(rounds):
        for i, t in enumerate(r):
            if not isinstance(t, str):
                rows[i][1] = t[0]
                rows[i][2] = t[1]
            else:
                if not rows[i][1]:
                    rows[i][0] += pad_char * indent

    for i, r in enumerate(rows):
        pad, name, score = r
        if i % 2:
            last = rows[i - 1][2]
            color = Back.GREEN if score > last else Fore.RESET
        else:
            nnext = rows[i + 1][2]
            color = Back.GREEN if score > nnext else Fore.RESET
        if isinstance(score, str):
            rows[i][1] = ''
            rows[i][0] = ''
        else:
            rows[i][1] = '{}{} {}{:10}{}{}'.format(pad, Fore.BLACK, color, name, score, Fore.RESET + Back.RESET)
    rows = [[pad, text] for (pad, text, score) in rows]
    return '\n'.join(''.join(str(i) for i in row) for row in rows)

