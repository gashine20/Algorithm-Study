import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B1267 {
    //핸드폰 요금
    //영식 Y 민식 M
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] callTime = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            callTime[i] = Integer.parseInt(st.nextToken());
        }

        int Y = 0, M = 0;
        for (int i = 0; i < N; i++) {
            Y += 10 + (callTime[i] / 30) * 10;
            M += 15 + (callTime[i] / 60) * 15;
        }

        if (Y < M) {
            System.out.println("Y " + Y);
        } else if (Y == M) {
            System.out.println("Y M " + Y);
        } else {
            System.out.println("M " + M);
        }
    }
}
