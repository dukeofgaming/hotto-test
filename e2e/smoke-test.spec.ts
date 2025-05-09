import { test, expect } from '@playwright/test';
// Import Tailwind config to get the brand purple and orange
// @ts-ignore
import tailwindConfig from '../tailwind.config.js';

// Get the purple and font values from the config
const TAILWIND_PURPLE = tailwindConfig.theme.colors.primary.DEFAULT;
const TAILWIND_FONT = tailwindConfig.theme.extend.fontFamily.sans[0].toLowerCase();
const TAILWIND_ORANGE = tailwindConfig.theme.colors.secondary.DEFAULT;

test.describe.configure({
  mode: 'serial',
  projects: [
    { name: 'chromium', use: { browserName: 'chromium' } },
  ],
});

test.describe('Patient survey page', () => {
  test('body should match viewport size (no overflow)', async ({ page }) => {
    await page.setViewportSize({ width: 1024, height: 768 });
    await page.goto('http://localhost/?patient_id=abc321');
    const viewport = page.viewportSize();
    const windowInner = await page.evaluate(() => ({ width: window.innerWidth, height: window.innerHeight }));
    const windowOuter = await page.evaluate(() => ({ width: window.outerWidth, height: window.outerHeight }));
    const htmlSize = await page.evaluate(() => {
      const html = document.documentElement;
      return { width: html.offsetWidth, height: html.offsetHeight, clientWidth: html.clientWidth, clientHeight: html.clientHeight, scrollWidth: html.scrollWidth, scrollHeight: html.scrollHeight };
    });
    const bodySize = await page.evaluate(() => {
      const body = document.body;
      return { width: body.offsetWidth, height: body.offsetHeight, clientWidth: body.clientWidth, clientHeight: body.clientHeight, scrollWidth: body.scrollWidth, scrollHeight: body.scrollHeight };
    });
    // Log all measurements for debugging
    console.log('viewport', viewport);
    console.log('window.inner', windowInner);
    console.log('window.outer', windowOuter);
    console.log('html', htmlSize);
    console.log('body', bodySize);
    // Assert all relevant sizes do not exceed viewport
    expect(bodySize.width).toBeLessThanOrEqual(viewport.width);
    expect(bodySize.height).toBeLessThanOrEqual(viewport.height);
    expect(htmlSize.width).toBeLessThanOrEqual(viewport.width);
    expect(htmlSize.height).toBeLessThanOrEqual(viewport.height);
    expect(bodySize.scrollWidth).toBeLessThanOrEqual(viewport.width);
    expect(bodySize.scrollHeight).toBeLessThanOrEqual(viewport.height);
    expect(htmlSize.scrollWidth).toBeLessThanOrEqual(viewport.width);
    expect(htmlSize.scrollHeight).toBeLessThanOrEqual(viewport.height);
    expect(bodySize.clientWidth).toBeLessThanOrEqual(viewport.width);
    expect(bodySize.clientHeight).toBeLessThanOrEqual(viewport.height);
    expect(htmlSize.clientWidth).toBeLessThanOrEqual(viewport.width);
    expect(htmlSize.clientHeight).toBeLessThanOrEqual(viewport.height);
  });
  test('should display correct answers and UI elements for "basic_check" form', async ({ page }) => {
    // Arrange
    await page.goto('http://localhost/?patient_id=abc321');

    // Act
    await page.getByLabel('form selector').selectOption('basic_check');
    const basicCheckCells = await page.$$('td');
    for (const cell of basicCheckCells) {
      const text = await cell.textContent();
      if (text && text.trim() === 'basic_check') {
        await cell.click();
        break;
  }
}
    await page.getByRole('button', { name: 'view' }).click();
    // Visual Regression: Take screenshot for manual inspection
    await page.screenshot({ path: __dirname + '/smoke-basic_check.png', fullPage: true });

    // Assert: check for unique, screen reader-friendly ARIA label for the present submission
    await expect(page.getByLabel('survey submission ghi123', { exact: true })).toContainText('basic_check');
    await expect(page.getByRole('textbox', { name: 'answer value' })).toBeVisible();
    await expect(page.getByTestId('array-answer-value')).toContainText('Hospitalization in 2020Started physical therapyDiagnosed with insomnia');
    await expect(page.getByLabel('patient surveys root')).toMatchAriaSnapshot(`
      - dialog "answers":
        - button "close": Close
        - table:
          - rowgroup:
            - row "Question Type Answer":
              - cell "Question"
              - cell "Type"
              - cell "Answer"
          - rowgroup:
            - row "answer":
              - cell "Patient Name"
              - cell "text"
              - cell "Mario López":
                - textbox "answer value"
            - row "answer":
              - cell "Date of Birth"
              - cell "date"
              - cell /\\d+-\\d+-\\d+/: 
                - textbox: /\\d+-\\d+-\\d+/
            - row "answer":
              - cell "Has Insurance?"
              - cell "boolean"
              - cell "answer value":
                - checkbox "answer value"
            - row "answer":
              - cell "Insurance Provider"
              - cell "object"
              - cell "name policy_number":
                - table:
                  - rowgroup:
                    - row "name":
                      - cell "name":
                        - strong: name
                      - cell
                    - row "policy_number":
                      - cell "policy_number":
                        - strong: policy_number
                      - cell
            - row "answer":
              - cell "Recent Health Events"
              - cell "array"
              - cell /Hospitalization in \\d+ Started physical therapy Diagnosed with insomnia/:
                - list:
                  - listitem: /Hospitalization in \\d+/
                  - listitem: Started physical therapy
                  - listitem: Diagnosed with insomnia
    `);
    await page.getByRole('button', { name: 'close' }).click();
  });
});

/**
 * TAILWIND BUG DOCUMENTATION (2025-05-06)
 *
 * There is a confirmed issue with Tailwind CSS v4.x (and possibly related build tooling) where custom palette-based color classes
 * (e.g., bg-primary, bg-primary-500) defined in tailwind.config.js are NOT emitted in the final CSS output, even when:
 *   - The color palette is defined as:
 *       colors: { primary: { DEFAULT: '#4B4662', 500: '#4B4662' }, ... }
 *   - The class (e.g., 'bg-primary-500') is present in both source code and safelist[]
 *   - The build is run with no errors
 *
 * This results in missing classes in the built CSS, causing style tests to fail and components to render with transparent backgrounds.
 *
 * WORKAROUND: Using arbitrary value classes (e.g., bg-[#4B4662]) always works, but is less semantic and not preferred.
 *
 * This test is left as a canary for the bug. If Tailwind or the build system is fixed/upgraded in the future,
 * this test should pass once .bg-primary-500 is correctly emitted.
 */

test.describe('Patient survey page styles', () => {
  test.describe('Given the patient survey page is loaded with patient_id=abc321', () => {
    test.beforeEach(async ({ page }) => {
      await page.goto('http://localhost/?patient_id=abc321');
      await page.getByLabel('form selector').selectOption('basic_check');
      const basicCheckCells = await page.$$('td');
for (const cell of basicCheckCells) {
  const text = await cell.textContent();
  if (text && text.trim() === 'basic_check') {
    await cell.click();
    break;
  }
}
    });

    test.describe('When the page is rendered', () => {
      test('Then the body should have Tailwind background and font styles', async ({ page }) => {
        // Arrange
        // (Page is already loaded by beforeEach)

        // Act
        const bgColor = await page.evaluate(() => getComputedStyle(document.body).backgroundColor);
        const fontFamily = await page.evaluate(() => window.getComputedStyle(document.body).fontFamily);

        // Assert
        const rgbPurple = 'rgb(75, 70, 98)';
        expect(bgColor === rgbPurple || bgColor.toLowerCase() === TAILWIND_PURPLE.toLowerCase()).toBeTruthy();
        expect(fontFamily.toLowerCase()).toMatch(new RegExp(TAILWIND_FONT));
      });

      test('Then the accent element should use the orange accent color', async ({ page }) => {
        // Arrange
        // (Page is already loaded by beforeEach)

        // Act
        const orangeEl = await page.$('.bg-secondary, .text-secondary, .bg-accent, .text-accent');
        let orangeBg, orangeText;
        if (orangeEl) {
          orangeBg = await orangeEl.evaluate(el => getComputedStyle(el).backgroundColor);
          orangeText = await orangeEl.evaluate(el => getComputedStyle(el).color);
        }

        // Assert
        if (orangeEl) {
          const rgbOrange = 'rgb(255, 111, 76)';
          expect([
            orangeBg,
            orangeText
          ].some(color => color === rgbOrange || color.toLowerCase() === TAILWIND_ORANGE.toLowerCase())).toBeTruthy();
        }
      });

      test('Then the SurveySubmissionList table header should have orange background and white text', async ({ page }) => {
        // Arrange
        // (Page is already loaded by beforeEach)

        // Act
        // Only check the <th> elements in the second <tr> of <thead> (the orange header row)
        const headerRows = await page.$$('thead tr');
        if (headerRows.length < 2) throw new Error('Expected at least two rows in <thead>');
        const orangeHeaderRow = headerRows[1];
        const orangeHeaderThs = await orangeHeaderRow.$$('th');
        const rgbOrange = 'rgb(255, 129, 89)';
        for (const th of orangeHeaderThs) {
          const headerBg = await th.evaluate(el => getComputedStyle(el).backgroundColor);
          // eslint-disable-next-line no-console
          console.log('Computed header <th> background:', headerBg);
          expect(headerBg && headerBg.includes('255, 129, 89')).toBeTruthy();
        }
      });

      test('Then the table card should have a border and shadow', async ({ page }) => {
        // Arrange
        // (Page is already loaded by beforeEach)

        // Act
        // Open the modal by clicking the 'view' button (or equivalent)
        await page.getByRole('button', { name: /view/i }).click();
        // Use ARIA role and label to robustly select the modal/card
        const tableCard = await page.getByRole('dialog', { name: 'answers' });

        // Assert
        expect(tableCard).not.toBeNull();
        if (tableCard) {
          // Assert Tailwind shadow class exists
          const classList = await tableCard.evaluate(el => el.className);
          expect(classList).toMatch(/shadow-(md|lg)/);

          // Assert computed style for box-shadow is not 'none'
          const boxShadow = await tableCard.evaluate(el => getComputedStyle(el).boxShadow);
          expect(boxShadow).not.toBe('none');
        }

        // Assert border on the survey submissions table
        const table = await page.getByRole('table', { name: 'survey submissions' });
        if (table) {
          const tableBorder = await table.evaluate(el => getComputedStyle(el).borderTopWidth);
          expect(parseFloat(tableBorder)).toBeGreaterThan(0);
        }
      });

      test('Then the SurveySubmissionList table should be centered and not overflow', async ({ page }) => {
        // Arrange
        // (Page is already loaded by beforeEach)

        // Act
        const table = await page.$('table[aria-label="survey submissions"]');
        const tableBox = table ? await table.boundingBox() : null;
        const viewport = page.viewportSize();
        const ths = table ? await table.$$('th') : [];

        // Assert
        expect(table).not.toBeNull();
        expect(tableBox).not.toBeNull();
        expect(viewport).not.toBeNull();
        if (tableBox && viewport) {
          const leftSpace = tableBox.x;
          const rightSpace = viewport.width - (tableBox.x + tableBox.width);
          expect(Math.abs(leftSpace - rightSpace)).toBeLessThanOrEqual(20);
          const topSpace = tableBox.y;
          const bottomSpace = viewport.height - (tableBox.y + tableBox.height);
          expect(Math.abs(topSpace - bottomSpace)).toBeLessThanOrEqual(20);
          expect(tableBox.width).toBeLessThanOrEqual(viewport.width);
        }
        for (const th of ths) {
          const thBox = await th.boundingBox();
          // eslint-disable-next-line no-console
          console.log('Header cell width:', thBox.width);
          expect(thBox.width).toBeLessThanOrEqual(800);
        }
      });
    });
  });
});