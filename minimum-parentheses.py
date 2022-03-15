class MinParenthesisRemover:
  def minRemoveToMakeValid(self, s: str) -> str:
        remove_ind = set()
        stack_ind = []
        for ind, char in enumerate(s):
            if char not in "()":
                continue
            if char == "(":
                stack_ind.append(ind)
            elif stack_ind == []:
                remove_ind.add(ind)
            else:
                stack_ind.pop()
        remove_ind = remove_ind.union(set(stack_ind))
        output = ""
        for ind, char in enumerate(s):
            if ind in remove_ind:
                continue
            output+=char
        return output