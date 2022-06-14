import torch
from sentence_transformers.util import pytorch_cos_sim


class EmptyVectorStoreException(Exception):
    pass


class VectorStore:
    """
    Stores vectors associated with IDs.
    """

    def neighbors(self, query_vectors):
        raise NotImplementedError

    def add(self, items):
        raise NotImplementedError

    def remove(self, items):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError


class NaiveVectorStore(VectorStore):
    """
    Toy index, storing vectors as 2-d torch.Tensor.
    """

    def __init__(self):
        self.matrix = None
        self.ids = None
        self.id_to_idx = {}

    def neighbors(self, query_vectors, k=None, thresh=None):
        """
        Get k nearest neighbors and their similarities.
        k=-1 returns all items & similarities.
        """
        if self.matrix is None:
            raise EmptyVectorStoreException(
                "Vector store is empty, needs to be populated before querying."
            )

        S = pytorch_cos_sim(query_vectors, self.matrix)
        outputs = []
        for i in range(len(query_vectors)):
            scores = S[i].tolist()
            scored = sorted(
                zip(self.ids, scores), key=lambda x: x[1], reverse=True
            )
            if thresh is not None:
                scored = [(id, x) for id, x in scored if x >= thresh]
            if k is not None:
                scored = scored[:k]
            outputs.append(scored)
        return outputs

    def add(self, ids, vectors):
        """
        Add new vectors to store.
        """
        assert [id not in self.id_to_idx for id in ids]
        if self.matrix is None:
            idx = 0
            self.matrix = vectors
            self.ids = ids
        else:
            idx = len(self.matrix)
            self.matrix = torch.cat([self.matrix, vectors], dim=0)
            self.ids += ids
        for id in ids:
            self.id_to_idx[id] = idx
            idx += 1

    def remove(self, ids):
        """
        Remove vectors from store corresponding to given ids.
        """
        idx_to_id = dict((idx, id) for id, idx in self.id_to_idx.items())
        deleted_indices = set([self.id_to_idx[id] for id in ids])
        new_matrix = [
            self.matrix[i] for i in range(len(self.matrix))
            if i not in deleted_indices
        ]
        new_matrix = torch.stack(new_matrix, dim=0)
        new_ids = [
            idx_to_id[i] for i in range(len(self.matrix))
            if i not in deleted_indices
        ]
        self.ids = new_ids
        self.id_to_idx = dict((id, i) for i, id in enumerate(new_ids))
        self.matrix = new_matrix

    def reset(self):
        self.matrix = None
        self.ids = None
        self.id_to_idx = {}
