import java.util.*;

class Solution {
    public int solution(int N, int number) {
        List<Set<Integer>> list = new ArrayList<>();
        
        for(int i = 0; i <= 9; i++){
            list.add(new HashSet<>());
        }
        
        list.get(1).add(N); // 1개로 만들 수 있는건 N 뿐
        
        for(int i = 2; i <=9; i++){
            Set<Integer> countSet = list.get(i);
            
            for(int j = 1; j < i; j ++){
                Set<Integer> preSet = list.get(j);
                Set<Integer> postSet = list.get(i-j);
                
                for(int preNum : preSet){
                    for(int postNum : postSet){
                        countSet.add(preNum + postNum);
                        countSet.add(preNum - postNum);
                        countSet.add(preNum * postNum);
                        
                        if(preNum!= 0 && postNum!= 0){
                            countSet.add(preNum / postNum);
                        }
                        
                    }
                }
            }
            countSet.add(Integer.parseInt(String.valueOf(N).repeat(i)));
        }
        
        for(Set<Integer> nums : list){
            if(nums.contains(number)){
                return list.indexOf(nums); 
            }
        }
        
        return -1;
    }
}