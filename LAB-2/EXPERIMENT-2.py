class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


def evaluate_expression(expression):
    stack = Stack()
    operators = {'+', '-', '*', '/'}

    # Split the expression by spaces
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():   # If it's a number, push to stack
            stack.push(int(token))

        elif token in operators:  # If it's an operator
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                stack.push(operand1 + operand2)

            elif token == '-':
                stack.push(operand1 - operand2)

            elif token == '*':
                stack.push(operand1 * operand2)

            elif token == '/':
                stack.push(operand1 / operand2)

    return stack.pop()


# Example usage
if __name__ == "__main__":
    expression = input("Enter a mathematical expression in postfix notation (e.g., '3 4 +'): ")
    result = evaluate_expression(expression)
    print(f"Result of the expression '{expression}': {result}")
    35