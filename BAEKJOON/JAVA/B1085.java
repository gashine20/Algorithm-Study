import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B1085 {
    //기하 - 직사각형에서 탈출
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());
        int width=x, height=y; //높이, 너비 더 짧은거 계산

        if(width > (w-x))
            width = w-x;

        if(height > (h-y))
            height = h-y;

        if(width<height)
            System.out.println(width);
        else System.out.println(height);
    }
}
