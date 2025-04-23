import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays){ 
        Map<String, Integer> genrePlayCount = new HashMap<>();
        Map<String, ArrayList<Song>> genreSongs = new HashMap<>();
        
        for(int i = 0; i < genres.length; i++){
            String genre = genres[i];
            int play = plays[i];
            
            genrePlayCount.put(genre, genrePlayCount.getOrDefault(genre, 0) + play);

            
            if(!genreSongs.containsKey(genre)){
                genreSongs.put(genre, new ArrayList<>());
            }
            genreSongs.get(genre).add(new Song(i, play));
        }
        
        List<String> sortedGenres = new ArrayList<>(genrePlayCount.keySet());
        sortedGenres.sort((g1, g2) -> genrePlayCount.get(g2) - genrePlayCount.get(g1));
        
        ArrayList<Integer> answer = new ArrayList<>();
        
        for(String genre: sortedGenres){
            ArrayList<Song> songs = genreSongs.get(genre);
            
            Collections.sort(songs);
            
            answer.add(songs.get(0).id);
            if(songs.size() > 1){
                answer.add(songs.get(1). id);
            }
        }
        
        return answer.stream().mapToInt(i->i).toArray();
    }
    
    class Song implements Comparable<Song>{
        int id;
        int plays;
        
        public Song(int id, int plays){
            this.id = id;
            this.plays = plays;
        }
        
        @Override
        public int compareTo(Song other){
            if(this.plays != other.plays){
                return other.plays - this.plays;
            }
            return this.id - other.id;
        }
    }
}