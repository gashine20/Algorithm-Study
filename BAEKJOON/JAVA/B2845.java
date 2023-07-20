import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B2845 {
    //파티가 끝나고 난 뒤
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int L = Integer.parseInt(st.nextToken()); //1^2 당 사람 수
        int P = Integer.parseInt(st.nextToken());

        StringTokenizer st1 = new StringTokenizer(br.readLine());

        int[] news = new int[5];
        for (int i = 0; i < 5; i++) {
            news[i] = Integer.parseInt(st1.nextToken());
        }

        for (int i = 0; i < 5; i++) {
            System.out.print(news[i] - (L * P) + " ");

        }
    }
}
