import java.util.*;
class Practice5 {
static int[] solve(String s) {
  // TODO: implement without looking at the reference.
  return new int[0];
}
public static void main(String[] args) {
check(Arrays.equals(solve("ababaca"),new int[]{0,0,1,2,3,0,1}));check(Arrays.equals(solve("aaaa"),new int[]{0,1,2,3}));check(Arrays.equals(solve("abc"),new int[]{0,0,0}));check(solve("").length==0);
System.out.println("All listed checks passed");
}
static void check(boolean ok){if(!ok)throw new AssertionError("A listed check failed");}
}
