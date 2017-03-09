#include <iostream>
using namespace std;
int main()
{
int max(int x, int y);
int a,b,m;
cin>>a>>b;
m=max(a,b);
cout<<"max="<<m<<endl;
return 0;
}

int max(int x, int y)
{
int z;
if(x>y) z=x;
else z=y;
return z;
}
