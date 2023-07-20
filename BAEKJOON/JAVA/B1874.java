import java.io.*;
import java.util.ArrayList;

class Sucheck {
    int top = -1;
    int n = 1;
    int[] su;

    Sucheck(int n) {
        su = new int[n];
    }

    public String push() {
        if ((top + 1) >= su.length) {
            return "NO";
        } else {
            su[++top] = n++;
            return "+";
        }
    }

    public String pop() {
        int u = su[top--];
        return "-";
    }

    public int top() {
        if (top == -1) {
            return 0;
        }
        return su[top];
    }
}

public class B1874 {
    //스택 수열
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] num = new int[n];
        Sucheck sc = new Sucheck(n);

        for (int i = 0; i < n; i++) {
            num[i] = Integer.parseInt(br.readLine());
        }

        int idx = 0;
        ArrayList<String> pp = new ArrayList<>();

        while (idx != n) {
            if (sc.top() == num[idx]) { //같으면
                pp.add(sc.pop()); //빼내기
                idx++;
            } else {
                String ans = sc.push();
                if (ans.equals("NO")) {
                    pp.add("NO");
                    break;
                } else {
                    pp.add(ans);
                }
            }
        }

        if (pp.contains("NO"))
            System.out.println("NO");
        else {
            for (String s : pp) {
                System.out.println(s);
            }
        }
    }
}
