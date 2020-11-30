#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    float to_dollar[] = {25, 10, 5, 1};   //array to store each corresponding values in dollars
    float change = get_float("Enter the change you want :");

    while(change< 0)
        change = get_float("Try again, Enter the change you want :");

    int coinNums = 0;
    
    change = change*100; //converting to cents
    int cents = round(owe); //to get rid of all the irrelevent digits that joins along a float
    for(int i=0; i<4; i++)
    {
        while(cents >= to_dollar[i])
        {
            coinNums ++;
            cents -= to_dollar[i];
        }
    }
     printf("%i", coinNums);
}
