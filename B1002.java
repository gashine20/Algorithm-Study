import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B1002 {
    //기하1 - 터렛
    //두 원의 중심 거리와 두 원 반지름의 합과 비교
    //외접 내접 고려
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine()); //케이스 개수
        int[] pcount = new int[T];

        for (int i = 0; i < T; i++) {
            int dist, rd_dist, rs_dist;

            StringTokenizer st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int r1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            int r2 = Integer.parseInt(st.nextToken());

            dist = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
            rd_dist = (r1 - r2) * (r1 - r2); //차
            rs_dist = (r1 + r2) * (r1 + r2); //합

            if (x1 == x2 && y1 == y2) {//중심이 같고 반지름이 다를 때 고려
                if (r1 == r2) //무한대
                    pcount[i] = -1;
                else
                    pcount[i] = 0;
            } else if (dist == rd_dist) { //내접 1
                pcount[i] = 1;
            } else if (dist == rs_dist) { //외접 1
                pcount[i] = 1;
            } else if (dist < rd_dist) { //내접 0
                pcount[i] = 0;
            } else if (dist > rs_dist) { //외접 0
                pcount[i] = 0;
            } else {
                pcount[i] = 2;
            }

        }

        for (int j : pcount) {
            System.out.println(j);
        }
    }
}
