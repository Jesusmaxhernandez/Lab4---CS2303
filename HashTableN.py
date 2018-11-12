#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 22:24:55 2018
Jesus Maximino Hernandez
CS 2302 Data Structures - Diego Aguirre
TA - Manoj Saha
Lab 4 - Option B 
Program that sorts english words into a hash table using different hash functions
and has different functions determine comparisons and load factor 

@author: JesusMHernandez
"""

class HashTableNode:
    def __init__(self, item, next):
        self.item = item
        self.next = next
