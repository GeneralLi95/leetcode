// @Date       : 2022/1/31 
// @Filename   : 137.cpp
// @Tag        :
// @Autor      : LI YAO
// @Difficulty :

#include <iostream>
#include <string>
#include <vector>

using namespace std;

// ----------------
class Solution {
public:
	int singleNumber(vector<int>& nums) {
		int ans = 0;
		for (int i = 0; i< 32; ++i){
			int total = 0;
			for (int num: nums){
				total += (num >> i) & 1;
			}
			
			if (total % 3){
				ans |= (1 << i);  // 或等于
			}
			
		}
		return ans;
	}
};


//------------------


int main(){
	Solution a;
	vector<int> b = {1,1,1,2,4,4,4,5,5,5,3,3,3};
	cout<<a.singleNumber(b);
	
}