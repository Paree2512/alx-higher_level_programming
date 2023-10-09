#include <Python.h>

/**
 * print_python_list_info - function prints information about a Python list
 * @p: pointer to a PyObject representing a Python list
 *
 * Function prints information about a Python list, including its
 * number of elements and allocated memory size. It also iterates
 * through the list elements and prints the type of each element
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc;
	int i;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid Python list\n");
		return;
	}

	size = PyList_Size(p);

	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		PyObject *element = PyList_GetItem(p, i);

		if (element != NULL)
		{
			printf("Element %d: %s\n", i, Py_TYPE(element)->tp_name);
		}
		else
		{
			fprintf(stderr, "Failed to retrieve element %d\n", i);
		}
	}
}
