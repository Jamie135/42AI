class Account(object):
    ID_COUNT = 1

    # kwargs est un dictionnaire qui contient les attributs additionnels 
    # (paires cles-valeurs) qu'on pourrait vouloir ajouter à l'instance
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        #hasattr vérifie si l'attribut value existe déjà pour l'instance
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
    

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""

    def __init__(self):
        self.accounts = []


    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occurred
        """
        if not isinstance(new_account, Account):
            return False
        for a in self.accounts:
            if (a.name == new_account.name):
                return False
        if self.corrupted(new_account):
            return False
        self.accounts.append(new_account)
        return True


    def transfer(self, origin, dest, amount):
        """ Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occurred
        """

        origin_acc = None
        dest_acc = None
        for a in self.accounts:
            if a.name == origin:
                origin_acc = a
            if a.name == dest:
                origin_acc = a

        if origin_acc is None or dest_acc is None:
            return False

        if self.corrupted(origin_acc) or self.corrupted(dest_acc):
            return False

        if amount < 0 or origin_acc.value < amount:
            return False

        if origin_acc == dest_acc:
            return True
        
        origin_acc.value -= amount
        dest_acc.value += amount
        return True
        

    def fix_account(self, name):
        """ Fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occurred
        """
        account = None
        for a in self.accounts:
            if a.name == name:
                account = a

        if account is None:
            return False
        
        if not isinstance(name, str):
            return False
        
        fixed = False
        # Fix name, id, and value
        if not hasattr(account, 'name') or not isinstance(account.name, str):
            account.name = name
            fixed = True
        if not hasattr(account, 'id') or not isinstance(account.id, int):
            account.id = Account.ID_COUNT
            Account.ID_COUNT += 1
            fixed = True
        if not hasattr(account, 'value') or not isinstance(account.value, (int, float)):
            account.value = 0
            fixed = True
        
        # Remove attributes starting with 'b'
        for attr in dir(account):
            if attr.startswith('b'):
                delattr(account, attr)
                fixed = True
        
        # Ensure there's an attribute starting with 'zip' or 'addr'
        if not any(attr.startswith('zip') or attr.startswith('addr') for attr in dir(account)):
            account.zip = '00000'
            fixed = True
        
        # Ensure the number of attributes is odd
        if len(dir(account)) % 2 == 0:
            if hasattr(account, 'temp'):
                delattr(account, 'temp')
            else:
                account.temp = 'temporary attribute'
            fixed = True
        
        return fixed
        

    def corrupted(self, account):
        # dir() returns the list of valid attributes of the passed object
        attribute = dir(account)

        if len(attribute) % 2 == 0:
            return True
        zipaddr = False
        for a in attribute:
            if a.startswith('b'):
                return True
            if a.startswith('zip') or a.startswith('addr'):
                zipaddr = True
        if not zipaddr:
            return True
        for a in ['name', 'id', 'value']:
            if not hasattr(account, a):
                return True
        if not isinstance(account.name, str):
            return True
        if not isinstance(account.id, int):
            return True
        if not isinstance(account.value, (int, float)):
            return True
        
        return False
