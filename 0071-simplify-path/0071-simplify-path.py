class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for i in path:
            if i == '..':
                if stack:
                    stack.pop()
            elif i != '.' and i != '':
                stack.append(i)
        return '/' + '/'.join(stack)
       