#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Encrypting passwords """
    p = password.encode()
    return bcrypt.hashpw(p, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if password matches hashed password."""
    if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
        return True
    else:
        return False
