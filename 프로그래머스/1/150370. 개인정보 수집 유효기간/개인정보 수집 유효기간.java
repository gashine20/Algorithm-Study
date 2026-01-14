import java.util.*;


class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        ArrayList<Integer> result = new ArrayList<>();
        HashMap<String, Integer> map = new HashMap<>();
        int todayCount = calc(today);
        
        
        for(String term : terms){
            String[] s = term.split(" ");
            map.put(s[0], map.getOrDefault(s[0], Integer.parseInt(s[1]) * 28));
        }
        
        for(int i = 0; i < privacies.length; i++){
            String privacy = privacies[i];
            String[] s = privacy.split(" ");
            
            int dayCount = calc(s[0]);
            
            if (dayCount + map.get(s[1]) - 1 < todayCount) {
                result.add(i+1);
            }
        }
        
        int[] answer = result.stream()
            .mapToInt(Integer::intValue)
            .toArray();
        
        return answer;
    }
    
    public int calc(String day) { // 2022.05.19 -> 2022*12*28 + 5 * 28 + 19
        String[] d = day.split("\\.");
        System.out.println(d[0]);
        
        return Integer.parseInt(d[0])*12*28 + Integer.parseInt(d[1])*28 + Integer.parseInt(d[2]);
    }
}