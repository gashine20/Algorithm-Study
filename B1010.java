import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B1010 {
    //다리 놓기 - mCn
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T= Integer.parseInt(br.readLine()); //테스트 개수
        int[] array = new int[T];

        for(int i=0;i<T;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int NN=1,MM=1;
            for(int j=1;j<=N;j++){
                NN*=j;
            }
            for(int j=1;j<=M;j++){
                MM*=j;
            }
            array[i] = MM/NN;
        }
        for(int a: array){
            System.out.println(a);
        }

    }
}
