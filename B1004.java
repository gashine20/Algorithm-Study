import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B1004 {
    //기하1 - 어린왕자
    //점이 원 안에 있는가
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine()); //테스트 케이스 개수

        int[] count = new int[T]; //진입/이탈 횟수

        for(int i=0;i<T;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            int n = Integer.parseInt(br.readLine()); //행성계 개수
            int[][] planet = new int[n][3]; //진입/이탈 횟수

            for(int j=0;j<n;j++){
                StringTokenizer st2 = new StringTokenizer(br.readLine());
                planet[j][0] = Integer.parseInt(st2.nextToken());
                planet[j][1] = Integer.parseInt(st2.nextToken());
                planet[j][2] = Integer.parseInt(st2.nextToken());
            }

            //점과 원의 중심의 거리 <= 반지름
            PinC(count, i, x1, y1, n, planet);
            PinC(count, i, x2, y2, n, planet);

        }
        for(int j:count)
            System.out.println(j);


    }

    private static void PinC(int[] count, int i, int x2, int y2, int n, int[][] planet) {
        for(int k=0;k<n;k++) {
            int dist = (x2-planet[k][0])*(x2-planet[k][0]) + (y2-planet[k][1])*(y2-planet[k][1]);//점과 원의 중심의 거리
            if(dist<=(planet[k][2]*planet[k][2])) {
                count[i]++;
            }
        }
    }
}
