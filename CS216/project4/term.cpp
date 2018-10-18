#include <iostream>
#include <string>
#include "term.h"
#include "autocomplete.h"

using namespace std;

//Pre: n/a
//Post: a default term, for inialization
term::term()
{
	query = "";
	weight = 0;
}

//Pre: string for query and long for weight
//Post: obj containing both
term::term(string q, long w)
{
	query = q;
	weight = w;
}

//comparison types
int term::byReverseWeightOrder(term that, term other)
{
	if (that.weight < other.weight)
	{
		return 1;
	}
	else if (that.weight > other.weight)
	{
		return -1;
	}	
	else
	{
		return 0;
	}
}

int term::compareTo(term that, term other)
{
	if (that.query > other.query)
        {
                return 1;
        }
        else if (that.query < other.query)
        {
                return -1;
        }
        else
        {
                return 0;
        }

}

///////unnecessary - never called
//int term::byPrefixOrder(term that, int r)
//{
//	string left_r = query.substr(0, r);
//	string right_r = that.query.substr(0, r);
//
//	if (left_r > right_r)
//        {
//                return 1;
//        }
//        else if (left_r < right_r)
//        {
//                return -1;
//        }
//        else
//        {
//                return 0;
//        }
//}

//allows printing of contents
void term::print()
{
	cout << weight << "\t" << query << endl;
}

//standard access functions
long term::getWeight()
{
	return weight;
}

string term::getWord()
{
	return query;
}
