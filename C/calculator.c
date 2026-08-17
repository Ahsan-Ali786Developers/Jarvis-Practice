#include <stdio.h>

int main()
{
    int n1,n2;
    printf("Enter 1 : ");
    scanf("%d",&n1);
    printf("Enter 2 : ");
    scanf("%d",&n2);
    printf("Sum = %d\n",n1+n2);
    printf("Subtract = %d\n",n1-n2);
    printf("Multiplication = %d\n",n1*n2);
    printf("Enter a number ");
    int n;
    scanf("%d",&n);
    if (n>0){
        printf("Number is positive!");
    }else if(n<0){printf("number is negative!");}
    else{printf("zero");}
    
    if(n%2==0){printf("\nnumber is even");}
    else{printf("\nnumber is odd!");}

    if(n1>n2){printf("number 1 is large!");}
    else if(n1==n2){printf("both equal!");}
    else{printf("number 2 is large!");}
    return 0;

}