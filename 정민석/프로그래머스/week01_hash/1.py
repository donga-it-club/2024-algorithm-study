class SimpleHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def simple_hash(self, key):
        # 문자열의 아스키 코드 합을 테이블 크기로 나눈 나머지
        return sum(ord(char) for char in key) % self.size

    def add(self, key):
        index = self.simple_hash(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append(key)

    def remove(self, key):
        index = self.simple_hash(key)
        if self.table[index] is not None:
            try:
                self.table[index].remove(key)
                if not self.table[index]:
                    self.table[index] = None
            except ValueError:
                pass

    def find_non_completer(self):
        for entry in self.table:
            if entry is not None:
                return entry[0]  


def solution(participant, completion):
    hash_table = SimpleHashTable(100) 
    
    for p in participant:
        hash_table.add(p)
    for c in completion:
        hash_table.remove(c)

    return hash_table.find_non_completer()