import filecmp
import os
import pytest
import helper
from main import guess_key, xor_decrypt, filter_matches
from documentation import assertion_manager


@pytest.mark.sanity
def test_xor_decrypt():
    """This is a sanity test that checks if xor_decrypt working as expected (from qspark example)"""
    assert xor_decrypt([24, 24, 26, 30, 28], "yz") == "abcde", assertion_manager.xor_decrypt_assertion_message()


@pytest.mark.sanity
def test_xor_decrypt_with_empty_string_and_empty_key():
    """Decrypt an empty string with an empty key"""
    encrypted_text = b''
    key = ''
    expected_output = ''
    assert xor_decrypt(encrypted_text, key) == expected_output, assertion_manager.xor_decrypt_assertion_message()


@pytest.mark.sanity
def test_guess_key_error_handling_check_if_key_is_0():
    """This test checks the error handling in guess_key - we are now allowed that the key will be 0!!"""
    with pytest.raises(ValueError):
        encrypted_text = [1, 2, 3]
        key_size = 0
        guess_key(encrypted_text, key_size)


@pytest.mark.sanity
def test_guess_key_error_handling_check_if_the_encrypted_text_is_a_list_of_integers():
    """This test checks the error handling in guess_key - the list must be int!!"""
    with pytest.raises(ValueError):
        encrypted_text = ["1", "2", "3"]
        key_size = 0
        guess_key(encrypted_text, key_size)


@pytest.mark.sanity
def test_guess_key_error_handling_check_if_the_encrypted_text_length():
    """This test checks the error handling in guess_key -encrypted_text length is at least key_size!!"""
    with pytest.raises(ValueError):
        encrypted_text = [1, 2, 3]
        key_size = 88
        guess_key(encrypted_text, key_size)


@pytest.mark.sanity
def test_guess_key_with_non_string_word():
    """Test case with a non-string word"""
    with pytest.raises(TypeError):
        guess_key(['apple', 'banana', 'carrot', 'grape', 123])


@pytest.mark.functionality
def test_guess_key():
    with open('test_data/cipher.txt', 'r') as f:
        encrypted_text = [int(x) for x in f.read().strip().split(',')]
    key_size = 3
    matches = guess_key(encrypted_text, key_size)
    "This test checks the number of the possible key matches"
    assert len(matches) == 504
    "This test checks that all the keys that returned are strings as we expected from our method"
    assert all(isinstance(match[0], str) for match in matches)
    "This test checks that each pair key-text that was returned is string as we expected from our method"
    assert all(isinstance(match[1], str) for match in matches)


@pytest.mark.functionality
def test_filter_matches():
    matches = [('abc', 'hello world'), ('def', 'lorem ipsum')]
    filtered_matches = filter_matches(matches)
    assert len(filtered_matches) == 1
    assert filtered_matches[0][0] == 'abc'
    assert filtered_matches[0][1] == 'hello world'
    matches = [('abc', 'hello עולם'), ('def', 'lorem ipsum')]
    filtered_matches = filter_matches(matches)
    assert len(filtered_matches) == 0


@pytest.mark.functionality
def test_that_check_the_cipher_text():
    helper.actual_result_from_cipher_text()
    f1 = os.path.join("test_data", "expected_result.txt")
    f2 = os.path.join("test_data", "actual_result.txt")
    result = filecmp.cmp(f1, f2, shallow=False)
    assert result, "we didn't found the exact output"


def teardown_function():
    # The f_teardown() function removes the actual_result.txt file, if it was created.
    files = os.listdir(os.path.join("test_data"))
    if 'actual_result.txt' in files:
        os.remove(os.path.join("test_data", "actual_result.txt"))
