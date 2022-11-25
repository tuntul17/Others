#include <iostream>
using namespace std;

int func(int a, int c, int b){
	return((c+a)/b);
}

void swap(int& x, int& y, int& z){
	x=y; y=z; z=x;
}

int main(){
	int a = 1, b=2, c = 3, d;
	swap(a,b,c);
	d = func(a,b,c);
	
	cout<<d;
	
	return 0;	
}
