/****************************************************************************
 * dictionary.h
 *
 * Application Security, Assignment 1
 *
 * Adapted from code written by Ben Halperin
 ***************************************************************************/

#ifndef DICTIONARY_H
#define DICTIONARY_H

#include <stdbool.h>
#include <stdio.h>

// maximum length for a word
// (e.g., pneumonoultramicroscopicsilicovolcanoconiosis)
#define LENGTH 45

#define HASH_SIZE 2000

typedef struct node
{
    char word[LENGTH + 1];
    struct node* next;
}
node;

typedef node* hashmap_t;

/**
 * Returns true if all words are spelled correctly, false otherwise. Array misspelled is populated with words that are misspelled.
 */
int check_words(FILE* fp, hashmap_t hashtable[], char * misspelled[]);

/**
 * Returns true if word is in dictionary else false.
 */
bool check_word(const char* word, hashmap_t hashtable[]);

/**
 * Loads dictionary into memory.  Returns true if successful else false.
 */
bool load_dictionary(const char* dictionary_file, hashmap_t hashtable[]);

/**
 * Maps string to a number corresponding to location in hash table.
 */

#endif // DICTIONARY_H
