import java.util.*;

class Solution {
    public boolean isPrime(int number){
        if(number == 0 || number == 1){
            return false;
        }
        if(number == 2){
            return true;
        }
        for(int i = 2; i < Math.sqrt(number) + 1; i++) {
            if(number % i == 0){
                return false;
            }
        }
        return true;
    }
    
    Set<Integer> numberSet = new HashSet<>();
    boolean[] visited;
    
    public void makeNumbers(String prefix, String numbers){
        if(!prefix.equals("")){
            numberSet.add(Integer.parseInt(prefix));
        }
        
        for(int i = 0; i < numbers.length(); i++){
            if(!visited[i]){
                visited[i] = true;
                makeNumbers(prefix + numbers.charAt(i), numbers);
                visited[i] = false;
            }
        }
    }
    
    public int solution(String numbers) {
        int answer = 0;
        // int[] nums = Arrays.stream(numbers.split(""))
        //                 .mapToInt(Integer::parseInt)
        //                 .toArray();
        
        
        visited = new boolean[numbers.length()];
        makeNumbers("", numbers); // 조합 만들기
        
        for(int num : numberSet){
            if(isPrime(num)){
                //System.out.println(num);
                answer +=1;
            }
        }
        return answer;
    }
}