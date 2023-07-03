import java.io.*;

public class B2446 {
    //별 찍기-9
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        //1 일땐 다 찍고
        //2 ,3,4.....
        for (int i = 1; i <= N - 1; i++) { //1 2 3 4
            for (int j = 1; j <= i - 1; j++) { // 0 1 2 3
                System.out.print(" ");
            }
            for (int j = 1; j <= 2 * (N - i + 1) - 1; j++) { // 9
                System.out.print("*");
            }
            System.out.println();
        }
        for (int j = 1; j <= N - 1; j++) { // 0 1 2 3
            System.out.print(" ");
        }

        System.out.print("*");
        System.out.println();

        for (int i = 2; i <= N; i++) { //2 3 4 5
            for (int j = 1; j <= N - i; j++) { // 3 2 1 0
                System.out.print(" ");
            }
            for (int j = 1; j <= 2 * i - 1; j++) { // 3 5 7 9
                System.out.print("*");
            }
            System.out.println();
        }

    }

}
