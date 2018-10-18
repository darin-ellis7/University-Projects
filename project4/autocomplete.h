

#ifndef AUTOCOMPLETE_H
#define AUTOCOMPLETE_H

#include "term.h"
#include <vector>
#include <iostream>

class autocomplete
{
 	public:
		//default constructor
		autocomplete(); 		
		//constructor so object con be constructed with input vector
		autocomplete(vector<term> in_vector);
		// inserts the newterm to the sequence
 		void insert(term newterm);

 		// returns all terms that start with the given prefix,
 		// in descending order of weight
 		vector<term> allMatches(string prefix);
 		// first: the index of the first query that equals
 		// the search key, or -1 if no such key
 		// last: the index of the last query that equals
 		// the search key, or -1 if no such key
 		void Search(string key, int& first, int& last);

 		// return the index number of the search key using binary search algorithm
 		int BS_helper(string key, int left, int right);
 		// display all the terms
 		void print(int times);
 		// other member functions you need…
		void selection_sort(int (*compare)(term t1, term t2));
		void quickSort(int (*compare)(term t1, term t2), int low, int high);
		int partition (int (*compare)(term t1, term t2), int low, int high);
	 	vector<term> getContents();
		
		autocomplete &operator=(autocomplete &other);

 	private:
 		// choose your own data structure to represent the sequence of Term objects
		vector<term> terms;
};

#endif
