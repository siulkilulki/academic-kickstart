#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_array(int *array, int size) {
  printf("[");
  for (int i = 0; i < size; i++) {
    if (i < size - 1) {
      printf("%d, ", array[i]);
    } else {
      printf("%d", array[i]);
    }
  }
  printf("]\n");
}

int main() {
  int *array;
  int n = 5;
  printf("Size of int is %lu.\n\n", sizeof(int));

  // Dynamically allocate memory, values are undefined (e.g. could be random)
  array = malloc(n * sizeof(int));
  if (array == NULL) {
    printf("Memory not allocated");
    exit(0);
  }
  for (int i = 0; i < n; i++) {
    array[i] = 9;
  }
  printf("Array after malloc and initialisation: ");
  print_array(array, n);

  // Dynamically reallocate memory
  printf("Array after realloc and setting last element: ");
  array = realloc(array, (n + 1) * sizeof(int));
  array[0] = 3;
  print_array(array, n + 1);

  // Free dynamically allocated memory
  free(array);

  // Other option
  // Dynamically allocate memory and initalise with zeros
  array = calloc(n, sizeof(int));
  printf("Array after calloc: ");
  print_array(array, n);

  free(array);
  return 0;
}
