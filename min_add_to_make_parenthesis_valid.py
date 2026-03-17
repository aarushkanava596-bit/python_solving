class Solution:
    def minParentheses(self, s):
        balance = 0
        insertions = 0
        for char in s:
            if char == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    insertions += 1
        return insertions + balance
