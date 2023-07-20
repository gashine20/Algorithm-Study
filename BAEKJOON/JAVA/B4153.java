import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B4153 {
    //기하1 - 직각삼각형
    //마지막 줄은 0 0 0 입력으로 파악
    //max를 구해야돼!!
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] pita = new int[30001]; // T/F 구별
        int[] abc = new int[4]; //한 변의 길이


        for (int i = 0; i < pita.length; i++) {
            //입력 받기

            StringTokenizer st = new StringTokenizer(br.readLine());
            abc[0] = Integer.parseInt(st.nextToken());
            if (abc[0] == 0) break;
            abc[1] = Integer.parseInt(st.nextToken());
            abc[2] = Integer.parseInt(st.nextToken());

            int x = 0; //max 제외한 것 제곱의 합
            int max = 0; //index로 저장

            //max 찾기
            for (int j = 0; j < abc.length; j++) {
                if (abc[max] < abc[j]) max = j;
            }

            //피타고라스
            for (int j = 0; j < abc.length; j++) {
                if (max != j) {
                    x = x + (abc[j] * abc[j]);
                }
            }
            if (abc[max] * abc[max] == x)
                pita[i] = 2; //right
            else pita[i] = 1; //wrong
        }


        for (int i = 0; i < pita.length; i++) {
            if (pita[i] == 2)
                System.out.println("right");
            else if (pita[i] == 1)
                System.out.println("wrong");
            else break;
        }
    }
}
