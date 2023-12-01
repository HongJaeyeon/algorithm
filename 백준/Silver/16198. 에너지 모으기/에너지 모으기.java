import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;
import static java.lang.Math.max;

public class Main {
    public static int N;
    public static boolean[] visited;
    public static int maxValue = Integer.MIN_VALUE;
    public  static int[] arr;
    public  static boolean[] isRemoved;
    public static ArrayList<Integer> selected = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        visited = new boolean[N];
        visited[0] = true;
        visited[N-1] = true;
        arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < N; i++) {
        }

        int[] selected = new int[N-2];
        recur(0, selected);
        System.out.println(maxValue);
    }
    public static void recur(int depth, int[] selected){
//        System.out.println("depth"+ depth +"selected" + Arrays.toString(selected));
        if (depth == N-2){
            maxValue = max(maxValue, cal(selected));
            return;
        }
        for (int i = 0; i < N; i++) {
            if (visited[i]){
                continue;
            }
            visited[i] = true;
            selected[depth] = i;
            recur(depth+1, selected);
            visited[i] = false;
        }
    }

    public static int cal(int[] selected){ //selected는 index를 담고 있다.
//        System.out.println("cal"+Arrays.toString(selected));
        int sum = 0;
        int[] copy_arr = new int[N];
        isRemoved = new boolean[N];

        for (int i = 0; i < N; i++) {
            copy_arr[i] = arr[i];
        }

        for (int idx: selected) {
            sum += copy_arr[findLeftIdx(idx-1)] * copy_arr[findRightIdx(idx+1)];
            isRemoved[idx] = true;
        }
        return sum;
    }

    public static int findLeftIdx(int idx){
        while(isRemoved[idx]){
            idx--;
        }
        return idx;
    }

    public static int findRightIdx(int idx){
        while(isRemoved[idx]){
            idx++;
        }
        return idx;
    }
}