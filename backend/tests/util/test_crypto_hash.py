from backend.utils.crypto_hash import crypto_hash

def test_crypto_hash():
    # It Should create the same  with arguments of different data types
    # in any order    
    assert crypto_hash(29, ['Recife', 'Pernambuco'], 'Thales') == crypto_hash('Thales', 29, ['Recife', 'Pernambuco'])
    assert crypto_hash('foo') == 'b2213295d564916f89a6a42455567c87c3f480fcd7a1c15e220f17d7169a790b'


