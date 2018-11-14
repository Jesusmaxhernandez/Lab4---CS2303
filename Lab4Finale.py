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
from HashTableN import HashTableNode
import math
import random

gl_file_name = "testW.txt"

def string_to_base26(word):
    ''' 
    Converts a string from Base26 to a positive
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
    with open(gl_file_name) as f: #change file to testFile when you want to test
        for line in f:
            count += 1
    return count
    

def div_hash_function(word):
    '''
    method to determine hash function using divison method
    '''
    value = string_to_base26(word)
    size = count_lines(gl_file_name)
    #print(str(value % size)+"function")
    return value % size

def mad_hash_function(word):
    '''
    method to determine hash function using Multiply-Add-and-Divide method
    [(ai+b) mod p] mod N,
    '''

    prime = 0
    size = count_lines(gl_file_name)
    prime = find_next_prime(size)
    a = random.randint(0, prime-1)
    b = random.randint(0, prime-1)
    
    
    function = ((a+b) % prime) % size
    #print(str(function)+"function")
    return function
def is_prime(a):
    '''
    Function to check if a num is prime 
    '''
    for i in range(2, a):
       if a % i == 0:
          return False
    return True

def find_next_prime(n):
  '''
  Function to find the next prime number
  '''
  num = n + 1
  while True:
     if is_prime(num):
        return num
     else:
        num += 1
        
def num_com(table, word, index):
    '''
    gets num of comparisons when looking for a word 
    '''
    counter = 0
    temp = table[index]

    while temp is not None:
        counter += 1
        temp = temp.next
        
    return counter
def avg_com(table, file_name, method):
    '''
    gets average num of comparisons when looking for words in a file
    '''
    i = 0
    temp = dict()
    with open(file_name) as f: 
            for line in f:
                 if "\n" in line:
                     line = line.replace("\n", "")
                 word = (line.lower()) #this line makes every word a lower case
                 if method == 'a':
                     i = div_hash_function(word)
                 if method == 'b': 
                     i = mad_hash_function(word)
                 temp[word] = num_com(table, word, i)
    total_comp = 0
    counter = 0
    # Counts comparisons 
    for value in temp:
        total_comp += temp[value]
        counter += 1
    return total_comp / counter
    
    
def get_load_factor(table):
        '''
        Gets load factor by counting how many elements in table then dividing
        it by size
            '''
        num_elements = 0
        
        for i in range(len(table)):
            temp = table[i]

            while temp is not None:
                num_elements += 1
                temp = temp.next
        #print(num_elements)
        #print(len(table))
        return num_elements / len(table)
    
def create_hash(file_name, method):
    '''
    creates the hash table
    '''

    lines = count_lines(file_name)
    #print(lines)
    size = int(round(lines * 1.25))
    #print(size)
    table = [None] * size
#    table = [[] for x in range(size)]
    if(method == 'a'):
        print("Creating Hash Table using Divison Method")
        with open(file_name) as f: #change file to testFile when you want to test
            for line in f:
                 if "\n" in line:
                     line = line.replace("\n", "")
                 word = (line.lower()) #this line makes every word a lower case
                 index = div_hash_function(word)
                 table[index] = HashTableNode(line, table[index])
                 #insert(table, word)  
    else:
        print("Creating Hash Table using MAD Method")
        with open(file_name) as f: #change file to testFile when you want to test
            for line in f:
                 if "\n" in line:
                     line = line.replace("\n", "")
                 word = (line.lower()) #this line makes every word a lower case
                 index = mad_hash_function(word)
                 table[index] = HashTableNode(line, table[index])
    return table
             
def main():
    file_name = gl_file_name
    valid = False
    #method= ''

    while(valid == False):
        answer = input("Enter 'A' for Divison Method or 'B' for MAD Method: ")
        answer = answer.lower()
        if(answer == 'a'or answer == 'b'):
            hash_table = create_hash(file_name, answer)
            print("Hash Function Completed")
            print("Load Factor of HashTable is " +  str(get_load_factor(hash_table)))
            print("Average number of comparisons is " +  str(avg_com(hash_table, file_name, answer)))
           # num_com("mom")
            break
        if(answer != 'b' or answer != 'a'):
            print("Invalid Input try again")
            valid = False
    
        
main()
