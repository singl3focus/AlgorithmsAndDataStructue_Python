from typing import List, Tuple, TypeVar, Generic, Optional

K = TypeVar("K", int, str)  # Вводим тип К, обобщающий int, str
V = TypeVar("V")  # Вводим тип V, обобщающий все типы


class HashedTable(Generic[K, V]):
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.table: List[List[Tuple[K, V]]] = [[] for _ in range(size)]

    def get_size(self) -> int:
        return self.size

    def _hash(self, key: K) -> int:
        h: int = hash(K)
        return h % self.size

    def set(self, key: K, value: V) -> None:
        indx: int = self._hash(key)

        for i, (k, v) in enumerate(self.table[indx]):
            if k == key:
                self.table[indx][i]: Tuple[K, V] = (key, value)
                return

        self.table[indx].append((key, value))

    def get(self, key: K) -> (V, bool):
        indx: int = self._hash(key)

        for k, v in self.table[indx]:
            if k == key:
                return v, True

        return None, False

    def delete(self, key: K) -> bool:
        indx: int = self._hash(key)

        for i, (k, v) in enumerate(self.table[indx]):
            if k == key:
                del self.table[indx][i]
                return True

        return False

    def contains_with_index(self, key: K) -> bool:
        indx: int = self._hash(key)

        for k, _ in self.table[indx]:
            if k == key:
                return True

        return False

    def contains_with_enumeration(self, key: K) -> bool:
        for lst in self.table:
            for k, _ in lst:
                if k == key:
                    return True

        return False
