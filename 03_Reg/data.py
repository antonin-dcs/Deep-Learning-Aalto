import os
import numpy as np
import pandas as pd

import torch
from torch.utils.data import TensorDataset


class RatingsData(TensorDataset):    
    def __init__(self, root, train=True):
        self.root = root
        self._folder = folder = os.path.join(root, 'Ratings')
        self._fetch_data(root)
        
        self.n_users = 943
        self.n_items = 1682

        if train:
            filename = os.path.join(folder, 'train.tsv')
        else:
            filename = os.path.join(folder, 'test.tsv')

        cols = ['user_ids', 'item_ids', 'ratings', 'timestamps']
        df = pd.read_csv(filename, sep='\t', names=cols).astype(int)
        user_ids = torch.LongTensor(df.user_ids.values)
        item_ids = torch.LongTensor(df.item_ids.values)
        ratings = torch.LongTensor(df.ratings.values)

        super(RatingsData, self).__init__(user_ids, item_ids, ratings)
    
    def _check_integrity(self):
        files = ['train.tsv', 'test.tsv']
        for file in files:
            if not os.path.isfile(os.path.join(self._folder, file)):
                return False
        return True

    def _fetch_data(self, data_dir):
        if self._check_integrity():
            return
        print("Move the data files from the 'course_data' path of the repository to '/coursedata'")



    