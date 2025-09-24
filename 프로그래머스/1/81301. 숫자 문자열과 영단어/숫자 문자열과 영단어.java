import java.util.*;

class Solution {
    public int solution(String s) {
        String result = "";
        String[] number = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        List<String> numList = new ArrayList<>(Arrays.asList(number));
        
        String S = "";
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(Character.isDigit(c)){
                // 문자열 숫자로 바꾸기
                String k = "";
                for(int j = 0; j < S.length(); j++){
                    k += S.charAt(j);
                    if(numList.contains(k)){
                        result += numList.indexOf(k);
                        k = "";
                    }
                }
                result += c;
                S = "";
            } else{
                S += c;
            }
        }
        
        // S에 있는 값 result에 추가
        String k = "";
        for(int j = 0; j < S.length(); j++){
            k += S.charAt(j);
            if(numList.contains(k)){
                result += numList.indexOf(k);
                k = "";
            }
        }
        
        return Integer.parseInt(result);
    }
}