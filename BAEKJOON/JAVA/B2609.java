import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B2609 {
    //정수론 및 조합론 - 최대공약수와 최소공배수
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int mm=0;
        int maxdi=0,mindi; //최대공약수, 최소공배수
        int min = n;
        if (min > m) min = m;

        for (int i = 1; i <= min; i++) { //24 18 , min=18
            if (n % i == 0 && m % i == 0) {
                maxdi =i;
                mm = m / i;
            }
        }

        mindi = n * mm;
        System.out.println(maxdi);
        System.out.println(mindi);

    }
}
