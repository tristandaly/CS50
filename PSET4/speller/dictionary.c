// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents number of buckets in a hash table
#define N 26
// Variables for future loops declared
int g = 0;
int i = 0;
int x = 0;
int j = 0;
int y = 0;
int wordCount = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Represents a hash table
node *hashtable[N];

// Hashes the word (hash function posted on reddit by THEISBORG)
// The word you want to hash is contained within new node, arrow, word.
// Hashing that will give you the index. Then you insert word into linked list.
int hashIndex(char *hashThis)
{
    unsigned int hash = 0;
    for (i = 0, g = strlen(hashThis); i < g; i++)
    {
        hash = (hash << 2) ^ hashThis[i];
    }
    return hash % N;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize hash table
    for (i = 0; i < N; i++)
    {
        hashtable[i] = NULL;
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    // Insert words into hash table
    while (fscanf(file, "%s", word) != EOF)
    {
        // Create a newNode
        node *newNode = malloc(sizeof(node));
        if (newNode == NULL)
        {
            unload();
            free(newNode);
            free(hashtable);
            return false;
        }
        // Copy the word into newNode
        strcpy(newNode->word, word);
        // Use the hash function to check correct postion in hastable
        x = hashIndex(newNode->word);
        // Add newNode to the hastable
        if (hashtable[x] == NULL)
        {
            newNode->next = NULL;
            hashtable[x] = newNode;
            wordCount++;
        }

        else
        {
            newNode->next = hashtable[x];
            hashtable[x] = newNode;
            wordCount++;
        }
    }

    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    if (wordCount > 0)
    {
        return wordCount;
    }
    else
    {
        return 0;
    }
    return 0;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // Creates a copy of the input word and converts it all to lowercase
    g = strlen(word);
    char copy[g + 1];

    for (j = 0; j < g; j++)
    {
        copy[j] = tolower(word[j]);
    }
    // Adds NULL Terminator after word length is determined
    copy[g] = '\0';

    // Gives you the hashvalue of the word to compare
    x = hashIndex(copy);

    // Creates node for individual hashtable position
    node *position = hashtable[x];
    // Compare words (case-INsensitive)
    while (position != NULL)
    {
        if (strcasecmp(position->word, copy) == 0) // Result of 0 means they are the same
        {
            return true;
        }
        else
        {
            position = position->next; // Moves along to next in the linked list
        }

    }
    return false;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (y = 0; y < N; y++)
    {
        node *position = hashtable[y];
        while (position != NULL)
        {
            node *temp = position; // Declare temporary node for current position in hashtable
            position = position->next; // Move to next position
            free(temp); // Remove from current position; repeat until == NULL
        }

        if (position == NULL)
        {
            free(position); // Free place in memory
        }
    }
    return true;
}

