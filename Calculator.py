def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return ('Error: Too many problems.')
    parts = [problem.split() for problem in problems] 
    

    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    arranged_problems = []
    sums = []
    for part in parts:
        operand1, operator, operand2 = part

        if operator in ['*', '/'] :
            return ("Error: Operator must be '+' or '-'.")


        if not operand1.isdigit() or not operand2.isdigit():
            return ('Error: Numbers must only contain digits.')

        if len(operand1) > 4 or len(operand2) > 4 :
            return ('Error: Numbers cannot be more than four digits.')

        result = None

        max_length = max(len(operand1), len(operand2)) + 2

        first_line.append(operand1.rjust(max_length))
        second_line.append(operator + operand2.rjust(max_length - 1))
        third_line.append('-' * max_length)

        first_line_str = '    '.join(first_line)
        second_line_str = '    '.join(second_line)
        third_line_str = '    '.join(third_line)

        if show_answers:
            if operator == '+':
                result = int(operand1) + int(operand2)
            else:
                result = int(operand1) - int(operand2)
            fourth_line.append(str(result).rjust(max_length))

        sums.append(result)

        arranged_problems = f"{first_line_str}\n{second_line_str}\n{third_line_str}"
        if show_answers:
            fourth_line_str = '    '.join(fourth_line)
            arranged_problems += f"\n{fourth_line_str}"
    
    return arranged_problems
        

print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')

