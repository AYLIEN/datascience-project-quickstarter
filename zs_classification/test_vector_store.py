import unittest
import torch
from zs_classification.vector_store import NaiveVectorStore


class TestNaiveVectorStore(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vectors = torch.tensor([
            [0.1, 0.1, 0.1, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.1, 0.1, 0.1],
            [0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
        ])
        cls.ids = ["first-half", "last-half", "all"]

    def test_add(self):
        # fill empty store
        v = NaiveVectorStore()
        v.add(self.ids.copy(), torch.clone(self.vectors))
        assert torch.equal(v.matrix, self.vectors)
        assert v.ids == self.ids
        assert v.id_to_idx == dict((id, i) for i, id in enumerate(self.ids))
        # add a new vector & id on top
        new_id = "new"
        new_vec = torch.tensor([0.1, 0.1, 0.1, 0.2, 0.3, 0.4])
        v.add([new_id], new_vec.unsqueeze(0))
        assert v.ids[-1] == "new"
        assert torch.equal(v.matrix[-1], new_vec)
        assert v.matrix.shape == (len(self.ids) + 1, self.vectors.size(1))

    def test_remove(self):
        v = NaiveVectorStore()
        v.add(self.ids.copy(), torch.clone(self.vectors))
        v.remove([self.ids[0]])
        assert self.ids[0] not in v.ids
        assert self.ids[0] not in v.id_to_idx
        assert len(v.matrix) == len(self.vectors) - 1

    def test_neighbors(self):
        v = NaiveVectorStore()
        v.add(self.ids.copy(), torch.clone(self.vectors))
        for i, id in enumerate(self.ids):
            query = self.vectors[i].unsqueeze(0)
            neighbors = v.neighbors(query)[0]
            assert neighbors[0][0] == id

    def test_knn(self):
        v = NaiveVectorStore()
        v.add(self.ids.copy(), torch.clone(self.vectors))
        query = self.vectors[0].unsqueeze(0)
        for k in [1, 2, 3]:
            neighbors = v.neighbors(query, k=k)[0]
            assert len(neighbors) == k


if __name__ == '__main__':
    unittest.main()
