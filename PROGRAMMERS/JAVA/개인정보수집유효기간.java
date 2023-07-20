import java.util.*;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        
        ArrayList<Integer> answerList = new ArrayList<>();
        
        String[] kinds = new String[terms.length];
        String[] term = new String[terms.length]; 
        //1. temrs 정리 
        
        for(int i=0;i<terms.length;i++){
            String[] kindsSplit= terms[i].split(" "); //A 6 B 2 C 3
            kinds[i] = kindsSplit[0];
            term[i] = kindsSplit[1];
        }
        
        //2. privacies 정리
        String[] privaciesDate = new String[privacies.length];
        String[] privaciesKind = new String[privacies.length];
        
        for(int i=0;i<privacies.length;i++){
            String[] privaciesSplit= privacies[i].split(" "); // 2021.05.02 A
            privaciesDate[i] = privaciesSplit[0];
            privaciesKind[i] = privaciesSplit[1];
        }
        
        for(int i=0;i<privacies.length;i++){
            for(int j =0;j<terms.length;j++){
                if(privaciesKind[i].equals(kinds[j])){ //약관종류에 따라
                    //수집일자
                    int year = Integer.parseInt(privaciesDate[i].substring(0,4));
                    int month = Integer.parseInt(privaciesDate[i].substring(5,7));
                    int day = Integer.parseInt(privaciesDate[i].substring(8,10));
                    
                    //언제까지인지
                    month +=Integer.parseInt(term[j]); // 2019년 7월 1일 + 5개월 = 12
                    if(month>12){
                        year += (month/12); // +1
                        month %=12; // +7
                    }
                    
                    if(day==1){
                        if(month==1){
                            month=12;
                            year-=1;
                        }else{
                            month -=1;
                            day =28;
                        }
                        
                    }else{
                        day-=1;
                    }
                    
                    
                    System.out.println(year+" "+month+" "+day);
                        
                    //today와 비교 -지난거 찾기
                    int t_year = Integer.parseInt(today.substring(0,4));
                    int t_month = Integer.parseInt(today.substring(5,7));
                    int t_day = Integer.parseInt(today.substring(8,10));
                    
                    if(t_year>year){
                        answerList.add(i+1);
                    }
                    else if(t_year>=year && t_month>month){ 
                        answerList.add(i+1);
                    }
                    else if(t_year>=year && t_month>=month && t_day>day){ 
                        answerList.add(i+1);
                    }
                }
            }
        }
        int[] answer = new int[answerList.size()];
        for(int i=0;i<answerList.size();i++){
            answer[i]=answerList.get(i);
            
        }
        
        return answer;
        
    }
    
}
