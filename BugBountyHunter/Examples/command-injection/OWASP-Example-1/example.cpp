#include <stdio.h>
#include <unistd.h>
#include<stdlib.h>
#include<string.h>


int main(int argc, char **argv) {
	
	char cat[] = "cat ";
	char *command;
	size_t commandLength;
	int arglen = strlen(argv[1]) + 1;
	commandLength = strlen(cat) + arglen; 
	command = (char *) malloc(commandLength);
	strncpy(command, cat, commandLength);
	puts(command);
	strncat(command, argv[1], arglen );
	system(command);
	return (0);

}

