import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B5086 {
    //정수론 및 조합론 - 배수와 약수
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 0: neither 1: factor 약수, 2: multiple 배수
        int count = 0;
        int n, m;
        int[] relation = new int[10000];
        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());

            if (n == 0 && m == 0) break;

            if (n > m) {
                if (n % m == 0) //배수
                    relation[count] = 2;
            } else if (n < m) {
                if (m % n == 0) //약수
                    relation[count] = 1;
            }
            count++;
        }

        for (int i = 0; i < count; i++) {
            if (relation[i] == 0)
                System.out.println("neither");
            else if (relation[i] == 1)
                System.out.println("factor");
            if (relation[i] == 2)
                System.out.println("multiple");

        }
    }
}
