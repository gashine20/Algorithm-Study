class Solution {
    public int[] solution(int n, int m) {
        int g = gcd(n, m);
        int d = g * (n/g)* (m/g);
        
        int[] answer = {g, d};
        return answer;
    }
    
    public int gcd(int n, int m){
        if(n > m){
            int tmp = n;
            n = m;
            m = tmp;
        }
        
        int d = 1;
        for(int i = 1; i <= n; i ++ ){
            if(n % i == 0 && m % i == 0){
                d = i;
            }
        }
        
        return d;
    }
}