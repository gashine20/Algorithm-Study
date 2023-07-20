import java.io.*;

public class B2748 {
    //피보나치 수 2
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        System.out.println(ff(n));

    }

    public static int ff(int a) {
        if (a == 0) return 0;
        if (a == 1) return 1;

        return ff(a - 1) + ff(a - 2);
    }
}
