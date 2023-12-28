def lz77_encode(message):
    encoded_message = []
    buffer = ''
    index = 0

    while index < len(message):
        match = find_longest_match(buffer, message[index:])
        if match:
            offset, length = match
            next_char = message[index + length] if index + length < len(message) else ''
            encoded_message.append((offset, length, next_char))
            print(f'Буфер поиска: {buffer} | Буфер для предварительной записи сообщения: {message[index:]} | Кодовое слово: ({offset}, {length}, {next_char})')
            buffer += message[index:index + length + 1]
            index += length + 1
        else:
            encoded_message.append((0, 0, message[index]))
            print(f'Буфер поиска: {buffer} | Буфер для предварительной записи сообщения: {message[index:]} | Кодовое слово: (0, 0, {message[index]})')
            buffer += message[index]
            index += 1

    return encoded_message


def find_longest_match(buffer, remaining):
    max_offset = 0
    max_length = 0

    for offset in range(1, len(buffer) + 1):
        for length in range(1, len(remaining) + 1):
            if remaining[:length] == buffer[-offset:][:length]:
                if length >= max_length:
                    max_offset = offset
                    max_length = length
            else:
                break

    return max_offset, max_length


def lz77_decode(encoded_message):
    decoded_message = ''
    search_buffer = ''

    for offset, length, next_char in encoded_message:
        if offset == 0:
            decoded_message += next_char
            print(f'Кодовое слово: (0, 0, {next_char}) | Буфер поиска: {search_buffer} | Сообщение: {next_char}')
            search_buffer += next_char
        else:
            start = len(decoded_message) - offset
            end = start + length
            decoded_word = decoded_message[start:end] + next_char
            decoded_message += decoded_word
            print(f'Кодовое слово: ({offset}, {length}, {next_char}) | Буфер поиска: {search_buffer} | Сообщение: {decoded_word}')
            search_buffer += decoded_word
    print(f'Кодовое слово: - | Буфер поиска: {search_buffer} | Сообщение: - ')

    return decoded_message


def print_output(message):
    print(' ======================= ВХОДНЫЕ ДАННЫЕ ======================== ')
    print(message, end='\n\n')

    print(' ======================== КОДИРОВАНИЕ ========================== ')
    encoded_message = lz77_encode(message)
    print(f'\nКод -> {encoded_message}\n')

    print(' ======================= ДЕКОДИРОВАНИЕ ========================= ')
    decoded_message = lz77_decode(encoded_message)
    print(f'\nДекодированное сообщение -> {decoded_message}\n\n')
