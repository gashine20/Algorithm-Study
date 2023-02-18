import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B2953 {
    //나는 요리사다
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] score = new int[5];

        for (int i = 0; i < 5; i++) {

            StringTokenizer st = new StringTokenizer(br.readLine());
            score[i] += Integer.parseInt(st.nextToken());
            score[i] += Integer.parseInt(st.nextToken());
            score[i] += Integer.parseInt(st.nextToken());
            score[i] += Integer.parseInt(st.nextToken());

        }

        int max = 0;
        for (int i = 1; i < 5; i++) {
            if (score[i] > score[max])
                max = i;
        }

        System.out.println((max + 1)+ " " + score[max]);
    }
}
