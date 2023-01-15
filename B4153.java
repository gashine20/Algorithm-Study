import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B4153 {
    //기하 - 직각삼각형
    //마지막 줄은 0 0 0 입력으로 파악
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[][] len = new int[30000][3];
        int l;
        do{ //0이 아닐 때까지
            l = Integer.parseInt(st.nextToken());
            for(int i =0;i<3;i++){
                for(int j=0;j<3;j++){
                    len[i][j] = l; //입력 받기
                }
            }
        }while(l!=0);

        System.out.println(len.length);
//        for(int i=0;i<len.length;i++){
//
//        }

    }
}
