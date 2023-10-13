/*I/P: hello , how is your family?!
  O/P: ylima , fru oy siwo halleh*/
/*#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
	char str[100],i;
	for(i=0;str[i]!='\0';i++)
	{
		scanf("%s",str[i]);
	}
	for(i=0;str[i]!='\0';i--)
	{
		printf("%s",str[i]);
	}
	//printf("Reversed string: ");
}*/
#include <stdio.h>
#include <string.h>

int main() {
  // Declare a string variable to store the input string
  char input_string[] = "hello, how is your family?!";

  // Declare a string variable to store the output string
  char output_string[33];

  // Reverse the input string
  int i = 0;
  int j = strlen(input_string) - 1;

  while (i < j) {
    char temp = input_string[i];
    input_string[i] = input_string[j];
    input_string[j] = temp;

    i++;
    j--;
  }

  // Copy the reversed input string to the output string, but with the words in reverse order
  i = 0;
  int k = 0;

  while (input_string[i] != '\0') {
    if (input_string[i] == ' ') {
      output_string[k] = ' ';
      k++;
      i++;
    } else {
      while (input_string[i] != ' ' && input_string[i] != '\0') {
        output_string[k] = input_string[i];
        k++;
        i++;
      }
      output_string[k] = ' ';
      k++;
    }
  }

  // Add a null terminator to the output string
  output_string[k] = '\0';

  // Print the output string
  printf("%s\n", output_string);

  return 0;
}