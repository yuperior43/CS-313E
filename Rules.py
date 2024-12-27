def follows_rule(s, r):
    question_count = 0
    r_letters = []
    r_characters = [letter for letter in r]
    s_letters = [letter for letter in s]

    for letter in r:
        if letter == '?':
            question_count += 1
        elif letter == '*':
            r_characters.remove(letter)
        elif letter not in ('?', '*'):
            r_letters.append(letter)

    available_letters = len(s_letters) - question_count

    if len(s) < question_count:
        return False
    if available_letters < len(r_letters):
        return False

    used_letters = []
    for letter in range(len(r_letters)):
        if r_characters[letter] == '?':
            if s_letters[letter] not in used_letters:
                used_letters.append(s_letters[letter])
            else:
                return False
        elif r_characters[letter] != s_letters[letter]:
            return False

    return True
    

def main():
    s = input()
    r = input()

    print(follows_rule(s,r))

if __name__ == '__main__':
    main()
