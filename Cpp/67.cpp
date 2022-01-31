// @Date       : 2022/1/31 
// @Filename   : 67.cpp 二进制求和
// @Tag        :
// @Autor      : LI YAO
// @Difficulty : Easy

#include <iostream>
#include <string>


using namespace std;

// ----------------
class Solution {
public:
	string addBinary(string a, string b) {
		int i = a.length() - 1;
		int j = b.length() - 1;
		int carry = 0;
		string builder;
		
		// 循环相加两个字符串相同长度的低位数部分
		while ( i>=0 and j >=0){
			int sum = carry;
			cout<<"a---"<<a[i] - '0'<<endl;
			cout<<"b---"<<b[j] - '0'<<endl;
			sum += a[i--] - '0';
			cout<<sum<<endl;
			sum += b[j--] - '0';
			cout<<sum<<endl;
			carry = sum / 2; // 是否进位
			
			builder += to_string(sum%2);
		}
		// 如果 a 还没有遍历完成（a串比b串长），则继续遍历添加 a 的剩余部分
		while (i >= 0){
			int sum = carry + a[i--] - '0';
			carry = sum/2;
			builder += to_string(sum%2);
		}
		
		while(j >= 0){
			int sum = carry + b[j--] - '0';
			carry = sum / 2;
			builder += to_string(sum%2);
		}
		
		// 如果 carry 不等于0 还有个进位数没加进去，需要补充
		if (carry == 1){
			builder += to_string(carry);
		}
		
		// 反转字符串获得正常结果
		reverse(builder.begin(), builder.end());
		
		return builder;
	}
};


//------------------


int main(){
	Solution a;
	cout<<a.addBinary("1010", "1011");  // 结果应该是 10101
	
};