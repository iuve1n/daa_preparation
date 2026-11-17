import java.util.*;
class Practice6 {
static long solve(String s) {
  // TODO: implement without looking at the reference.
  return 0L;
}
public static void main(String[] args) {
check(solve("")==0);check(solve("a")==1);check(solve("ab")==33);check(solve("abc")==1026);
System.out.println("All listed checks passed");
}
static void check(boolean ok){if(!ok)throw new AssertionError("A listed check failed");}
}
