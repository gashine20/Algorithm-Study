import java.util.*;
import java.io.*;

public class B1546 {
    //평균
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        double[] score = new double[N];
        double everage = 0.0;

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            score[i] = Double.parseDouble(st.nextToken());
        }

        double max = score[0];
        for (int i = 1; i < N; i++) {
            if (score[i] > max)
                max = score[i];
        }

        for (int i = 0; i < N; i++) {
            score[i] = (score[i] / max) * 100;
            everage += score[i];
        }
        System.out.println(everage / (N * 1.));
    }

}
