# this is the user class

import hashlib as hl

class user:
    # instance variables
    def __init__(self, username, password, name, mobile_no):
        self.username = username
        self.password_hash = self._hash_password(password)
        self.name = name
        self.mobile_no = mobile_no

    @classmethod
    def _hash_password(cls, password):
        return hl.sha256(password.encode('utf-8')).hexdigest()
    
    def verify_password(self, password):
        return hl.sha256(password.encode('utf-8')).hexdigest() == self.password_hash


