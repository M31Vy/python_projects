def main(digits):
    if not digits:
            return []
    phone_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    def helper(digits, path, phone_map, ans):
        if not digits:
            ans.append(path)
        else: 
            for c in phone_map[digits[0]]:
                helper(digits[1:], path + c, phone_map, ans)

    ans = []
    helper(digits, '', phone_map, ans)
    return ans

if __name__ == '__main__':
    print(main('23'))
    print(main(''))
    print(main('2'))
    print(main('234'))
    print(main('2345'))