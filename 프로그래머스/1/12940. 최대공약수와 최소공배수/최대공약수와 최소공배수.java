class Solution {
    public int[] solution(int n, int m) {
        int g = gcd(n, m);
        int d = ((n*m)/g);
        
        int[] answer = {g, d};
        return answer;
    }
    
    // 유클리드 호제법
    public int gcd(int a, int b){
        while(b != 0){
            int tmp = a % b;
            a = b;
            b = tmp;
        }
        return a;
    }
}