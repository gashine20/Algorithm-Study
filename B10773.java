import java.io.*;

public class B10773 {
    //제로
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int K = Integer.parseInt(br.readLine());
        int[] money = new int[K];

        int top = -1;
        for (int i = 0; i < K; i++) {
            int n = Integer.parseInt(br.readLine());
            if (n == 0) {
                money[top--] = 0;
            } else money[++top] = n;
        }

        int sum = 0;
        for (int i = 0; i < K; i++) {
            sum += money[i];
        }

        System.out.println(sum);
    }
}
