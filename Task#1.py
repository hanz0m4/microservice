def palindrome(s1):
    reverse = ''.join(reversed(s1))
    if s1 == reverse:
        return "Строка является палиндромом"
    return "Строка не является палиндромом"


s1 = input("Введите желаемую строку: ")


print(palindrome(s1))
