import java.io.*;

public class B2588 {
    //곱셈
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int a = Integer.parseInt(br.readLine());
        int b = Integer.parseInt(br.readLine());

        int b1 = b / 100; //100의 자리, 385/100 = 3
        int b2 = (b % (b1 * 100)) / 10; //10의 자리, 385/300/10
        int b3 = (b % (b1 * 100)) % 10; //1의 자리

        int a1 = a * b3;
        int a2 = a * b2;
        int a3 = a * b1;
        System.out.println(a1);
        System.out.println(a2);
        System.out.println(a3);
        System.out.println(a1 + (a2 * 10) + (a3 * 100));
    }
}
