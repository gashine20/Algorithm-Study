import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B2442 {
    //별 찍기 -5
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        //5번째에 1개 찍고
        //4번째에 3개 찍고
        //3번째에 5개 찍고
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N - i; j++) {
                System.out.print(" ");
            }
            for (int j = 1; j <= 2 * i - 1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
