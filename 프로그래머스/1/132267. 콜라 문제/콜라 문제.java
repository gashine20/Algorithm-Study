class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;
        // a개를 가져다 주면 b병 줌, n개 가져다주면 얼마나 ? 
        
        int total = n;
        while(total >= a) {
            int get = total/a * b;
            answer += get;
            int remain = total % a;
            
            total = remain + get;
        }
        
        
        
        return answer;
    }
}