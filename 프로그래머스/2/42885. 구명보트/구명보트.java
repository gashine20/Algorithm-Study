import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        int left = 0;
        int right = people.length -1;
        
        Arrays.sort(people);
        
        while(left <= right){
            if(people[left] + people[right] <= limit){
                answer++;
                left++;
                right--;
            }
            else{ // 혼자서 타야함
                answer++;
                right--;
            }
        }
        
        return answer;
    }
}

// 몸무게 정렬 [40, 50, 50, 60, 70, 80] 
// 그래도 구명보트 한 번에 최대 2명씩만 가능