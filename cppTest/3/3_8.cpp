#include<iostream>

using namespace std;

int main()
{
int year;
bool leap;
cout<<"Please enter year:";
cin>>year;
leap = (year % 4 == 0&& year % 100 !=0) || year % 400 == 0;
if (leap)
cout<<year<<" is";
else 
cout<<year<<" is not";
cout<<" a leap year."<<endl;
return 0;
}

