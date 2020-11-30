#include <stdio.h>

int main (void)
{
  printf ("enter Minutes:");

  double GALLONS_PER_MIN = 1.5;
  int OUNCES_PER_GALLON = 128;
  int OUNCE_PER_BOTTLE = 16;

  int time_spent;
  scanf ("%d", &time_spent);

  double water_spent = time_spent * GALLONS_PER_MIN * OUNCES_PER_GALLON;	

  int num_of_bottles = (int)(water_spent / OUNCE_PER_BOTTLE);
  printf ("Bottles: %d", num_of_bottles);

}
