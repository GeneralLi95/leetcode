

    class RangeFreqQuery {
        int[] myList_a;
        public RangeFreqQuery(int[] arr) {
                this.myList_a = arr;
            
        }
        
        public int query(int left, int right, int value) {
            int num = 0;
            for(int i = left; i<=right; i++){
//              if (myList_a[i] == value){
//                  num++;
//              }
                
            }
            return num;
        }
        public static void main(String[] args) {
            System.out.println("Hello World"); // 输出 Hello World
            int[] myList = {12 , 33,  4,  56, 22, 2, 34, 33, 22, 12, 34, 56};
            RangeFreqQuery rangeFreqQuery = new RangeFreqQuery(myList);
            systerangeFreqQuery.query(1, 2, 4); // 返回 1 。4 在子数组 [33, 4] 中出现 1 次。
            rangeFreqQuery.query(0, 11, 33); // 返回 2 。33 在整个子数组中出现 2 次。
        }
    }
    
