import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B1037 {
    //정수론 및 조합론 - 약수
    public static void main(String[] args) throws IOException {
        //진짜 약수 주어질 때 N을 구하시오
        // 9의 약수 3
        int N;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int Count = Integer.parseInt(br.readLine());
        int[] real = new int[Count];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for(int i=0;i<Count;i++){
            real[i] = Integer.parseInt(st.nextToken());
        }

        if(Count == 1){
            N = real[0]*real[0];
        }
        else{
            Arrays.sort(real);
            N = real[0]*real[real.length-1];
        }

        System.out.println(N);
    }
}
