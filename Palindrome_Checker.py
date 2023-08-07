def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def main():
    user_input = input("Enter a string: ")
    final = is_palindrome(user_input)
    print(final)

if __name__ == "__main__":
    main()
