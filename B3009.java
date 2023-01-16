import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B3009 {
    //기하1 - 네 번째 점
    //3개의 점을 알려주고 직사각형을 만들 수 있는 나머지 점 알아내기
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        int p[][] = new int[1001][2]; // 확인 배열
        //0으로 초기화
        for (int i = 0; i < p.length; i++) {
            for (int j = 0; j < 2; j++) {
                p[i][j] = 0;
            }
        }
        int x, y; // 입력받을 좌표들

        for (int i = 0; i < 3; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());
            p[x][0]++;
            p[y][1]++;
        }

        for (int i = 0; i < p.length; i++) {
            if (p[i][0] == 1) {//x 좌표
                System.out.print(i + " ");
                break;
            }
        }
        for (int i = 0; i < p.length; i++) {
            if (p[i][1] == 1) {//y 좌표
                System.out.print(i);
                break;
            }
        }
    }
}
