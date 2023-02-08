import java.io.*;
import java.util.StringTokenizer;

public class B1547 {
    //공
    public static void main(String[] args) throws IOException {
        // 첫번 째꺼를 생각
        // 공이 어떻게 하면 사라지는데..?
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int M = Integer.parseInt(br.readLine()); //횟수

        int first = 1;

        for (int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int X = Integer.parseInt(st.nextToken());
            int Y = Integer.parseInt(st.nextToken());

            if (X == first && Y == first) {
                first = -1;
            } else {
                if (X == first) {
                    first = Y;
                } else if (Y == first) {
                    first = X;
                }
            }
        }

        System.out.println(first);

    }
}
