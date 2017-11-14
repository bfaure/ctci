
#include <iostream>

void print_arr(int *array, int array_length)
{
	for (int i=0; i<array_length; i++)
	{
		std::cout<<array[i]<<" ";
	}
	std::cout<<"\n";
}


int main()
{
	int *a = new int[3];

	for (int i=0; i<3; i++)
	{
		a[i]=i;
	}

	print_arr(a,3);
}