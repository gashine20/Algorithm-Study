import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        ArrayList<int[]> list = new ArrayList<>(); // {location, priority}
        ArrayList<Integer> result = new ArrayList<>();
        
        for(int i = 0 ; i < priorities.length; i++){
            int[] array = new int[2];
            array[0] = i;
            array[1] = priorities[i];
            list.add(array);
        }
        
        while(list.size()!=0){
            int[] now = list.get(0);
            int count = 0;
            list.remove(0);
            for(int i = 0; i < list.size(); i++){ // 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있는 경우
                int[] next = list.get(i);
                count += 1;
                if(now[1] < next[1]){ 
                    // System.out.println("now:" + now[1] + " < " + "next:" + next[1]);
                    list.add(now);
                    break;
                }
            }
            // 우선순위 더 높은 프로세스가 없는경우
            if(count == list.size()){
                result.add(now[0]); // location 
            }
            if(list.size() == 0){ // 마지막꺼라면
                result.add(now[0]);
            }
            
        }
        // System.out.println(result);
        int answer = result.indexOf(location) + 1;
        
        return answer;
    }
}