#include <iostream>

using namespace std;

int f(int );
int main()
{
int n;
cout<<"please input number:";
cin>>n;
cout<<f(n)<<endl;
return 0;
}

int f(int n)
{
int c;
if (n==0 || n==1) c=1;
else c=f(n-1)*n;
return c;
}
