import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B2630 {
    //색종이 만들기
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int M = N;
        int[][] square = new int[N][N];

        for(int i=0;i<N;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0;j<N;j++){
                square[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        //N이 2의 몇승 인지
        int q =0;
        while(N!=0){
            N/=2;
            q++; //4
        }

        int white=0, blue=0;

//        for(int i=0;i<q;i++){ //최대 4번까지 가능
//
//
//        }
//
//        for(int i=0;i<N;i++){
//            for(int j=0;j<M;j++){
//                if(square[i][j] ==0){
//
//                }
//
//            }
//        }

//        for(int i=0;i<N/2;i++){ //1~4, 5~8
//            for(int j=0;j<M/2;j++){ //1~4, 5~8
//                if(square[i][j] ==0){
//
//                }
//
//            }
//        }


    }
}
