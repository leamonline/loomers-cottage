const { readFileSync } = require('node:fs');
const { join } = require('node:path');
const { test, expect } = require('@playwright/test');

test.use({ serviceWorkers: 'block' });

const previewDirectory = join(__dirname, '../lab/p21');
const preview = readFileSync(join(previewDirectory, 'preview.html'), 'utf8');
const component = readFileSync(join(previewDirectory, 'loomers-lab-p21.js'), 'utf8');
const inMemoryPreview = preview.replace(
  '<script src="loomers-lab-p21.js" defer></script>',
  () => `<script>${component}</script>`,
);
const routes = [
  'Home', 'Climate', 'Energy', 'Mokka', 'Security', 'Entertainment',
  'Routines', 'Learning & insights', 'Home Health', 'Settings', 'History & analytics',
];

for (const width of [390, 599, 820, 1280]) {
  for (const colorScheme of ['light', 'dark']) {
    test(`${width}px ${colorScheme}: fixtures, navigation, and offline isolation`, async ({ page }) => {
      await page.setViewportSize({ width, height: 900 });
      await page.emulateMedia({ colorScheme, reducedMotion: 'reduce' });
      const requests = [];
      const errors = [];

      page.on('request', request => requests.push(request.url()));
      page.on('websocket', socket => requests.push(socket.url()));
      page.on('pageerror', error => errors.push(error.message));
      await page.route('**/*', route => route.abort());
      await page.routeWebSocket('**/*', socket => socket.close());
      await page.setContent(inMemoryPreview);

      const preview = page.locator('loomers-lab-p21');
      const scenario = preview.getByRole('combobox', { name: 'Lab scenario' });
      const now = preview.getByRole('region', { name: 'Right Now' });
      const section = preview.getByRole('heading', { level: 1 });
      const dialog = preview.getByRole('dialog');

      await expect(preview).toHaveCSS('color-scheme', colorScheme);
      await expect(scenario.locator('option')).toHaveCount(7);
      await expect(preview.locator('.grid article')).toHaveCount(9);
      await expect(preview.locator('.rooms button')).toHaveCount(6);
      await expect(preview.getByText('Temperature unavailable · Activity clear')).toBeVisible();
      expect(await page.evaluate(() => document.documentElement.scrollWidth)).toBeLessThanOrEqual(width);

      await scenario.selectOption({ label: 'Charging and humid bathroom' });
      await expect(now.getByRole('button', { name: /ventilation/i })).toBeVisible();
      await expect(now.getByRole('button', { name: /charg/i })).toBeVisible();

      await scenario.selectOption({ label: 'Unknown security' });
      await expect(now.getByRole('button', { name: 'Security status incomplete' })).toBeVisible();
      await expect(preview.locator('.grid').getByText('Doors reported locked')).toHaveCount(0);

      await scenario.selectOption({ label: 'Stale vehicle data' });
      await expect(preview.locator('.grid').getByText('Stale vehicle telemetry')).toBeVisible();

      await scenario.selectOption({ label: 'Away with uncertain occupancy' });
      await expect(preview.locator('.grid').getByText('Occupancy uncertain')).toBeVisible();
      await scenario.selectOption({ label: 'Winter night' });
      await expect(preview.locator('.shell')).toHaveAttribute('data-season', 'winter');
      await scenario.selectOption({ label: 'Smoke alert fixture' });
      await expect(now.getByRole('button').first()).toHaveText('Smoke detected');

      const room = preview.locator('.rooms').getByRole('button', { name: /Landing/ });
      await room.click();
      await expect(dialog.getByRole('heading', { name: 'Landing' })).toBeVisible();
      await page.keyboard.press('Escape');
      await expect(dialog).toBeHidden();
      await expect(room).toBeFocused();

      const go = async index => {
        const mobile = width < 600;
        const nav = preview.getByRole('navigation', { name: mobile ? 'Quick navigation' : 'Destinations' });
        let menu = nav;
        if (mobile && index >= 4) {
          await nav.getByRole('button', { name: /More/ }).click();
          menu = dialog;
        }
        await menu.getByRole('button', { name: routes[index], exact: true }).click();
      };

      for (const [index, name] of routes.entries()) {
        if (index === 0) continue;
        await go(index);
        await expect(section).toHaveText(name);
        await expect(section).toBeFocused();
      }

      await go(9);
      await preview.getByRole('checkbox', { name: 'Environmental backgrounds' }).uncheck();
      await expect(preview.locator('.shell')).toHaveAttribute('data-static', 'true');
      await go(0);
      await expect(now.getByRole('button').first()).toHaveText('Smoke detected');
      expect(requests).toEqual([]);
      expect(errors).toEqual([]);
    });
  }
}
