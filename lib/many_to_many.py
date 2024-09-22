class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [ contract for contract in Contract.all if contract.author == self ]
            # what we want    var name    list              conditional

    def books(self):
        return [ contract.book for contract in Contract.all if contract.author == self ]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        # get all my contracts
        # self_contracts = self.contracts()
        # # get all the royalties
        # self_royalties = [ contract.royalties for contract in self_contracts ]
        # # return the sum of all author's royalties
        # return sum(self_royalties)
        return sum( [ contract.royalties for contract in self.contracts() ] )

class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [ contract for contract in Contract.all if contract.book == self ]

    def authors(self):
        return [ contract.author for contract in Contract.all if contract.book == self ]

class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    # AUTHOR PROPERTY
    @property # GETTER
    def author(self):
        return self._author
    
    @author.setter # SETTER
    def author(self, new_author):
        if new_author in Author.all:
            self._author = new_author
        else:
            raise Exception("Invalid author")
    
    # BOOK PROPERTY
    @property # GETTER
    def book(self):
        return self._book
    
    @book.setter # SETTER
    def book(self, new_book):
        if new_book in Book.all:
            self._book = new_book
        else:
            raise Exception("Invalid book")
        
    # DATE PROPERTY
    @property # GETTER
    def date(self):
        return self._date
    
    @date.setter # SETTER
    def date(self, new_date):
        if isinstance(new_date, str):
            self._date = new_date
        else:
            raise Exception("Invalid date")
        
    @property # GETTER
    def royalties(self):
        return self._royalties
    
    @royalties.setter # SETTER
    def royalties(self, new_royalties):
        if isinstance(new_royalties, int):
            self._royalties = new_royalties
        else:
            raise Exception("Invalid royalties")
    
    @classmethod
    def contracts_by_date(cls, date):
        # cls == Contract
        # return all contracts of the given date
        return [ contract_instance for contract_instance in cls.all if contract_instance.date == date ]