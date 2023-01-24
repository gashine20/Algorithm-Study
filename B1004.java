import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B1004 {
    //기하1 - 어린왕자
    //점이 원 안에 있는가
    //두 점 다 원 안에 있을 수 있음 - 제외!!
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine()); //테스트 케이스 개수

        int[] count = new int[T]; //진입/이탈 횟수

        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            int n = Integer.parseInt(br.readLine()); //행성계 개수
            int[][] planet = new int[n][3]; //진입/이탈 횟수

            for (int j = 0; j < n; j++) {
                StringTokenizer st2 = new StringTokenizer(br.readLine());
                planet[j][0] = Integer.parseInt(st2.nextToken());
                planet[j][1] = Integer.parseInt(st2.nextToken());
                planet[j][2] = Integer.parseInt(st2.nextToken());
            }

            for (int k = 0; k < n; k++) {
                int dist1 = (x1 - planet[k][0]) * (x1 - planet[k][0]) + (y1 - planet[k][1]) * (y1 - planet[k][1]);//점과 원의 중심의 거리
                int dist2 = (x2 - planet[k][0]) * (x2 - planet[k][0]) + (y2 - planet[k][1]) * (y2 - planet[k][1]);//점과 원의 중심의 거리
                int r2 = (planet[k][2] * planet[k][2]);
                if (!(dist1 <= r2 && dist2 <= r2)) {//두 점 다 원 안에 있을 수 있음 - 제외!!
                    if (dist1 <= r2 || dist2 <= r2)
                        count[i]++;
                }
            }

        }
        for (int j : count)
            System.out.println(j);

    }

}
