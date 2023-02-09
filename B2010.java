import java.io.*;

public class B2010 {
    //플러그
    //마지막 꺼는 다 꽂을 수 있음
    //멀티탭 4개가 있고, 2 5 8 4 이면? 1+4+7+4= 16 아닌가

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int con = 0;

        for (int i = 0; i < N; i++) {
            if (i == (N - 1))
                con += Integer.parseInt(br.readLine());
            else {
                con += (Integer.parseInt(br.readLine()) - 1);
            }
        }
        System.out.println(con);
    }
}
