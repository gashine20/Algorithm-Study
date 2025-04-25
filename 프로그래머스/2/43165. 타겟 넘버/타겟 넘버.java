import java.util.*;

class Solution {
    int answer;
    
    public int solution(int[] numbers, int target) {        
        DFS(0, 0, numbers, target);
        return answer;
    }
    
    public void DFS(int index, int value, int[] numbers, int target){
        if(index >= numbers.length) {
            if(value == target){
                answer++;
            }
            return;
        }
        
        DFS(index+1, value+numbers[index], numbers, target);
        DFS(index+1, value-numbers[index], numbers, target);

    }
}