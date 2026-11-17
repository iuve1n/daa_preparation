import java.util.*;
class Practice3 {
static int solve(int n, int[][] edges) {
  // TODO: implement without looking at the reference.
  return n;
}
public static void main(String[] args) {
check(solve(4,new int[][]{{0,1},{1,2},{2,0},{2,3}})==2);check(solve(3,new int[][]{})==3);check(solve(2,new int[][]{{0,1},{1,0}})==1);
System.out.println("All listed checks passed");
}
static void check(boolean ok){if(!ok)throw new AssertionError("A listed check failed");}
}
