import re
import logging

from pathlib import Path
from collections import defaultdict
from typing import List, Dict

logger = logging.getLogger(__name__)


class OpcodeParser:
    def __init__(self):
        self.mnemonic_indexer = defaultdict(int)
        self.mnemonics: List = []
        self.valid_api: List = []
        self.valid_dll: List = []
        self.abs_path: str = str(Path.cwd())

        if 'Parser' not in self.abs_path:
            self.abs_path += '/Parser'

        self._load_mnemonics()
        self._load_api_dictionary()
        self._load_dll_dictionary()

    def _load_mnemonics(self):
        """Load all possible mnemonics from the file"""
        file_path = Path(self.abs_path) / '..' / 'data' / 'Mnemonics.txt'

        with open(file_path, 'r') as file:
            self.mnemonics = [
                line.strip('\n').lower() for line in file
            ]
            self.mnemonic_indexer = defaultdict(
                int, {
                    mnemonic[0]: idx for idx, mnemonic in enumerate(self.mnemonics)
                }
            )

    def _load_api_dictionary(self):
        """Load the API dictionary"""
        file_path = Path(self.abs_path) / '..' / 'data' / 'API_Dictionary.txt'
        with open(file_path, 'r') as file:
            self.valid_api = file.read().split('\n')

    def _load_dll_dictionary(self):
        """Load the DLL dictionary"""
        file_path = Path(self.abs_path) / '..' / 'data' / 'DLL_Dictionary.txt'
        with open(file_path, 'r') as file:
            self.valid_dll = file.read().split('\n')

    @staticmethod
    def add_to_hash_table(key: str, hash_table: Dict[str, int]):
        """Add a key to the hash table"""
        hash_table[key] += 1

    def is_valid_opcode(self, opcode: str) -> bool:
        """Check if the given opcode is valid"""
        opcode = opcode.lower()
        start = self.mnemonic_indexer[opcode[0]]

        for mnemonic in self.mnemonics[start:]:
            if opcode == mnemonic:
                return True

            elif opcode[0] < mnemonic[0] or opcode[1] < mnemonic[1]:
                return False

        return False

    @staticmethod
    def is_stop_word(opcode: str) -> bool:
        """Check if the given opcode is a stop word"""
        STOP_WORDS = [
            'call', 'jmp', 'ret', 'iret', 'iretd', 'iretw', 'int', 'into', 'leave', 'retf', 'retn', 'je',
            'jz', 'jcxz', 'jp', 'jpe', 'jne', 'jnz', 'jecxz', 'jnp', 'jpo', 'ja', 'jae', 'jb', 'jbe', 'jna',
            'jnae', 'jnbe', 'jc', 'jnc', 'jg', 'jge', 'jl', 'jle', 'jng', 'jnge', 'jnl', 'jnle', 'jo', 'jno',
            'js', 'jns'
        ]
        return opcode in STOP_WORDS

    @staticmethod
    def export_data_to_csv(data_dict: Dict[str, int], export_file: str):
        """Export the data dictionary to a CSV file.

        Args:
            data_dict (Dict[str, int]): The data dictionary to export.
            export_file (str): The path of the export file.

        Raises:
            IOError: If there is an error while writing to the export file.
        """
        try:
            with open(export_file, 'w+') as file:
                for key, value in data_dict.items():
                    file.write(f"{key},{value}\n")

            logger.info("Data Exported Successfully")

        except IOError as e:
            logger.error(f"Error exporting data to CSV: {str(e)}")

    @staticmethod
    def export_list_to_csv(data_list: List[str], export_file: str):
        """Export the data list to a CSV file.

        Args:
            data_list (List[str]): The data list to export.
            export_file (str): The path of the export file.

        Raises:
            IOError: If there is an error while writing to the export file.
        """
        try:
            with open(export_file, 'w+') as file:
                for item in data_list:
                    file.write(f"{item}\n")

            logger.info("Data Exported Successfully")

        except IOError as e:
            logger.error(f"Error exporting data to CSV: {str(e)}")

    @staticmethod
    def export_list_to_txt(data_list: List[str], export_file: str):
        """Export the data list to a text file.

        Args:
            data_list (List[str]): The data list to export.
            export_file (str): The path of the export file.

        Raises:
            IOError: If there is an error while writing to the export file.
        """
        try:
            with open(export_file, 'w+') as file:
                for item in data_list:
                    file.write(f"{item}\n")

            logger.info("Data Exported Successfully")

        except IOError as e:
            logger.error(f"Error exporting data to TXT: {str(e)}")

    def import_opcodes_to_list(self, file_name: str) -> List[str]:
        """Import opcodes from a file to a list.

        Args:
            file_name (str): The path of the file to import opcodes from.

        Returns:
            List[str]: The list of imported opcodes.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        if not self.mnemonics:
            self._load_mnemonics()
        opcodes = []

        try:
            with open(file_name, 'r') as file:
                for line in file:
                    opcodes.extend(re.findall(r'\b[A-F0-9]{2}\b', line))
            return opcodes

        except FileNotFoundError as exc:
            logger.error(f"File not found: {str(exc)}")
            raise exc
