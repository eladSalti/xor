from main import guess_key, filter_matches
#
def actual_result_from_cipher_text():
    with open('test_data/cipher.txt', 'r') as f:
        encrypted_text = [int(x) for x in f.read().strip().split(',')]

    matches = guess_key(encrypted_text, 3)
    filtered_matches = filter_matches(matches)

    for key, decrypted_text in filtered_matches:
        with open('test_data/actual_result.txt', 'a') as file:
            file.write('Key: ' + key + '\n' + 'Decrypted text: ' + decrypted_text)


