#include<iostream>

using namespace std;
int max(int x,int y)
{
int z;
z= x>y?x:y;
return z;
}
int main()
{
int max(int x, int y);
int a,b,c;
cout<<"Please enter two integer numbers:";
cin>>a>>b;
c = max(a,b);
cout<<"Max ="<<c<<endl;
return 0;

}
