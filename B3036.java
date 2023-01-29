import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B3036 {
    //정수론 및 조합론 - 링
    //분모 분자 최대공약수 구하기
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] ring = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            ring[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i < N; i++) {
            int maxdi = minmax(ring[0], ring[i]); //최대공약수
            System.out.println(ring[0] / maxdi + "/" + ring[i] / maxdi);
        }

    }

    static public int minmax(int a, int b) { //최대공약수
        int min = a;
        if (min > b) min = b;
        int maxdi = 1;

        for (int i = 1; i <= min; i++) {
            if (a % i == 0 && b % i == 0) {
                maxdi = i;
            }
        }

        return maxdi;
    }
}
