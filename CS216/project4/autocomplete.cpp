#include <iostream>
#include <vector>
#include <cassert>
#include "autocomplete.h"
#include "term.h"

using namespace std;

//Pre: n/a
//Post: object with empty term vector
autocomplete::autocomplete()
{

}

//Pre: a vector of terms
//Post: obj containing said vector of terms
autocomplete::autocomplete(vector<term> input_vector)
{
	terms = input_vector;
}

//Pre: term to be inserted
//Post: n/a
void autocomplete::insert(term newterm)
{
	terms.push_back(newterm);
}

//Pre: a prefix to be searched for
//Post: vector containing all matches to prefix
vector<term> autocomplete::allMatches(string prefix)
{
	autocomplete matches;
	
	int firstindex = 0;
	int lastindex = terms.size()-1;
	
	Search(prefix, firstindex, lastindex);

	int pos = terms.size()-1;
	int prefix_leng = prefix.length();

	while (terms[pos].query.substr(0, prefix_leng) > prefix) //find last index based off of first index
	{
		lastindex = pos;
		pos--;
	}

	for (int i = firstindex; i < lastindex; i++)
	{
		matches.insert(terms[i]); //push everything between first-last
	}
	
	return matches.terms;
}

//Pre: the prefix, beginning of vector and end
//Post: the actual first/last
void autocomplete::Search(string key, int& first, int& last)
{	
	first = BS_helper(key, first, last); //find first
	
	last = BS_helper(key, first, last); //find last
}

//Pre: incoming prefix/indexes
//Post: found indexes
int autocomplete::BS_helper(string key, int left, int right)
{

        int middle;

        while(left <= right)
        {
                //find middle
		
                middle =(left + right)/2;
                //if greater than the middle, search above
                if (key > terms[middle].query)
                {
                        left = middle+1;
                }
                //if less than the middle, search below
                else if (key < terms[middle].query)
                {
                        right = middle-1;
                }
                else
                {
                        return middle;
                }
        }
	
}

//Pre: number of times to print
//Post: cout stuff
void autocomplete::print(int times)
{
	int counter = 0;
	for (int i = 0; i < times; i++)
	{
		counter++;
		if (counter > terms.size()) //to prevent out of bounds reference
		{
			return;
		}
		terms[i].print();
	}
}

////////unnnessesary operator overload
//autocomplete &autocomplete::operator=(autocomplete &other)
//{
//	cout<<"this.size() = "<<this->getContents().size()<<endl;
//	cout<<"other.size() = "<<other.getContents().size()<<endl;
//        if (this != &other)
//        {
//	       cout<<"checktest1\n";
//	       if(this->getContents().size() < other.getContents().size())
//	       {
//			cout<<"c++\n";	
//               }
//	       else if(this->getContents().size() > other.getContents().size())
//	       {
//			cout<<"c--\n";
//	       }

               // assert(terms.size() == &other.getContents().size());
               // for (int i = 0; i < terms.size(); i++)
               //     terms[i] = other.terms[i];
//        }
//        return *this;
//}

//Pre: function for different comparisons
//Post: sorted vector
//void autocomplete::bubble_sort(int (*compare)(term t1, term t2))
//{
//    term temp;   // for swapping
//    for (int i = 0 ; i < terms.size() -1 ; i++)
//    {
//	cout << "swapping" << endl;
//        for (int j = 0 ; j < terms.size() -1 ; j++)
//        {
//            if ( (*compare)(terms[j], terms[j + 1]) >0 )
//            {
//	        temp = terms[j];
//                terms[j] = terms[j+1];
//                terms[j+1] = temp;
//            }
//        }
//    }
//}

//Pre: compare function and first index and last index
//Post: a new pivot index for more partitioning
int autocomplete::partition (int (*compare)(term t1, term t2), int left, int right)
{
	term temp;
	int pivot = right;    //pivot
	int i = (left - 1);  //index of smaller element
 
	for (int j = left; j <= right - 1; j++)
	{
        	if ((*compare)(terms[pivot], terms[j]) >= 0)//(arr[j] <= pivot)
        	{
                	i++;    // increment index of smaller element
            
	    		temp = terms[i]; //swap
            		terms[i] = terms[j];
            		terms[j] = temp;
		}
    	}
    	temp = terms[i+1];  //swap
    	terms[i+1] = terms[right];
    	terms[right] = temp;

    	return (i + 1);
}

//Pre: compare function and first index and last index
//Post: recursion aside, a sorted function
void autocomplete::quickSort(int (*compare)(term t1, term t2), int left, int right)
{
    if (left < right)
    {
        //partition the data
        int pi = partition((*compare), left, right);
 
        //sort elements before partition
        quickSort((*compare), left, pi - 1);
	//sort elements after partition
        quickSort((*compare), pi + 1, right);
    }
}

//Pre: a given obj containing a vector
//Post: access to said vector - in case access is needed
vector<term> autocomplete::getContents()
{
	return terms;
}
