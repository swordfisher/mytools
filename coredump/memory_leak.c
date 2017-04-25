#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    int n=512;
    while(1)
    {
        void * p = malloc(n);
        memset(p,0,n);
        if(p)
        {
            //printf("malloc success~\n");
        }else
        {
            //printf("malloc failed \n");
        }
        //usleep(5000);
    }
    return 0;
}

