import java.util.*;
class Practice0 {
static int[] solve(int[] input) {
  // TODO: implement without looking at the reference.
  return new int[0];
}
public static void main(String[] args) {
for(int[] a:new int[][]{{},{7},{3,1,3,-2},{9,8,7,6}}){ int[] copy=a.clone(),expected=a.clone();Arrays.sort(expected);check(Arrays.equals(solve(a),expected));check(Arrays.equals(a,copy)); }
System.out.println("All listed checks passed");
}
static void check(boolean ok){if(!ok)throw new AssertionError("A listed check failed");}
}
