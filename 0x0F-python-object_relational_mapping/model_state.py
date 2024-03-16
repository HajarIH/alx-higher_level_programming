#!/usr/bin/python3
"""Methode to define a class State"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mtd = MetaData()
Base = declarative_base(metadata=mtd)


class State(Base):
    """class sState"""
    __tablename__ = "states"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
