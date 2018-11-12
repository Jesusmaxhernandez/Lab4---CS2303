#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 14:48:33 2018

@author: JesusMHernandez
"""
from HashTableN import HashTableNode

file_name = "textW.txt"

def insert(table, value):
    '''
    inserts value into table
    '''
    #table[hash_function(value)] = value
    
    table[hash_function(value)].append((input,value))
    
def string_to_base26(word):
    ''' 
    Converts a string from Base26(letters only) with no 0th case to a positive
    integer. 
    '''
    word = word.lower()
    if word == " " or len(word) == 0:
        return 0
    if len(word) == 1:
        return ord(word)-96
    else:
        return string_to_base26(word[1:])+(26**(len(word)-1))*(ord(word[0])-96)
    
def count_lines(file_name):
    '''
    counts how many words in file
    '''
    count = 0
    with open("testW.txt") as f: #change file to testFile when you want to test
        for line in f:
            count += 1
    return count
    
def hash_function(word):
    '''
    method to determine hash function by getting the base26 value of a word
    then using the modulo
    '''
    value = string_to_base26(word)
    size = count_lines(file_name)
    return value % size

def hash_function(word):
    '''
    method to determine hash function
    '''
    value = string_to_base26(word)
    size = count_lines(file_name)
    return value % size
    
def create_hash(file_name):
    '''
    creates the hash table
    '''
    lines = count_lines(file_name)
    #print(lines)
    size = int(round(lines * 1.25))
    #print(size)
    table = [None] * size
#    table = [[] for x in range(size)]

    with open(file_name) as f: #change file to testFile when you want to test
        for line in f:
             if "\n" in line:
                 line = line.replace("\n", "")
             word = (line.lower()) #this line makes every word a lower case
             table[hash_function(word)] = HashTableNode(line, table[hash_function(word)])
             #insert(table, word)        
            
    return table
             
def main():
    user_answer = 0
    create_hash("testW.txt")
    valid = True

    while(valid == True):
        print("HashFunction? Yes:(A)")
        answer = input("Enter 'A' for modulo or 'B' for : ")
        answer = answer.lower()
        if(answer == 'a'):
            create_hash(file_name)
            valid == False  
        
main()