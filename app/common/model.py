# -*- coding: utf-8 -*-
"""
Module containing DB models.
"""

import datetime as dt

from enum import Enum


class TransactionType(Enum):
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"


class Transaction(object):
    """ Model example """

    def __init__(self, description, amount, type):
        self.description = description
        self.amount = amount
        self.created_at = dt.datetime.now()
        self.type = type

    def __repr__(self):
        return '<Transaction(name={self.description!r})>'.format(self=self)


class TransactionSchema():
    pass


class Income(Transaction):
    def __init__(self, description, amount):
        super(Income, self).__init__(
            description, amount, TransactionType.INCOME)

    def __repr__(self):
        return '<Income(name={self.description!r})>'.format(self=self)


class IncomeSchema(TransactionSchema):
    def make_income(self, data):
        return Income(**data)
