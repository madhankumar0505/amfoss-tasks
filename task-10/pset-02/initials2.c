#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>

int main(void) {

    string name = get_string("Enter name \n");
    int len = strlen(name);
    bool safe = true;
    
    for (int i=0; i < len; i++) 
        if (name[i] == ' ') 
        {
            safe = true;
            continue;
        }
        else if (safe)
        {
            safe = false;
            printf("%c", toupper(name[i]));
        }
        
    return 0;
}
