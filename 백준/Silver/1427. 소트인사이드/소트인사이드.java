import java.io.*;
import java.util.*;

public class Main {
    //소트인사이드
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[] num = new int[10];

        int cnt = 0;
        while (N != 0) {
            num[cnt++] = N % 10;
            N /= 10;
        }

        Arrays.sort(num);
        
        for (int i = 9; i > 9 - cnt; i--) {
            System.out.print(num[i]);
        }
    }
}
