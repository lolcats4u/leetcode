#include <string.h>
#include <stdio.h>
int main(void)
{
    char *number1 = "123";
    char *number2 = "1231";
    char *number3 = "551";

    char *test1[2] = [ number1, '3' ];
    char *text2[2] = [ number2, '1' ];
    char *text3[2] = [ number3, '1' ];

    char *tests[3] = [ test1, test2, test3 ];
    for (int i = 0; i < 3; i++)
    {
        removeDigit(tests[i][0], tests[i][1]);
    }
}
char *removeDigit(char *number, char digit)
{
    int count = 0;
    while (number[count] != "/0")
    {
        if (number[count] == digit && number[count + 1] > number[count])
        {
        }
    }
}