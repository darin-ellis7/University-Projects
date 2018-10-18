#include <ctime>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include "term.h"
#include "autocomplete.h"

using namespace std;

void trim(string& s);

int main(int argc, char** argv) 
{
    int k; //amount of matches to be displayed
    ifstream in_file;

    //file handling

    if (argc != 3)
    {
        cout << "It needs two command line arguments!" << endl;
        return 1;
    }

    in_file.open(argv[1]);

    k = *argv[2] - '0'; //calculate actual k value (complicated bc char to int)
    if (!in_file.is_open())
    {
       cout << "Failure in opening file: " << argv[1] << endl;
       return 2;
    }

    autocomplete query_list; //autocomplete obj to hold parsed file info

    while (in_file.good())
    {
	string word;
        long number;

        in_file >> number;
	getline(in_file, word);
	trim(word);

        if (word != "")
        {
            term in_term(word, number);
            query_list.insert(in_term); //push values in
        }
    }

	int begin, end;
	begin = clock();
	///////
	int (*compare)(term t1, term t2); //initialize function pointer
	compare = &term::compareTo;
	query_list.quickSort((*compare), 0, query_list.getContents().size()-1); //sort by lexigraphical order
	///////
	end = clock();
	double elaspsed_secs = double(end-begin) / CLOCKS_PER_SEC;
	cout << "Time spent sorting in lexigraphical order: " <<  elaspsed_secs << endl;

	cout << "Please input the search query (type 'exit' to quit): ";
	string search_word; 
	cin >> search_word; //prefix to search for

	while (search_word != "exit")
	{
		int begin, end;
                begin = clock();
		///////////
		vector<term> temp;
		temp = query_list.allMatches(search_word);

		if (temp.size() > 0) //if no matches, don't try to sort empty
		{
			autocomplete matches_list(temp); //create obj with new vector of matches

			compare = &term::byReverseWeightOrder; 

			matches_list.quickSort((*compare), 0, matches_list.getContents().size()-1); //sort by weight
		
			matches_list.print(k); //display
			//////////////
			end = clock();
			double elaspsed_secs = double(end-begin) / CLOCKS_PER_SEC;
			cout << "Time spent searching: " <<  elaspsed_secs << endl;

		}
		
		cout << "Please input the search query (type 'exit' to quit): ";
        	cin >> search_word;
	}
}

void trim(string& s)
{
   size_t p = s.find_first_not_of(" \t");
   s.erase(0, p);

   p = s.find_last_not_of(" \t");
   if (string::npos != p)
      s.erase(p+1);
}
