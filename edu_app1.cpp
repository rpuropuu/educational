#include <iostream>
//#include "pch.h"

using namespace std;

typedef struct {
	char a;
	int b;
}VAR;

int main(){
	setlocale(LC_ALL, "rus");
	VAR v = { '#', 5 };
	VAR* p = &v;
	cout << (*p).a << " " << (*p).b << endl;
	p->a = '*';
	p->b = -8;
	cout << p->a << " " << p->b << endl;
	return 0;
}