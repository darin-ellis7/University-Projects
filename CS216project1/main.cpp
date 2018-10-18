//Author: Darin Ellis
//Class: CS 216
//Section: 002
//Date: 2/14
//Purpose: main function, displays menu and allows user to input and manipulate
//	   an array many times.

using namespace std;

#include <iostream>
#include "IntSequence.h"

void pause_215(bool have_newline);

int main()
{	
	bool quit_flag = false;	//to check for option 6
	IntSequence input_sequence = IntSequence(); // the array	

	while (quit_flag == false)
	{
		//menu input and validation
		int option;	

		cout << "1. Read" << endl;
		cout << "2. Print" << endl;
		cout << "3. Sort" << endl;
		cout << "4. Shuffle" << endl;
		cout << "5. Search" << endl;
		cout << "6. Quit" << endl;
		cout << "Option: ";
		cin >> option;

		while (option > 6 || option < 1 || cin.fail())
		{
			cin.clear();
			cin.ignore(256, '\n');
			cout << "Invalid option!" << endl;

			cout << "1. Read" << endl;
			cout << "2. Print" << endl;
			cout << "3. Sort" << endl;
			cout << "4. Shuffle" << endl;
			cout << "5. Search" << endl;
			cout << "6. Quit" << endl;
			cout << "Option: ";
			cin >> option;

		}
		
		//read
		if (option == 1)
		{
			string q_check;
			bool q_flag = false;			

			int new_element;
			cout << "Enter the next element (Enter 'q' to stop): ";
			cin >> new_element;
			while (cin.fail())
                        {
                        	cin.clear();
                                cin >> q_check;
                                if (q_check == "q")
                                {
                                	q_flag = true;
                                }
                                else
                                {
                                	cin.ignore(256, '\n');
                                        cout << "Invalid input!" << endl;
                                        cout << "Enter the next element (Enter 'q' to stop): ";
                                        cin >> new_element;
                                 }
                        }
			
			while (q_flag != true)
			{
				input_sequence.insert(new_element);
				cout << "Enter the next element (Enter 'q' to stop): ";
                                cin >> new_element;
				
				while (cin.fail())
				{
					cin.clear();
					cin >> q_check;
					if (q_check == "q")
					{
						q_flag = true;
					}
					else
					{
						cin.ignore(256, '\n');
						cout << "Invalid input!" << endl;
						cout << "Enter the next element (Enter 'q' to stop): ";
                        			cin >> new_element;
					}
				}
			}	
		}
		
		//print
		if (option == 2)
		{
			input_sequence.print();
		}
		
		//all of the sorts
		if (option == 3)
		{
			int sort_option;
			cout << "1. Insertion sort" << endl;
			cout << "2. Selection sort" << endl;
			cout << "3. Bubble sort" << endl;
			cout << "4. Quit" << endl;
			cout << "Option: ";
			cin >> sort_option;
			
			while (sort_option > 4 || sort_option < 1 || cin.fail())
			{
				cin.clear();
				cin.ignore(256, '\n');
				cout << "1. Insertion sort" << endl;
                        	cout << "2. Selection sort" << endl;
                        	cout << "3. Bubble sort" << endl;
                        	cout << "4. Quit" << endl;
				cout << "Option: ";
                        	cin >> sort_option;
			}
			
			//insertion sort
			if (sort_option == 1)
			{
				input_sequence.insertion_sort();
			}
			//selection sort
			if (sort_option == 2)
			{
				input_sequence.selection_sort();
			}
			//bubble sort
			if (sort_option == 3)
			{
				input_sequence.bubble_sort();
			}
		}
		//shuffle
		if (option == 4)
		{	
			input_sequence.shuffle();
		}
		
		//search
		if (option == 5)
		{
			int search_key;
			int search_option;
			int index;
                        cout << "1. Sequential search" << endl;
                        cout << "2. Binary search" << endl;
                        cout << "3. Quit" << endl;
			cout << "Option: ";
                        cin >> search_option;

                        while (search_option > 3 || search_option < 1 || cin.fail())
                        {
                                cin.clear();
                                cin.ignore(256, '\n');
                                cout << "1. Sequential search" << endl;
                                cout << "2. Binary search" << endl;
                                cout << "3. Quit" << endl;
				cout << "Option: ";
                                cin >> search_option;
                        }
			
			//sequential
                        if (search_option == 1)
                        {
				cout << "Enter the key to find: ";
				cin >> search_key;
				while (cin.fail())
				{
					cout << "Invalid key!" << endl;
					cout << "Enter the key to find: ";
                                	cin >> search_key;
				}
                                index = input_sequence.sequential_search(search_key);
				if (index == -1)
				{
					cout << "Key not found." << endl;
				}
				else
				{
					cout << "Key found at index " << index << endl;
				}
                        }
			//binary
                        if (search_option == 2)
                 	{
				cout << "Enter the key to find: ";
                                cin >> search_key;
                                while (cin.fail())
                                {
                                        cout << "Invalid key!" << endl;
                                        cout << "Enter the key to find: ";
                                        cin >> search_key;
                                }
                                index = input_sequence.binary_search(search_key);
				if (index == -1)
                                {
                                        cout << "Key not found." << endl;
                                }
                                else
                                {
                                        cout << "Key found at index " << index << endl;
                                }
                        }
		}
		//set flag to end menu loop
		if (option == 6)
		{
			quit_flag = true;
		}
	}
	cout << "Thank you for using the program." << endl;
	cout << "==============================================================";
	pause_215(true);
	return 0;
}

//function for pause at end
void pause_215(bool have_newline)
{
	if (have_newline)
	{
		cin.ignore(256, '\n');
	}
	cout << endl << "Press ENTER to continue." << endl;
	cin.ignore(256, '\n');
}

