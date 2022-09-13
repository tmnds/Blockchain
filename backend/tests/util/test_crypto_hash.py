from backend.utils.crypto_hash import crypto_hash

def test_crypto_hash():
    # It Should create the same  with arguments of different data types
    # in any order    
    assert crypto_hash(29, ['Recife', 'Pernambuco'], 'Thales') == crypto_hash('Thales', 29, ['Recife', 'Pernambuco'])
    assert crypto_hash('foo') == 'abcd'


