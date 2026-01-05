class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        
        int[] wallpaper = new int[n];
        for(int s : section) {
            wallpaper[s-1] = 1;
        }
        
        for(int i = 0; i < n; i++){
            if(wallpaper[i] == 1) {
                // paint
                for(int j = i; j < i+m; j++){
                    if(j >= n){
                        break;
                    }
                    wallpaper[j] = 0;
                }
                answer+=1;
            }
        }
        
        
        return answer;
    }
}