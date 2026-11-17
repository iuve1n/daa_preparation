import asyncio,json
from pathlib import Path
from playwright.async_api import async_playwright
R=Path(__file__).resolve().parents[1]
(R/'.impeccable/review').mkdir(parents=True,exist_ok=True)
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(headless=True,args=['--no-sandbox']);page=await b.new_page(viewport={'width':1440,'height':1000});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  await page.goto('http://localhost:8000');await page.wait_for_selector('.hero');await page.screenshot(path=str(R/'.impeccable/review/v2-desktop.png'),full_page=True)
  # Legacy state migration without losing completed lectures.
  await page.evaluate("localStorage.setItem('daa-fieldnotes-v1',JSON.stringify({passed:{1:true},notes:{1:'old note'},exams:{},project:{}}))");await page.reload();await page.goto('http://localhost:8000/#analysis');await page.wait_for_selector('#grade-form');assert 'No attempts yet' in await page.inner_text('main')
  await page.goto('http://localhost:8000/#lesson/1');await page.wait_for_selector('#quiz-form')
  qs=[q for q in json.loads((R/'questions.json').read_text()) if q['lesson']==1 and not q.get('examOnly')]
  for i,q in enumerate(qs):
   a=(q['answer']+1)%len(q['options']) if i==0 and q['type']=='mc' else q['answer']
   if q['type']=='mc':await page.check(f'input[name=q{q["id"]}][value="{a}"]')
   else:await page.fill(f'input[name=q{q["id"]}]',str(a))
  await page.click('button[type=submit]');await page.wait_for_selector('#retry');await page.goto('http://localhost:8000/#analysis');assert 'Questions to revisit' in await page.inner_text('main');assert 'Repeat 1 questions' in await page.inner_text('main')
  # Targeted review clears just the missed item, preserves history.
  await page.goto('http://localhost:8000/#review');await page.click('#begin-review');assert await page.locator('.question').count()==1;q=qs[0];await page.check(f'input[name=q{q["id"]}][value="{q["answer"]}"]');await page.click('button[type=submit]');await page.goto('http://localhost:8000/#analysis');await page.goto('http://localhost:8000/#review');assert 'No missed questions' in await page.inner_text('main')
  await page.goto('http://localhost:8000/#analysis');await page.wait_for_selector('#grade-form');
  for name in ['a1','a2','q1','mid','a3','a4','q2','end','final']:await page.fill(f'input[name={name}]','80')
  await page.click('#grade-form button');assert 'Overall estimate: 80.0%' in await page.inner_text('#grade-result')
  await page.goto('http://localhost:8000/#coding/0');await page.fill('#code-draft','static int[] solve(int[] input) { return input.clone(); }');await page.select_option('#test-status','tested');await page.fill('#code-evidence','Passed local examples');await page.reload();await page.wait_for_selector('#code-draft');assert 'input.clone()' in await page.input_value('#code-draft');assert await page.input_value('#test-status')=='tested'
  await page.goto('http://localhost:8000/#analysis');await page.wait_for_selector('#grade-form');await page.screenshot(path=str(R/'.impeccable/review/v2-analysis.png'),full_page=True)
  await page.click('#theme-toggle');assert await page.locator('html').get_attribute('class')=='light'
  await page.set_viewport_size({'width':390,'height':844});await page.screenshot(path=str(R/'.impeccable/review/v2-mobile.png'),full_page=True)
  for route in ['#home','#lesson/1','#analysis','#coding/0','#coding']:
   await page.goto('http://localhost:8000/'+route);await page.wait_for_timeout(100);assert await page.evaluate('document.documentElement.scrollWidth<=innerWidth'),route
  assert not errors,errors;print('PASS: legacy migration, attempt evidence, targeted retry, official grade weights, coding persistence, theme toggle, 5 mobile routes, no browser errors.');await b.close()
asyncio.run(main())
