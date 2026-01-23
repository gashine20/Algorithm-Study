import java.util.*;

class Solution {
    public int[] solution(String[][] places) {
        int len = places.length;
        int[] answer = new int[len];
        for(int i = 0; i < len; i++){
            answer[i] = 1;
        }
        
        ArrayList<int[]> result = new ArrayList<>();
        
        for(int i = 0; i < len; i++){
            String[] place = places[i];
            
            // 형 변환
            String[][] field = format(place);
            // System.out.println(i+1 +"번째 중");
            
            for(int k = 0; k < 5; k ++){
                for(int p = 0; p <5; p++){
                    if(field[k][p].equals("P")){ // P 발견하면 사각지대에 P 있나 확인
                        result = find(k, p, field);
                        //P가 있으면
                        if(!result.isEmpty()){
                            // 거리두기 잘 지켰나 확인
                            if(!validateDistance(result, k, p, field)){ // 지키지못하면
                                answer[i] = 0;
                                break;
                            }
                        }
                    }
                }
            }
            
        }
        
        return answer;
    }
    
    public boolean validateDistance(ArrayList<int[]> result, int r, int c, String[][] field){
        for(int[] arr: result){
            int r2 = arr[0];
            int c2 = arr[1];
            // System.out.println("(" + r + "," + c + ") 근처에 " + "(" + r2 + "," + c2 + ") 있다.");
            
            // 거리 확인
            int distance = Math.abs(r-r2) + Math.abs(c-c2);
            
            if(distance == 1) {
                return false;
            } 
            if (distance == 2){
                if(r == r2 ) {
                    if(!field[r][(c+c2)/2].equals("X")){
                        return false;     
                    }
                   
                } else if (c == c2){
                    if(!field[(r+r2)/2][c].equals("X")){
                        return false;     
                    }
                } else { // (1,2) (0,3) -> (1,3),(0, 2)
                    if(!field[r][c2].equals("X") || !field[r2][c].equals("X")){
                        return false;
                    }
                }
            }
        }
        return true;
    }
    
    public String[][] format(String[] place){ //["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"] -> [["P", "O"]]
        String[][] field = new String[5][5];
        
        for(int i = 0; i < 5; i++){
            field[i] = place[i].split("");
        }
        return field;
    }
    
    public ArrayList<int[]> find(int r, int c, String[][] field){ // r,c 기준으로 사각지대에 P 있는지 찾기
        ArrayList<int[]> result = new ArrayList<>();
        int[] dx = new int[] {0,0,0,0, 1, -1, 2, -2, 1, 1, -1, -1};
        int[] dy = new int[] {1, -1, 2 ,-2, 0, 0, 0, 0, 1, -1, -1, 1};
        
        for(int i = 0; i < dx.length; i++){
            int nx = r + dx[i];
            int ny = c + dy[i];
            
            if(nx >= 0 && nx < 5 && ny >= 0 && ny < 5) {
                if(field[nx][ny].equals("P")){
                    result.add(new int[]{nx, ny});
                }
                
            }
        }
        return result;
        
    }
}