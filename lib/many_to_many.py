class Author:

    all = []

    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if contract.author == self])

class Book:
    
    all = []

    def __init__(self, title):
        self.title = title
        Book.add_book_to_all(self)
    
    @classmethod
    def add_book_to_all(cls, book):
        cls.all.append(book)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self ]


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author):
            self.author = author
        else:
            raise Exception
        if isinstance(book, Book):
            self.book = book
        else:
            raise Exception
        if type(date) == str:
            self.date = date
        else:
            raise Exception
        if type(royalties) == int:
            self.royalties = royalties
        else:
            raise Exception
        Contract.add_contract_to_all(self)
    
    @classmethod
    def add_contract_to_all(cls, contract):
        cls.all.append(contract)
    
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]