def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    return ' '.join([word[::-1] for word in s.split(' ')])

if __name__ == '__main__':
    print(reverseWords("Let's take LeetCode contest"))
