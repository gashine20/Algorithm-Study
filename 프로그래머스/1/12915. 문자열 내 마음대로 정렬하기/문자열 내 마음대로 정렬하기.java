import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public String[] solution(String[] strings, int n) {
        ArrayList<String> stringList = new ArrayList<>(Arrays.asList(strings));
        List<String> sortedList = stringList.stream()
            .sorted((s1, s2) -> {
                int cmp = Character.compare(s1.charAt(n), s2.charAt(n));
                if(cmp == 0){
                    return s1.compareTo(s2);
                }
                return cmp;
            })
            .collect(Collectors.toList());
        
        return sortedList.toArray(new String[0]);
    }
}