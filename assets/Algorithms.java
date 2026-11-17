import java.util.*;

/** Java 17 reference implementations. Graph vertices are 0..n-1.
 * Compile: javac Algorithms.java; run: java Algorithms
 * String indexing uses Java UTF-16 code units. */
public class Algorithms {
  public static void mergeSort(int[] a) { merge(a,0,a.length,new int[a.length]); }
  private static void merge(int[] a,int l,int r,int[] t) {
    if(r-l<=1)return; int m=(l+r)>>>1;
    merge(a,l,m,t);merge(a,m,r,t);int i=l,j=m;
    for(int k=l;k<r;k++)t[k]=j==r||(i<m&&a[i]<=a[j])?a[i++]:a[j++];
    System.arraycopy(t,l,a,l,r-l);
  }
  public static class DSU {
    int[] p,size;
    public DSU(int n){p=new int[n];size=new int[n];for(int i=0;i<n;i++){p[i]=i;size[i]=1;}}
    public int find(int x){while(x!=p[x]){p[x]=p[p[x]];x=p[x];}return x;}
    public boolean union(int a,int b){a=find(a);b=find(b);if(a==b)return false;
      if(size[a]<size[b]){int t=a;a=b;b=t;}p[b]=a;size[a]+=size[b];return true;}
  }
  /** Iterative first pass preserves exit order without Java recursion depth limits. */
  public static int[] kosaraju(List<List<Integer>> g) {
    int n=g.size();List<List<Integer>> rev=new ArrayList<>();
    for(int i=0;i<n;i++)rev.add(new ArrayList<>());
    for(int v=0;v<n;v++)for(int u:g.get(v))rev.get(u).add(v);
    boolean[] seen=new boolean[n];List<Integer> order=new ArrayList<>();
    for(int root=0;root<n;root++)if(!seen[root]){
      Deque<int[]> st=new ArrayDeque<>();st.push(new int[]{root,0});seen[root]=true;
      while(!st.isEmpty()){
        int[] f=st.peek();int v=f[0];
        if(f[1]<g.get(v).size()){
          int u=g.get(v).get(f[1]++);
          if(!seen[u]){seen[u]=true;st.push(new int[]{u,0});}
        }else{order.add(v);st.pop();}
      }
    }
    int[] comp=new int[n];Arrays.fill(comp,-1);int id=0;
    for(int k=n-1;k>=0;k--){int root=order.get(k);if(comp[root]!=-1)continue;
      Deque<Integer> st=new ArrayDeque<>();st.push(root);comp[root]=id;
      while(!st.isEmpty()){int v=st.pop();for(int u:rev.get(v))if(comp[u]==-1){comp[u]=id;st.push(u);}}
      id++;
    }return comp;
  }
  public record Edge(int to,long weight) {}
  public record Pick(int from,int to,long weight) {}
  /** Lazy Prim for a connected undirected graph; both edge directions must be present.
   * Throws for disconnected input; an empty graph has an empty MST. */
  public static List<Pick> prim(List<List<Edge>> g,int start){
    int n=g.size();List<Pick> result=new ArrayList<>();if(n==0)return result;
    boolean[] used=new boolean[n];int visited=0;
    PriorityQueue<Pick> pq=new PriorityQueue<>(Comparator.comparingLong(Pick::weight));
    pq.add(new Pick(-1,start,0));
    while(!pq.isEmpty()){
      Pick e=pq.remove();int v=e.to();if(used[v])continue;
      used[v]=true;visited++;if(e.from()!=-1)result.add(e);
      for(Edge a:g.get(v))if(!used[a.to()])pq.add(new Pick(v,a.to(),a.weight()));
    }
    if(visited!=n)throw new IllegalArgumentException("Graph is disconnected");
    return result;
  }
  public static int editDistance(String a,String b){
    int[][] d=new int[a.length()+1][b.length()+1];
    for(int i=0;i<=a.length();i++)d[i][0]=i;
    for(int j=0;j<=b.length();j++)d[0][j]=j;
    for(int i=1;i<=a.length();i++)for(int j=1;j<=b.length();j++)
      d[i][j]=Math.min(d[i-1][j]+1,Math.min(d[i][j-1]+1,d[i-1][j-1]+(a.charAt(i-1)==b.charAt(j-1)?0:1)));
    return d[a.length()][b.length()];
  }
  public static int[] prefix(String s){int[] pi=new int[s.length()];
    for(int i=1;i<s.length();i++){int j=pi[i-1];while(j>0&&s.charAt(i)!=s.charAt(j))j=pi[j-1];
      if(s.charAt(i)==s.charAt(j))j++;pi[i]=j;}return pi;
  }
  /** Polynomial hash with high-order leading symbol; fixed safe constants. */
  public static class RollingHash {
    static final long MOD=1_000_000_007L, BASE=911382323L;
    long[] h,p;
    public RollingHash(String s){h=new long[s.length()+1];p=new long[s.length()+1];p[0]=1;
      for(int i=0;i<s.length();i++){p[i+1]=p[i]*BASE%MOD;h[i+1]=(h[i]*BASE+s.charAt(i)+1)%MOD;}}
    /** Hash of [l,r). Equal hashes still require verification for exact equality. */
    public long hash(int l,int r){if(l<0||l>r||r>=h.length)throw new IndexOutOfBoundsException();
      return (h[r]-h[l]*p[r-l]%MOD+MOD)%MOD;}
  }
  /** Comparison-sort prefix doubling, O(n log^2 n), not the radix-sort variant. */
  public static int[] suffixArray(String s){
    int n=s.length();Integer[] order=new Integer[n];int[] ranks=new int[n];
    for(int i=0;i<n;i++){order[i]=i;ranks[i]=s.charAt(i);}
    for(int k=1;k<n;k*=2){final int gap=k;final int[] r=ranks;
      Arrays.sort(order,(a,b)->{int c=Integer.compare(r[a],r[b]);return c!=0?c:
        Integer.compare(a+gap<n?r[a+gap]:-1,b+gap<n?r[b+gap]:-1);});
      int[] next=new int[n];
      for(int i=1;i<n;i++){int a=order[i-1],b=order[i];
        boolean different=r[a]!=r[b]||(a+k<n?r[a+k]:-1)!=(b+k<n?r[b+k]:-1);
        next[b]=next[a]+(different?1:0);}
      ranks=next;if(ranks[order[n-1]]==n-1||k>n/2)break;
    }
    return Arrays.stream(order).mapToInt(Integer::intValue).toArray();
  }
  /** LCP[0]=0; LCP[r] compares SA[r] to SA[r-1]. */
  public static int[] kasai(String s,int[] sa){int n=s.length(),h=0;int[] rank=new int[n],lcp=new int[n];
    for(int r=0;r<n;r++)rank[sa[r]]=r;
    for(int i=0;i<n;i++){int r=rank[i];if(r==0){h=0;continue;}int j=sa[r-1];
      while(i+h<n&&j+h<n&&s.charAt(i+h)==s.charAt(j+h))h++;
      lcp[r]=h;if(h>0)h--;}
    return lcp;
  }
  public static void main(String[] args){
    int[] a={7,2,5,1};mergeSort(a);check(Arrays.equals(a,new int[]{1,2,5,7}));
    DSU d=new DSU(4);check(d.union(0,1)&&d.union(2,3)&&d.union(1,3)&&!d.union(0,2));
    List<List<Integer>> g=List.of(List.of(1),List.of(2),List.of(0,3),List.of());
    int[] c=kosaraju(g);check(c[0]==c[1]&&c[1]==c[2]&&c[2]!=c[3]);
    List<List<Edge>> w=new ArrayList<>();for(int i=0;i<4;i++)w.add(new ArrayList<>());
    for(int[] e:new int[][]{{0,1,2},{0,2,3},{1,2,1},{1,3,4},{2,3,5}}){w.get(e[0]).add(new Edge(e[1],e[2]));w.get(e[1]).add(new Edge(e[0],e[2]));}
    check(prim(w,0).stream().mapToLong(Pick::weight).sum()==7);
    check(editDistance("cat","cut")==1&&editDistance("","abc")==3);
    check(Arrays.equals(prefix("ababaca"),new int[]{0,0,1,2,3,0,1}));
    RollingHash hash=new RollingHash("ababa");check(hash.hash(0,3)==hash.hash(2,5));
    int[] sa=suffixArray("banana");check(Arrays.equals(sa,new int[]{5,3,1,0,4,2}));
    check(Arrays.equals(kasai("banana",sa),new int[]{0,1,3,0,0,2}));
    Random rand=new Random(42);
    for(int trial=0;trial<500;trial++){
      int n=rand.nextInt(30);StringBuilder sb=new StringBuilder();
      for(int i=0;i<n;i++)sb.append((char)('a'+rand.nextInt(4)));String s=sb.toString();
      int[] actual=suffixArray(s);Integer[] ref=new Integer[n];for(int i=0;i<n;i++)ref[i]=i;
      Arrays.sort(ref,Comparator.comparing(s::substring));
      check(Arrays.equals(actual,Arrays.stream(ref).mapToInt(Integer::intValue).toArray()));
      int[] lcp=kasai(s,actual);
      for(int r=1;r<n;r++){int h=0,i=actual[r],j=actual[r-1];while(i+h<n&&j+h<n&&s.charAt(i+h)==s.charAt(j+h))h++;check(lcp[r]==h);}
    }
    System.out.println("Reference checks passed");
  }
  private static void check(boolean ok){if(!ok)throw new AssertionError();}
}
