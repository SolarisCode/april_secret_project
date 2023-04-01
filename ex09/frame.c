#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int	main(int argc, char **argv)
{
	int		count;
	int		len;
	int		word_len;
	char	*input;
	char	*str;

	if (argc == 1)
		return (1);
	count = -1;
	input = calloc(strlen(argv[1]), sizeof(char));
	strcpy(input, argv[1]);
	str = strtok(input, " ");
	len = strlen(str);
	while (str)
	{
		str = strtok(NULL, " ");
		if (str && strlen(str) > len)
			len = strlen(str);
	}
	len += 4;
	while (++count < len)
		printf("*");
	printf("\n");
	str = strtok(argv[1], " ");
	while (str)
	{
		word_len = strlen(str);
		count = -1;
		while (++count <= len)
		{
			if (!count || count == len)
				printf("*");
			else if (count == 2)
				count += printf("%s", str);
			else
				printf(" ");
		}
		printf("\n");
		str = strtok(NULL, " ");
	}
	count = -1;
	while (++count < len)
		printf("*");
	printf("\n");
	free(input);
}
