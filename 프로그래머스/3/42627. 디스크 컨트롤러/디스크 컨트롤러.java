import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        int end = 0;
        int jobsIdx = 0;
        int count = 0;
        
        Arrays.sort(jobs, (o1, o2) -> (o1[0] - o2[0]));
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);
        
        while(count < jobs.length) {
            while(jobsIdx < jobs.length && jobs[jobsIdx][0] <= end){
                pq.add(jobs[jobsIdx++]);
            }
            
            if(pq.isEmpty()){
            end = jobs[jobsIdx][0]; // 다음 Job의 시작 시간으로 설정
            } else{
                int[] temp = pq.poll();
                answer += end + temp[1] - temp[0]; // 시작한 시간 + 소요 시간 - 하려고 했던 시간
                end += temp[1];
                count++;
            }
        }
        
        return (int) Math.floor(answer / jobs.length);
    }
}