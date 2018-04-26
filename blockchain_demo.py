import hashlib as hasher
from datetime import datetime


class Blockchain:
    def __init__(self):
        self._blockchain = []

    def add(self, data):
        idx = len(self._blockchain)
        timestamp = datetime.now()
        previous_hash = self.last_hash()
        block = Block(idx, timestamp, data, previous_hash)
        self._blockchain.append(block)

    def last_hash(self):
        if len(self._blockchain) == 0:
            return ""
        return self._blockchain[-1].hash

    def print(self):
        for b in self._blockchain:
            print(b)


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        seq = (str(x) for x in (
            self.index, self.timestamp, self.data, self.previous_hash))
        sha.update(''.join(seq).encode('utf-8'))
        return sha.hexdigest()

    def __str__(self):
        self_str = "prev_hash: {}\nBlock #{}\n{}\n{}"\
            .format(self.previous_hash, self.index, self.timestamp, self.data)
        self_str += "\nthis_hash: {}\n".format(self.hash)
        self_str += "======================================"
        self_str += "====================================="
        return self_str


class BlockchainDemo:
    def run(self):
        blockchain = Blockchain()

        blockchain.add("first block")

        for i in range(1, 6):
            data = 'example data for block {}'.format(i)
            blockchain.add(data)

        blockchain.print()


if __name__ == "__main__":
    BlockchainDemo().run()
