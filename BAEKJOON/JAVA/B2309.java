import java.io.*;
import java.util.*;

public class B2309 {
    //일곱 난쟁이
    // 전체 합에서 2개씩 빼는.. 알고리즘
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] height = new int[9];

        int sum=0;
        for(int i=0;i<9;i++){ //난쟁이들 키 합
            height[i] = Integer.parseInt(br.readLine());
            sum+=height[i];
        }

        Loop1:
        for(int i=0;i<7;i++){

            for(int j=i+1;j<9;j++){
                int sum2 = sum;
                sum2 = sum2 - (height[i]+height[j]);

                if(sum2==100){ //해당 i랑 j 빼고 넣기
                    height[i]=0;
                    height[j]=0;

                    Arrays.sort(height);
                    break Loop1;
                }
            }
        }
        for(int k=2;k<9;k++){
            System.out.println(height[k]);
        }

    }
}
