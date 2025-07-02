class Solution {
    public int[] foundTileSize(int totalTile, int brown){
        for(int i=1; i < Math.sqrt(totalTile)+1; i++){
            if(totalTile % i == 0){
                int j = totalTile / i;
                int countBrown = i*2 + j*2 -4;
                if(brown == countBrown){
                    int[] arr = {j, i};
                    return arr;
                }
            }
        }
                    
        int[] arr = {0,0};
        return arr;
    }
    
    public int[] solution(int brown, int yellow) {
        int totalTile = brown + yellow;
        int[] answer = foundTileSize(totalTile, brown);
        
        return answer;
    }
}