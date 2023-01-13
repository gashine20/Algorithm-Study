import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class B11478 {
    //서로 다른 부분 문자열의 개수
    //문자열 S의 서로 다른 부분 문자열의 개수 구하기
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String S = br.readLine();
        HashSet<String> s = new HashSet<>();

        for(int i =S.length();i>0;i--){ // 5~0
            for(int j =0;j<i;j++) {
                //System.out.println(S.substring(j,i));
                //하나하나 쪼개서 넣기
                s.add(S.substring(j,i)); // (0,5), (1,5), (2,5), ...
            }

        }

        System.out.println(s.size());
    }
}
