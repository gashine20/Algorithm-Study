import java.io.*;
import java.lang.String;

public class B25501 {
    //재귀의 귀재
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        String[] SS = new String[T];

        for (int i = 0; i < T; i++) {
            String S = br.readLine();
            SS[i] = isPalindrome(S);
        }
        for (int i = 0; i < T; i++) {
            System.out.println(SS[i]);
        }
    }

    public static String isPalindrome(String s) {
        return recursion(s, 0, s.length() - 1, 0);
    }

    public static String recursion(String s, int l, int r, int cnt) {
        cnt++;
        if (l >= r) return "1 " + cnt;
        else if (s.charAt(l) != s.charAt(r)) return "0 " + cnt;
        else return recursion(s, l + 1, r - 1, cnt);
    }
}
