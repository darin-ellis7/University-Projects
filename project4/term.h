#ifndef TERM_H
#define TERM_H

using namespace std;

class term
{
 public:
 	// default constructor
 	term();
 	// initialize with the given query string and weight
 	term(string q, long w);
 	// compares two terms in descending order by weight
 	static int byReverseWeightOrder(term that, term other);
 	// compares two terms in lexicographic order by query
 	static int compareTo(term that, term other);
 	// compares two terms in lexicographic order but using only
 	// the first r characters of each query
 	static int byPrefixOrder(term that, int r);
 	// displays the term in the following format:
 	// the weight, followed by a tab key, followed by the query
 	void print();
 	// other member functions you need…
	// accessor method for weight
	long getWeight();
	// accessor method for word
	string getWord();
 	friend class autocomplete;

 private:
 	string query;
 	long weight;

};

#endif
