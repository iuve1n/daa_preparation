import java.util.*;
class Practice2 {
static long solve(int n, int[][] edges) {
  // TODO: implement without looking at the reference.
  return 0L;
}
public static void main(String[] args) {
check(solve(4,new int[][]{{0,1,2},{0,2,3},{1,2,1},{1,3,4},{2,3,5}})==7);check(solve(1,new int[][]{})==0);check(solve(2,new int[][]{{0,1,-3}})==-3);boolean threw=false;try{solve(3,new int[][]{{0,1,1}});}catch(IllegalArgumentException e){threw=true;}check(threw);
System.out.println("All listed checks passed");
}
static void check(boolean ok){if(!ok)throw new AssertionError("A listed check failed");}
}
