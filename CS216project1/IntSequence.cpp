//Author: Darin Ellis
//Class: CS 216
//Section: 002
//Date: 2/14/2016
//Purpose: class definition, for IntSequence, to define the various functions
//	   to create/manipulate the arrays.

using namespace std;
#include <iostream>
#include <cstdlib>
#include <ctime>
#include "IntSequence.h"

//default constructor
IntSequence::IntSequence()
{
	capacity = INITIAL_CAPACITY;
	count = 0;
	seq = new int [capacity];
}
//constructor
IntSequence::IntSequence(int in_capacity)
{
	capacity = in_capacity;
	count = 0;
	seq = new int [capacity];
}
//fill the array based on user input, expand array if capacity is exceeded
void IntSequence::insert(int item)
{
        count++;
        while (count > capacity)
        {
                capacity *= 2;
                int *copy_seq = new int [capacity];
                for (int i = 0; i < count-1; i++)
                {
                        copy_seq[i] = seq[i];
                }
        	delete [] seq;
        	seq = copy_seq;
        }
        seq[count-1] = item;
}
//print the contents of the array
void IntSequence::print()
{
	cout << "Sequence:      ";
	for (int i = 0; i <= count-1; i++)
        {
                cout << seq[i] << " ";
        }
	cout << endl;
	cout << "======================================================" << endl;
}
//selection sort
void IntSequence::selection_sort()
{
	//check for empty array
	if (count == 0)
	{
		cout << "Array is empty!" << endl;
		return;
	}	

	cout << "===Selection Sort========================================" << endl;
	for (int i = 0; i < count-1; i++)
	{
		int min_index = i;
		for (int j = i+1; j < count; j++)
		{
			if (seq[j] < seq[min_index])
			{
				min_index = j;
			}
		}
		if (min_index != i)
		{
			//swap
			int temp = seq[i];
			seq[i] = seq[min_index];
                        seq[min_index] = temp;
			cout << "Min " << seq[i] << " Swap with " << seq[min_index] << ":     ";
			//print sequence
                	for (int k = 0; k <= count-1; k++)
                	{
                        	cout << seq[k] << " ";
                	}
			cout << endl;
		}
	}
	//print final sorted
	print();
}

void IntSequence::insertion_sort()
{
	//check for empty
	if (count == 0)
        {
                cout << "Array is empty!" << endl;
                return;
        }	

	cout << "===Insertion Sort========================================" << endl;
	for (int i = 1; i <= count-1; i++)
        {
                int key = seq[i];
                int position = i;
                while (position > 0 && seq[position-1] > key)
                {
			//insert and move
                        seq[position] = seq[position-1];
                        position--;
                }
                seq[position] = key;
		cout << "Insert " << key << ":    ";
                for (int k = 0; k <= count-1; k++)
                {
                        cout << seq[k] << " ";
                }
		cout << endl;
        }
	print();
	cout << "======================================================" << endl;
}

void IntSequence::bubble_sort()
{
	//check for empty
	if (count == 0)
        {
                cout << "Array is empty!" << endl;
                return;
        }

	cout << "===Bubble Sort========================================" << endl;
	//iterate through
	for (int i = 1; i <= count-1; i++)
        {
                for (int j = 0; j <= count-2; j++)
                {
			//compare
                        if (seq[j] > seq[j+1])
                        {
				//swap
                                int temp = seq[j];
                                seq[j] = seq[j+1];
                                seq[j+1] = temp;
                        }
                }
		cout << "Iteration " << i << ":    ";
		for (int k = 0; k <= count-1; k++)
        	{	
                	cout << seq[k] << " ";
        	}
		cout << endl;
	}
	print();
        cout << "======================================================" << endl;
}

void IntSequence::shuffle()
{	
	//set random
	srand(time(0));

	for (int i = count-1; i >= 1; i--)
	{
		//randomly select and swap
		int j = rand() % (i);
		int temp = seq[j];
                seq[j] = seq[i];
                seq[i] = temp;
	}
}

int IntSequence::sequential_search(int key)
{
	//print array being searched
	print();
	
	int comparisons = 0;
	
	//iterate through
	for (int i = 0; i < count; i++)
	{
		comparisons++; //increment comparison number
		//if found
		if (seq[i] == key)
		{
			cout << "Search with " << comparisons << " comparison(s)" << endl;
			return i;	
		}
	}
	//if not found
	return -1;
}

int IntSequence::binary_search(int key)
{
	//print unsorted
	cout << "Unsorted ";
	print();
	
	//bubble sort
	for (int i = 1; i <= count-1; i++)
        {
                for (int j = 0; j <= count-2; j++)
                {
                        if (seq[j] > seq[j+1])
                        {
                                int temp = seq[j];
                                seq[j] = seq[j+1];
                                seq[j+1] = temp;
                        }
                }
        }

	//print sorted
	cout << "Sorted ";
	print();
	
	int middle;
	int left = 0; 
	int right = count-1;
	int index = 0;
	int comparisons = 0;	

	while(left <= right)
	{
		comparisons++; //increment comparison number
		//find middle
		middle =(left + right)/2;
		//if greater than the middle, search above
		if (key > seq[middle])
		{
			index += middle +1; //calculate index
			left = middle+1;
		}
		//if less than the middle, search below
		else if (key < seq[middle])
		{
			index++; //calculate index
			right = middle-1;
		}
		else
		{
			cout << "Search with " << comparisons  << " comparison(s)" << endl;
			return middle;
		}
	}
	return -1;
}

IntSequence::~IntSequence()
{

}







