import hashlib

def hash256_of_int(number: int) -> str:
    """
    Receives an integer number and returns the corresponding hash for the number.
    The used algorithm is SHA-256.
    """
    number_str = str(number)
    sha256 = hashlib.sha256()
    sha256.update(number_str.encode("utf-8"))
    return sha256.hexdigest()

def is_correct_hash(hashed_number: str, difficulty: int) -> bool:
    """
    Returns true if the received hashed_number meets the conditions to be correct
    according the received difficulty.
    """
    zeros = str(0).zfill(difficulty) 
    return hashed_number[:difficulty] == zeros