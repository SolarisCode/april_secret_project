#include <stdio.h>
#include <ctype.h>

int	main(int argc, char **argv)
{
	int	count;
	int	sum;

	if (argc == 1)
		return (1);
	count = 0;
	sum = 0;
	while (argv[1][count])
	{
		if (isdigit(argv[1][count]))
			sum += (argv[1][count] - '0');
		else if (argv[1][count] != 'A')
			sum += 10;
		else if(argv[1][count] == 'A' && sum + 11 <= 21)
			sum += 11;
		else
			sum += 1;
		count ++;
	}
	sum == 21 ? printf("Blackjack!\n") : printf("%d\n", sum);
	return (0);
}
