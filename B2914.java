import java.io.*;
import java.util.*;

public class B2914 {
    //저작권
    public static void main(String[] args) throws IOException {
        //멜로디 개수 / 곡의 개수 = 올림한 평균값
        // ? / 곡의개수 = 평균값
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int A = Integer.parseInt(st.nextToken()); //곡의 개수
        int I = Integer.parseInt(st.nextToken()); //평균값

        System.out.println((I - 1) * A + 1);
    }
}
