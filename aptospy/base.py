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

chain_url = {
    'devnet': 'https://fullnode.devnet.aptoslabs.com',
    'local': 'http://127.0.0.1:8080'
}

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

    # @classmethod
    # def create_from_mnemonic(cls, mnemonic: str,  language_code: str = MnemonicLanguageCode.ENGLISH) -> 'Keypair':
    #     """
        
    #     """
    #     private_key = bip39.decode_phrase(mnemonic)
    #     hex_private_key = private_key.hex()
    #     public_key = SigningKey(mnemonic).verify_key.encode().hex()

    #     return cls(private_key=private_key, hex_private_key=hex_private_key, public_key=public_key)

class Aptos:

    def __init__(self, url=None, chain=None):
        """
        
        """
        if (not url and not chain) or (url and chain):
            raise ValueError("Either 'url' or 'chain' must be provided")
        elif url:
            self.url = url
        elif chain:
            self.url = chain_url[chain]
        self.session = requests.Session()
    
    def get_version(self):
        self._version = self.session.get(self.url)
        return self._version.json()

    def get_transactions(self, start=None, limit=None):
        if start:
            self._transactions = self.session.get(f'{self.url}/transactions?start={start}')
        elif limit:
            self._transactions = self.session.get(f'{self.url}/transactions?limit={limit}')
        elif (start and limit):
            self._transactions = self.session.get(f'{self.url}/transactions?limit={limit}&start={start}')
        else:
            self._transactions = self.session.get(f'{self.url}/transactions')
        return self._transactions.json()

    def get_transaction(self, txn_hash_or_version: str or int):
        self._transaction = self.session.get(f'{self.url}/transactions/{txn_hash_or_version}')
        return self._transaction.json()

    def get_account_transactions(self, address: str):
        self._account_transactions = self.session.get(f'{self.url}/accounts/{address}/transactions')
        return self._account_transactions.json()

    def get_account(self, address: str):
        self._account = self.session.get(f'{self.url}/accounts/{address}')
        return self._account.json()

    def get_account_resources(self, address: str):
        self._account_resources = self.session.get(f'{self.url}/accounts/{address}/resources')
        return self._account_resources.json()

    def get_account_resource(self, address: str, resource_type: str):
        self._account_resource = self.session.get(f'{self.url}/accounts/{address}/resource/{resource_type}')
        return self._account_resource.json()

    def get_account_modules(self, address: str):
        self._account_modules = self.session.get(f'{self.url}/accounts/{address}/modules')
        return self._account_modules.json()

    def get_account_module(self, address: str, module_name: str):
        self._account_module = self.session.get(f'{self.url}/accounts/{address}/module/{module_name}')
        return self._account_module.json()

    def get_events_by_key(self, event_key: str):
        self._events = self.session.get(f'{self.url}/events/{event_key}')
        return self._events.json()

    def get_events_by_handle(self, address: str, event_handle_struct: str, field_name: str):
        self._events = self.session.get(f'{self.url}/accounts/{address}/events/{event_handle_struct}/{field_name}')
        return self._events.json()


    
