class Solution:
    def isValid(self, s: str) -> bool:
        pilha = []

        for char in s:
            if char in "({[":
                pilha.append(char)
            else:
                match char:
                    case ")":
                        if pilha and pilha[-1] == "(":
                            pilha.pop()
                        else:
                            pilha.append(char)
                    case "}":
                        if pilha and pilha[-1] == "{":
                            pilha.pop()
                        else:
                            pilha.append(char)
                    case "]":
                        if pilha and pilha[-1] == "[":
                            pilha.pop()
                        else:
                            pilha.append(char)
                    case _:
                        continue

        return len(pilha) == 0
