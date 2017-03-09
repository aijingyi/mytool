#include <iostream>
using namespace std;

int main()
{
void swap(int *p1, int *p2);
int *point_1, *point_2, a,b;
cin>>a>>b;
point_1=&a;
point_2=&b;
if(a<b) swap(point_1,point_2);
cout<<"max="<<a<<" min="<<b<<endl;
return 0;
}

void swap(int *p1,int *p2)
{
int temp;
temp=*p1;
*p1=*p2;
*p2=temp;
}
