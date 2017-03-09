#include <iostream>
using namespace std;
int main()
{
char **p;
char *name[]={"a","b","C++","d","d"};
p=name+2;
cout<<*p<<endl;
cout<<**p<<endl;
return 0;
}
