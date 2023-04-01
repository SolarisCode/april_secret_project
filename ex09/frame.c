#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void	ft_draw_body(char *input, int size)
{
	int		count;
	char	*str;

	str = strtok(input, " ");
	while (str)
	{
		count = -1;
		while (++count <= size)
		{
			if (!count || count == size)
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
	while (++count < size)
		printf("*");
	printf("\n");
}

int	main(int argc, char **argv)
{
	int		count;
	int		len;
	char	*input;
	char	*str;

	if (argc == 1)
		return (1);
	input = calloc(strlen(argv[1]) + 1, sizeof(char));
	strcpy(input, argv[1]);
	str = strtok(argv[1], " ");
	len = strlen(str);
	while (str)
	{
		str = strtok(NULL, " ");
		if (str && strlen(str) > len)
			len = strlen(str);
	}
	len += 4;
	count = -1;
	while (++count < len)
		printf("*");
	printf("\n");
	ft_draw_body(input, len);
	free(input);
}
