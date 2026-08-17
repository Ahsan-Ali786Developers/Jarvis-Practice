#include <stdio.h>
int main()
{ 
    int n1, n2, n3;
    printf("Enter first number: ");
    scanf("%d",&n1);
    printf("\nEnter Second number : ");
    scanf("%d",&n2);
    printf("\nEnter third number : ");
    scanf("%d",&n3);
    if (n1>n2 && n1 > n3)
    {
        printf("Number 1 is largest!");
    }
    else if (n2>n1 && n2>n3)
    {
        printf("Number 2 is largest!");
    }
    else
    {
           printf("Number 3 is largest!");
    }
}
