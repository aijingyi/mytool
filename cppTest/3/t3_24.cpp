#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
int i,j,k,m,n;
n= 7;

for (j=1;j<n;j=j+2)
    {   
    for(i=1;i<=j;i++)
    {
    cout<<'*';
    }
    cout<<endl;
    }

for (m=n;m>=1;m=m-2)
    {
    for(k=1;k<=m;k++)
    {
    cout<<'*';
    }
    cout<<endl;
    }
return 0;

}
