from pathlib import Path
import subprocess,tempfile
r=Path(__file__).resolve().parents[1];ref=(r/'assets/Algorithms.java').read_text().replace('public class Algorithms','class Algorithms');ref=ref[ref.index('/**'):]
bodies=[
'int[] a=input.clone();Algorithms.mergeSort(a);return a;',
'Algorithms.DSU d=new Algorithms.DSU(n);int count=n;for(int[] e:edges)if(d.union(e[0],e[1]))count--;return count;',
'List<List<Algorithms.Edge>> g=new ArrayList<>();for(int i=0;i<n;i++)g.add(new ArrayList<>());for(int[] e:edges){g.get(e[0]).add(new Algorithms.Edge(e[1],e[2]));g.get(e[1]).add(new Algorithms.Edge(e[0],e[2]));}return Algorithms.prim(g,0).stream().mapToLong(Algorithms.Pick::weight).sum();',
'List<List<Integer>> g=new ArrayList<>();for(int i=0;i<n;i++)g.add(new ArrayList<>());for(int[] e:edges)g.get(e[0]).add(e[1]);return (int)Arrays.stream(Algorithms.kosaraju(g)).distinct().count();',
'return Algorithms.editDistance(a,b);','return Algorithms.prefix(s);',
'long h=0;for(char c:s.toCharArray())h=(h*31+c-\'a\'+1)%1000000007;return h;',
'return Algorithms.kasai(s,sa);']
import json
for task,body in zip(json.loads((r/'tasks.json').read_text()),bodies):
 src=(r/f'assets/practice/Practice{task["id"]}.java').read_text().replace(task['starter'],task['signature']+'{'+body+'}')+'\n'+ref
 with tempfile.TemporaryDirectory() as d:
  p=Path(d)/f'Practice{task["id"]}.java';p.write_text(src)
  c=subprocess.run(['java',str(p)],capture_output=True,text=True)
  assert c.returncode==0,(task['title'],c.stderr)
print('PASS: all eight downloadable Java harnesses with reference adapters.')
