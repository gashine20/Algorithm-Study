class Solution {
    public boolean solution(String s) {
        if(s.length() == 4 || s.length() == 6){
            return isNumber(s);
        }
        return false;
    }
    
    public boolean isNumber(String s){
        char[] C = s.toCharArray();
        
        for(char c : C)
        if(!Character.isDigit(c)){
            return false;
        }
        
        return true;
    }
}