#include <iostream>

// Provides an integer array object that will resize itself when needed
class dynamic_array
{
private:

	int *data;
	int array_size = 100;
	int num_items = 0;
public:

	// constructor
	dynamic_array()
	{
		std::cout<<"Creating a new dynamic array!\n";
		data = new int[array_size];
	}

	// size function
	int length(){  return num_items;  }

	// bracket operator
	int operator[](int i){  return data[i];  }

	// append function
	void append(int p)
	{
		if (num_items==array_size)
		{
			// need to increase array size
			array_size = array_size*2;
			int *temp = new int[array_size];
			for (int i=0; i<num_items; i++)
			{
				temp[i] = data[i];
			}
			data = temp;
			std::cout<<"Resized array to length "<<array_size<<"\n";
		}
		// simply add in the new data
		data[num_items] = p;
		num_items++;
	}
};


int main(int argc, char ** argv)
{
	dynamic_array test;

	for (int i=0; i<1000; i++)
	{
		test.append(i);
	}
	std::cout<<"Element at end: "<<test[999]<<"\n";

	return 1;
}