#include "Python.h"
#include <stdio.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t i;
    PyObject *obj;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    for (i = 0; i < PyList_Size(p); i++)
    {
        obj = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t i;
    char *str;

    printf("[.] bytes object info\n");
    if (PyBytes_Check(p))
    {
        printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
        str = ((PyBytesObject *)p)->ob_sval;
        printf("  trying string: %s\n", str);
        if (((PyVarObject *)p)->ob_size > 10)
            printf("  first 10 bytes:");
        else
            printf("  first %ld bytes:", ((PyVarObject *)p)->ob_size + 1);
        for (i = 0; i < ((PyVarObject *)p)->ob_size && i < 10; i++)
            printf(" %02x", str[i] & 0xff);
        printf("\n");
    }
    else
        printf("  [ERROR] Invalid Bytes Object\n");
}
