#!/usr/bin/env python3
"""Module document"""
import csv
import math
from os import access
from re import Match
from typing import List, Dict


def index_range(page: int, page_size: int) -> tuple:
    """calculate index range"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # number = list(range(0,101))

            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get page from set"""
        try:
            assert isinstance(page, int) and isinstance(page_size, int)
            assert page > 0
            start_index, end_index = index_range(page, page_size)
            return self.dataset()[start_index:end_index]
        except TypeError:
            print('type error')

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Get hyper from set"""
        try:
            assert isinstance(page, int) and isinstance(page_size, int)
            assert page > 0
            start_index, end_index = index_range(page, page_size)
            data = self.dataset()[start_index:end_index]
            total_items = len(self.dataset())
            total_pages = 0 if total_items == 0 else (
                total_items - 1) // page_size + 1
            next_page = page + 1 if page < total_pages else None
            prev_page = page - 1 if page > 1 else None
            return {
                'page_size': len(data),
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
            }
        except TypeError:
            print('type error')
