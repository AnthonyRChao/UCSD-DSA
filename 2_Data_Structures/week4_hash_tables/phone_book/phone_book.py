# python3

class PhoneBook:
    """A simple phone book manager implementation using the direct
    addressing scheme."""

    def __init__(self):
        self.book= [None] * (10 ** 7)

    def add(self, number, name):
        """Adds name and number to book.

        If there exists a name with number, overwrite name.
        """
        self.book[number] = name

    def delete(self, number):
        """Deletes number from book if number exists.

        Otherwise, ignore query."""
        if self.book[number] is not None:
            self.book[number] = None

    def find(self, number):
        """Look for a person with provided number.

        If found, return with appropriate name, otherwise return
        string "not found" (without quotes).
        """
        if self.book[number] is None:
            return "not found"
        return self.book[number]



def process_queries(queries):
    """Helper function to process provided queries."""
    for query in queries:
        q = query.split()
        cmd, num = q[0], int(q[1])
        if cmd == 'add':
            phonebook.add(num, q[2])
        elif cmd == 'del':
            phonebook.delete(num)
        elif cmd == 'find':
            print(phonebook.find(num))


if __name__ == "__main__":
    phonebook = PhoneBook()
    n = int(input())
    queries = [input() for _ in range(n)]
    process_queries(queries)
