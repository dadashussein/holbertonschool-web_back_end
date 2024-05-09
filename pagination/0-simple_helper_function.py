#!/usr/bin/env python3
"""Module document"""


def index_range(page: int, page_size: int) -> tuple:
    """calculate index range"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
