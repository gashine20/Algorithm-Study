import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class B2981 {
    //정수론 및 조합론 - 검문
    //시간 초과..
    public static void main(String[] args) throws IOException {
        int N;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        int[] paper = new int[N];
        //int[] mpaper = new int[N*2];
        int mpaper;

        for (int i = 0; i < N; i++) {
            paper[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(paper); //정렬
//        for(int i=0;i<(paper.length/2);i++){
//            mpaper[i] = paper[i*2+1]-paper[i*2];
//        }
        mpaper = paper[1] - paper[0];//초기화

        for (int i = 2; i < N; i++) {
            mpaper = gcd(mpaper, paper[i] - paper[i - 1]);
        }

        // 최대공약수의 약수들 찾기
        for (int i = 2; i <= mpaper; i++) {

            // i가 최대공약수의 약수라면 출력
            if (mpaper % i == 0) {
                System.out.print(i + " ");
            }
        }

    }

    // 최대공약수 함수
    static int gcd(int a, int b) {
        while (b != 0) {
            int r = a % b;
            a = b;
            b = r;
        }
        return a;
    }
}
