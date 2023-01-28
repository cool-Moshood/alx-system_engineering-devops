#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - creating a infinite loops
 * Return: Zero
 *
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creating a zombie
 * Return: Always return 0
 */

int main()

{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
		{
			exit(0);
			printf("Zombie process created, PID: %d\n", pid)
		}
	}
	infinite_while();
	return 0;
}
