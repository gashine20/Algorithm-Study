import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class B2477 {
    //기하1 - 참외밭
    //
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int K = Integer.parseInt(br.readLine()); //1m^2에 자라는 참외 수

        int wmax, wmin, hmax, hmin;
        int area = 0;
        int[] width = new int[2];
        int[] height = new int[2];


        for (int i = 0; i < 6; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int direct = Integer.parseInt(st.nextToken()); //방향
            // 1:동쪽, 2:서쪽, 3:남쪽, 4:북쪽
            int len = Integer.parseInt(st.nextToken()); //최대 최소

            if (direct == 1) { //동
                width[0] += len;
            }
            if (direct == 2) { //서
                width[1] += len;
            }
            if (direct == 3) { //남
                height[0] += len;
            }
            if (direct == 4) { //북
                height[1] += len;
            }
        }

        //w
        if (width[0] > width[1]) {
            wmax = width[0];
            wmin = width[1];
        } else {
            wmax = width[0];
            wmin = width[1];
        }

        //h
        if (height[0] > height[1]) {
            hmax = height[0];
            hmin = height[1];
        } else {
            hmax = height[0];
            hmin = height[1];
        }

        if (wmax == wmin || hmax == hmin)
            area = wmax * hmax * K;
        else
            area = ((wmax * hmax) - (wmin * hmin)) * K;
        System.out.println(area);
    }
}
