#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>

int main(void) {

    string name = get_string("Enter \n");
    int len = strlen(name);
    
    for (int i=0; i < len; ++i) 
        if (i == 0 || (name[i] != ' ' && name[i-1] == ' ')) printf("%c", toupper(name[i]));
        
    return 0;
}
