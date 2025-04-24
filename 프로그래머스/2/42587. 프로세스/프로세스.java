import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<Process> queue = new LinkedList<>();
        int count = 0;
        
        for(int i = 0; i < priorities.length; i++){
            queue.add(new Process(i, priorities[i]));
        }
        
        while(!queue.isEmpty()){
            Process now = queue.poll();
            boolean hasHighPriority = false;
            
            for(Process p: queue){
                if(now.priority < p.priority){
                    hasHighPriority = true;
                    break;
                }
            }
            
            if(hasHighPriority){
                queue.add(now);
            } else{
                count += 1;
                if(now.id == location){
                    return count;
                }
            }
        }
        return count;
    }
    
    class Process{
        int id;
        int priority;
        
        Process(int id, int priority){
            this.id = id;
            this.priority = priority;
        }
    }
}