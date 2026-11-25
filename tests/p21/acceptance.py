from pathlib import Path
from playwright.sync_api import sync_playwright
import json
root=Path(__file__).resolve().parents[2] / 'lab' / 'p21'
results=[]
with sync_playwright() as p:
 b=p.chromium.launch()
 for width,height in [(320,700),(390,844),(768,1024),(1280,800)]:
  for dark in ['light','dark']:
   page=b.new_page(viewport={'width':width,'height':height},color_scheme=dark,reduced_motion='reduce',service_workers='block')
   errors=[]; requests=[]; page.on('pageerror',lambda e:errors.append(str(e)));page.on('request',lambda r:requests.append(r.url))
   page.route('**/*', lambda route: route.abort())
   page.route_web_socket('**/*', lambda socket: socket.close())
   page.on('websocket', lambda socket: requests.append(socket.url))
   page.set_content((root/'preview.html').read_text().replace('<script src="loomers-lab-p21.js" defer></script>', '<script>'+ (root/'loomers-lab-p21.js').read_text() + '</script>')); host=page.locator('loomers-lab-p21'); sel=host.get_by_label('Lab scenario'); sel.wait_for()
   def check(name,ok):
    results.append({'viewport':width,'mode':dark,'test':name,'pass':bool(ok)})
   check('nine grouped permanent widgets',host.locator('.grid .tile').count()==9)
   check('six room cards',host.locator('.rooms button').count()==6)
   check('no horizontal overflow',page.evaluate('document.documentElement.scrollWidth <= innerWidth'))
   sel.select_option('charging');check('concurrent charging and ventilation',host.locator('[aria-label="Right Now"]').inner_text().find('Charging active')>=0 and 'Bathroom ventilation recommended' in host.locator('[aria-label="Right Now"]').inner_text())
   sel.select_option('security');check('incomplete security', 'Status incomplete' in host.locator('.grid').inner_text())
   sel.select_option('stale');check('stale vehicle age', '2 hours' in host.locator('.grid').inner_text())
   sel.select_option('smoke');check('smoke priority',host.locator('[aria-label="Right Now"] button').first.inner_text()=='Smoke detected')
   sel.select_option('away');check('uncertain occupancy','Occupancy uncertain' in host.locator('.grid').inner_text())
   sel.select_option('morning');
   first=host.locator('.grid .tile button').first;first.click();check('detail modal opens',host.locator('dialog').is_visible());page.keyboard.press('Escape');check('escape closes',not host.locator('dialog').is_visible());check('focus return',host.evaluate('(e)=>e.shadowRoot.activeElement===e.shadowRoot.querySelector(".grid .tile button")'))
   if width<600:
    host.get_by_role('button',name='⋯ More').click();host.locator('dialog').get_by_role('button',name='Settings',exact=True).click()
   else: host.locator('.sidebar').get_by_role('button',name='Settings',exact=True).click()
   check('settings reachable',host.locator('h1').inner_text()=='Settings');host.get_by_label('Environmental backgrounds').uncheck();check('static atmosphere setting',host.locator('.shell').get_attribute('data-static')=='true')
   check('no external network',not requests);check('no runtime errors',not errors)
   page.close()
 b.close()
failures = [result for result in results if not result['pass']]
print(f'{len(results) - len(failures)}/{len(results)} passed')
if failures:
 raise SystemExit(json.dumps(failures, indent=2))
