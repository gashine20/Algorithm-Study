import java.util.*;

class Solution {
    public int countPlay(int[] order, int[][] dungeons, int k){
        int play = 0;
        for(int index: order){
            if(k >= dungeons[index][0]){
                play++;
                k-= dungeons[index][1];
            }
        }
        return play;
    }
    
    public void permute(int[] nums, int start, List<int[]> orders){
        if(start == nums.length){
            orders.add(nums.clone());
            return;
        }
        
        for(int i = start; i < nums.length; i++){
            swap(nums, start, i);
            permute(nums, start +1, orders);
            swap(nums, start, i); // 백트래킹
        }
    }
    
    public void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    public int solution(int k, int[][] dungeons) {
        // 순열 만듦
        int[] nums = new int[dungeons.length];
        for(int i = 0; i < dungeons.length; i ++){
            nums[i] = i;
        }
        
        List<int[]> orders = new ArrayList<>();
        
        permute(nums, 0, orders);
        
        
        // play한 결과 담기
        ArrayList<Integer> list = new ArrayList<>();
        for(int[] order: orders){
            int play = countPlay(order, dungeons, k);
            list.add(play);
        }
        
        int answer = Collections.max(list);
        
        return answer;
    }
}