#include <iostream>
#include <vector>
using namespace std;


class RangeFreqQuery {
	public:
		RangeFreqQuery(vector<int>& arr) {
			this.arr = &arr;
		}
		
		int query(int left, int right, int value) {
			cout<<"hello"<<endl;
		}
};


int main(int argc, char *argv[]) {
	RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]);
	rangeFreqQuery.query(1, 2, 4); // 返回 1 。4 在子数组 [33, 4] 中出现 1 次。
	rangeFreqQuery.query(0, 11, 33); // 返回 2 。33 在整个子数组中出现 2 次。
	
}