import requests
import json
import logging
from bip39 import bip39_to_mini_secret, bip39_generate, bip39_validate
import bip39
from nacl.signing import SigningKey

class MnemonicLanguageCode:
    ENGLISH = 'en'
    CHINESE_SIMPLIFIED = 'zh-hans'
    CHINESE_TRADITIONAL = 'zh-hant'
    FRENCH = 'fr'
    ITALIAN = 'it'
    JAPANESE = 'ja'
    KOREAN = 'ko'
    SPANISH = 'es'

class Keypair:

    def __init__(self):
        pass

    @classmethod
    def generate_mnemonic(cls, words: int = 12, language_code: str = MnemonicLanguageCode.ENGLISH) -> str:
        """
        Generates a new seed phrase with given amount of words (default 12)
        Parameters
        ----------
        words: The amount of words to generate, valid values are 12, 15, 18, 21 and 24
        language_code: The language to use, valid values are: 'en', 'zh-hans', 'zh-hant', 'fr', 'it', 'ja', 'ko', 'es'. Defaults to `MnemonicLanguageCode.ENGLISH`
        Returns
        -------
        str: Seed phrase
        """
        return bip39_generate(words, language_code)

    @classmethod
    def validate_mnemonic(cls, mnemonic: str, language_code: str = MnemonicLanguageCode.ENGLISH) -> bool:
        """
        Verify if specified mnemonic is valid
        Parameters
        ----------
        mnemonic: Seed phrase
        language_code: The language to use, valid values are: 'en', 'zh-hans', 'zh-hant', 'fr', 'it', 'ja', 'ko', 'es'. Defaults to `MnemonicLanguageCode.ENGLISH`
        Returns
        -------
        bool
        """
        return bip39_validate(mnemonic, language_code)

    @classmethod
    def create_from_mnemonic(cls, mnemonic: str,  language_code: str = MnemonicLanguageCode.ENGLISH) -> 'Keypair':
        """
        
        """
        private_key = bip39.decode_phrase(mnemonic)
        hex_private_key = private_key.hex()
        public_key = SigningKey(mnemonic).verify_key.encode().hex()

        return cls(private_key=private_key, hex_private_key=hex_private_key, public_key=public_key)

a = Keypair.create_from_mnemonic('design guide gasp train traffic slight mansion aware notice home cute season')
print(a)



    
