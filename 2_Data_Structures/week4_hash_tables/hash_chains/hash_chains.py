# python3

class HashTable:
    """Implementation of a hash table using the chaining scheme.

    Example:
    >>> 5
    ... 12
    ... add world
    ... add HellO
    ... check 4
    ... find World
    ... find world
    ... del world
    ... check 4
    ... del HellO
    ... add luck
    ... add GooD
    ... check 2
    ... del good

    >>> HellO world
    ... no
    ... yes
    ... Hell0
    ... GooD luck

    Explanation: The ASCII code of 'w' is 119, for 'o' it is 111, for
    'r' it is 114, for 'l' it is 108, and for 'd' it is 100. Thus,
    h('world') = 4. It turns out that the hash value of HellO is also 4.
    Recall that we always insert in the beginning of the chain, so after
    adding "world" and then "HellO" in the same chain index 4, first goes
    "HellO" and then goes "world". Of course, "World" is not found, and
    "world" is found, because the strings are case-sensitive, and the
    codes of 'W' and 'w' are different. After deleting "world", only
    "HellO" is found in chain 4. Similarly to "world" and "HellO", after
    adding "luck" and "GooD" to the same chain 2, first goes "GooD" and
    then "luck".

    """

    _multiplier = 263
    _prime = 1000000007

    def __init__(self, num_buckets):
        self.num_buckets = num_buckets
        self.buckets = [[] for i in range(num_buckets)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.num_buckets

    def add(self, string):
        """Inserts string into table.

        If there is already a string in the hash table, ignore query.
        """
        key = self._hash_func(string)
        bucket = self.buckets[key]

        if string not in bucket:
            self.buckets[key] = [string] + bucket

    def delete(self, string):
        """Removes string from table.

        If there is no such string in the hash table, ignore query.
        """
        key = self._hash_func(string)
        bucket = self.buckets[key]
        for i in range(len(bucket)):
            if bucket[i] == string:
                bucket.pop(i)
                break

    def find(self, string):
        """Outputs 'yes' or 'no' (without quotes) depending on whether
        table contains string or not.
        """
        key = self._hash_func(string)
        bucket = self.buckets[key]
        if string in bucket:
            return 'yes'
        return 'no'

    def check(self, i):
        """Outputs the i-th list in the table.

        Elements separated by spaces. If i-th list is empty, outputs
        a blank line.
        """
        return self.buckets[int(i)]


def process_queries(queries):
    for query in queries:
        cmd, arg = query.split()
        if cmd == 'add':
            hashtable.add(arg)
        elif cmd == 'del':
            hashtable.delete(arg)
        elif cmd == 'find':
            print(hashtable.find(arg))
        elif cmd == 'check':
            print(' '.join(hashtable.check(arg)))


if __name__ == "__main__":
    num_buckets = int(input())
    n = int(input())
    hashtable = HashTable(num_buckets)

    queries = [input() for _ in range(n)]
    process_queries(queries)

