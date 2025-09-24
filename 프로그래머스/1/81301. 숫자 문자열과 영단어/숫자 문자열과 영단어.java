import java.util.*;

class Solution {
    public int solution(String s) {
        String result = "";
        String[] number = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        for(int i = 0; i < number.length; i++){
            s = s.replaceAll(number[i], Integer.toString(i));
        }
        return Integer.parseInt(s);
    }
}