import java.io.*;
import java.util.*;

public class B2525 {
    //오븐 시계
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken()); //시
        int B = Integer.parseInt(st.nextToken()); //분

        int C = Integer.parseInt(br.readLine()); //걸리는 시간

        int h = A + C / 60;
        int m = B + C % 60;
        if (m == 60) { //60분?
            m = 0;
            h += 1;
        }
        if (m > 60) { //68분?
            m %= 60;
            h += 1;
        }
        if (h >= 24) { //25시?
            h %= 24;
        }

        System.out.print(h + " " + m);

    }
}
