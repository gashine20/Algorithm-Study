import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class B2587 {
    //대표값2
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] num = new int[5];
        int avg = 0, mid;

        for (int i = 0; i < num.length; i++) {
            num[i] = Integer.parseInt(br.readLine());
            avg += num[i];
        }

        avg /= 5; //평균
        Arrays.sort(num);
        mid = num[num.length / 2];

        System.out.println(avg);
        System.out.println(mid);

    }
}
