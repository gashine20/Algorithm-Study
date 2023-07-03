import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class B9506 {
    //약수들의 합
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n;
        ArrayList<Integer> nn = new ArrayList<>();
        while (true) {
            n = Integer.parseInt(br.readLine());
            if (n == -1) break;
            nn.add(n);
        }


        for (int x : nn) {
            if (isF(x)) {
                System.out.print(x + " = 1 ");
                for (int i = 2; i < x; i++) {
                    if (x % i == 0)
                        System.out.print("+ " + i + " ");

                }
                System.out.println();
            } else System.out.println(x + " is NOT perfect.");
        }
    }

    //1. 완전수 인지 아닌지 먼저 확인.
    public static boolean isF(int n) {
        int sum = 0;
        for (int i = 1; i < n; i++) {
            if (n % i == 0) {
                sum += i;
            }

        }
        if (sum == n) return true;
        else return false;
    }
}
