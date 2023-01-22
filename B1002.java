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
            int dist = 0, r_dist = 0, rmax = 0, rmin = 0;

            StringTokenizer st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int r1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            int r2 = Integer.parseInt(st.nextToken());

            //반지름 큰거 찾기
            if (r1 > r2) {
                rmax = r1;
                rmin = r2;
            } else {
                rmax = r2;
                rmin = r1;
            }

            dist = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
            r_dist = (r1 + r2) * (r1 + r2);

            if (x1 == x2 && y1 == y2) {//중심이 같고 반지름이 다를 때 고려
                if (r1 == r2)
                    pcount[i] = -1;
                else
                    pcount[i] = 0;
            } else if (dist < rmin) { //내접
                if (dist + rmin == rmax)
                    pcount[i] = 1;
                else if (dist + rmin > rmax)
                    pcount[i] = 2;
                else pcount[i] = 0;
            } else{ //외접
                if (dist > r_dist)
                    pcount[i] = 0;
                else if (dist == r_dist)
                    pcount[i] = 1;
                else
                    pcount[i] = 2;
            }


        }

        for (int i = 0; i < pcount.length; i++) {
            System.out.println(pcount[i]);
        }
    }
}
