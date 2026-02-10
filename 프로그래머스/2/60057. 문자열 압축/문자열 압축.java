class Solution {
    public int solution(String s) {
        int answer = Integer.MAX_VALUE;
        
        // 문자열 제일 앞에서 정해진 길이 만큼 잘라야함
        // 최대 자르는 길이 s/2
        int n = s.length();
        StringBuilder sb = new StringBuilder(s);
        for(int i = 1; i <= n/2+1; i++) {
            int result = cutString(sb, i); // i 크기 만큼 자름
            answer = Math.min(answer, result);
            
        }
        return answer;
    }
     
    public int cutString(StringBuilder sb, int k) { // n개 단위로 잘랐을 때 길이 return
        StringBuilder sb2 = new StringBuilder();
        
        // n개씩 단어를 자름, 몇개 나왔는지 count
        int n = sb.length();
        String str = new String(sb.substring(0,k));
        int count = 1;
        for(int i = k; i < n-k+1; i+=k) {
            int end = i+k > n-1 ? n : i+k;
            String s = sb.substring(i, end).toString();
            
            if(str.equals(s)) {
                count++;
            } else{ // 앞 단어랑 다르면
                if(count == 1) { // 한글자 혼자라면
                    sb2.append(str);
                    str = s;
                    continue;
                }
                sb2.append(count+""+str);
                str = s;
                count = 1; // 초기화
            }
            
        }
        
        // 마지막 붙이기
        if(count > 1) {
            sb2.append(count+""+str);
        } else {
            sb2.append(str);
        }
        
        // n이 k로 나누어 떨어지지 않으면 맨 마지막꺼 안함
        if(n%k != 0) {
            sb2.append(sb.substring(k*(n/k), n));
        }
        
        // System.out.println(k + "개로 자를 때: " + sb2.toString());
        return sb2.length();
    }
}