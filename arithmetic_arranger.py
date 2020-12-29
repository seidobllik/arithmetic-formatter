def arithmetic_arranger(problems, show_solution=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    formatted = {'top': [], 'bottom': [], 'line': [], 'result': []}

    for s in problems:
        s = s.split()

        if s[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        try:
            int(s[0])
            int(s[2])
        except ValueError:
            return "Error: Numbers must only contain digits."

        if len(s[0]) > 4 or len(s[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        top = s[0]
        operator = s[1]
        bottom = s[2]
        width = (len(top) + 2
                 if len(top) + 2 > len(bottom) + 2 else len(bottom) + 2)
        line = '-' * (width)
        result = str(eval(top + operator + bottom))

        formatted['top'].append(top.rjust(width))
        formatted['bottom'].append(operator + bottom.rjust(width - 1))
        formatted['line'].append(line)
        formatted['result'].append(result.rjust(width))

    result = '    '.join(formatted['top']) + '\n' + '    '.join(
        formatted['bottom']) + '\n' + '    '.join(
            formatted['line']) + ('' if show_solution is not True else
                                  ('\n' + '    '.join(formatted['result'])))

    return result
