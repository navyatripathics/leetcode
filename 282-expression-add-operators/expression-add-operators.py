class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        def dfs(index, path, value, prev):
            if index == len(num):
                if value == target:
                    result.append(path)
                return
            for i in range(index, len(num)):
                if i != index and num[index] == '0':
                    break               
                curr_str = num[index:i+1]
                curr_num = int(curr_str)
                if index == 0:
                    dfs(i + 1, curr_str, curr_num, curr_num)
                else:
                    dfs(i + 1, path + '+' + curr_str, value + curr_num, curr_num)
                    dfs(i + 1, path + '-' + curr_str, value - curr_num, -curr_num)
                    dfs(i + 1, path + '*' + curr_str, value - prev + prev * curr_num, prev * curr_num)

        dfs(0, "", 0, 0)
        return result
