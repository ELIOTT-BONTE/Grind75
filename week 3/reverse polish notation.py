class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for t in tokens:
            if t == "+":
                term2 = stack.pop()
                term1 = stack.pop()
                termRes = term1 + term2
                stack.append(termRes)
            elif t == "-":
                term2 = stack.pop()
                term1 = stack.pop()
                termRes = term1 - term2
                stack.append(termRes)
            elif t == "/":
                term2 = stack.pop()
                term1 = stack.pop()
                termRes = int(float(term1) / term2)  # Ensure correct integer truncation towards zero
                stack.append(termRes)
            elif t == "*":
                term2 = stack.pop()
                term1 = stack.pop()
                termRes = term1 * term2
                stack.append(termRes)
            else:
                stack.append(int(t))

        return stack.pop()
