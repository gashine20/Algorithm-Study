import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B11050 {
    //정수론 및 조합론 - 이항 계수 1
    //이항계수 -> n!/(k!(n-k)!) ㅋㅋ?
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        for(int i=N-1;i>=N-K;i--){
            N*=i;
        }
        for(int i=K-1;i>=1;i--){
            K*=i;
        }
        System.out.println(N/K);
    }
}
