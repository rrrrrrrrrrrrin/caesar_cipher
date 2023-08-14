def core_d(letter, shift, limit, alphabet_length, text):
    letter = ord(letter) - shift
    if letter < limit:
        letter += alphabet_length
    text += chr(letter)
    return text


def core_e(letter, shift, limit, alphabet_length, text):
    letter = ord(letter) + shift
    if letter > limit:
        letter -= alphabet_length
    text += chr(letter)
    return text


if input('In what language do you want to decode/encode your text?/'
         'На каком языке вы желаете дешифровать/зашифровать ваш текст? (eng/рус): ') == 'eng':
    while True:
        shift = input('Enter the shift number: ')
        if shift.isdigit():
            shift = int(shift)
            way = input('Do you need to decode or encode your text? (d/e): ')

            for i in input('Enter your text: '):
                text = ''
                alphabet_length = 26

                if i.islower():
                    text = core_d(i, shift, 97, alphabet_length, text) if way == 'd'\
                           else core_e(i, shift, 122, alphabet_length, text)
                elif i.isupper():
                    text = core_d(i, shift, 65, alphabet_length, text) if way == 'd'\
                           else core_d(i, shift, 90, alphabet_length, text)
                else:
                    text += i

                print(text, end='')

            break
        else:
            print('Enter a number')
            continue

else:
    while True:
        shift = input('Введите шаг сдвига: ')
        if shift.isdigit():
            shift = int(shift)
            way = input('Вам необходимо дешифровать или зашифровать текст? (д/з): ')

            for i in input('Введите текст: '):
                text = ''
                alphabet_length = 32

                if i.islower():
                    text = core_d(i, shift, 1072, alphabet_length, text) if way == 'д'\
                           else core_e(i, shift, 1103, alphabet_length, text)
                elif i.isupper():
                    text = core_d(i, shift, 1040, alphabet_length, text) if way == 'д'\
                           else core_e(i, shift, 1071, alphabet_length, text)
                else:
                    text += i

                print(text, end='')

            break
        else:
            print('Введите число')
            continue
