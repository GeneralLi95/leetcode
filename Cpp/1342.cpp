// @Date       : 2022/1/31 
// @Filename   : 1342.cpp
// @Tag        :
// @Autor      : LI YAO
// @Difficulty :

#include <iostream>

using namespace std;

class Solution {
public:
	int numberOfSteps(int num) {
		int ret = 0;
		while (num){
			ret += (num > 1 ? 1: 0) + (num & 0x01);
			num >>= 1;
		}
		return ret;
	}
};



int main() {
	Solution a;
	cout<<a.numberOfSteps(123);
}