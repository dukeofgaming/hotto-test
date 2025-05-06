import { test, expect } from '@playwright/test';
// Import Tailwind config to get the brand purple and orange
// @ts-ignore
import tailwindConfig from '../tailwind.config.js';

// Get the purple and font values from the config
const TAILWIND_PURPLE = tailwindConfig.theme.colors.primary.DEFAULT;
const TAILWIND_FONT = tailwindConfig.theme.extend.fontFamily.sans[0].toLowerCase();
const TAILWIND_ORANGE = tailwindConfig.theme.colors.secondary.DEFAULT;

test.describe('Patient survey page', () => {
  test('should display correct answers and UI elements for "basic_check" form', async ({ page }) => {
    // Arrange
    await page.goto('http://localhost/?patient_id=abc321');
    // Act
    await page.getByLabel('form selector').selectOption('basic_check');
    await page.getByRole('cell', { name: 'basic_check' }).click();
    await page.getByRole('button', { name: 'view' }).click();
    // Visual Regression: Take screenshot for manual inspection
    await page.screenshot({ path: __dirname + '/smoke-basic_check.png', fullPage: true });
    // Assert
    await expect(page.getByLabel('submission', { exact: true })).toContainText('basic_check');
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

test.describe('Patient survey page styles', () => {
  test('should apply Tailwind background and font styles to body', async ({ page }) => {
    // Arrange
    await page.goto('http://localhost/?patient_id=abc321');
    // Act
    await page.getByLabel('form selector').selectOption('basic_check');
    await page.getByRole('cell', { name: 'basic_check' }).click();
    await page.getByRole('button', { name: 'view' }).click();
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
    // Style test: check background color matches HottoCare purple
    const bgColor = await page.evaluate(() => getComputedStyle(document.body).backgroundColor);
    // Convert #4B4662 to rgb for assertion
    const rgbPurple = 'rgb(75, 70, 98)';
    expect(bgColor === rgbPurple || bgColor.toLowerCase() === TAILWIND_PURPLE.toLowerCase()).toBeTruthy();
    // Assert computed font family
    const fontFamily = await page.evaluate(() => {
      const style = window.getComputedStyle(document.body);
      return style.fontFamily;
    });
    // Accept any of the configured sans fonts from tailwind config
    expect(fontFamily.toLowerCase()).toMatch(new RegExp(TAILWIND_FONT));

    // Example: check a header or button uses the orange accent (secondary)
    // This assumes you have a .bg-secondary or .text-secondary element in your UI
    const orangeEl = await page.$('.bg-secondary, .text-secondary, .bg-accent, .text-accent');
    if (orangeEl) {
      const orangeBg = await orangeEl.evaluate(el => getComputedStyle(el).backgroundColor);
      const orangeText = await orangeEl.evaluate(el => getComputedStyle(el).color);
      // Accept either background or text being the orange
      const rgbOrange = 'rgb(255, 111, 76)';
      expect([
        orangeBg,
        orangeText
      ].some(color => color === rgbOrange || color.toLowerCase() === TAILWIND_ORANGE.toLowerCase())).toBeTruthy();
    }

    // Helper to check color match (hex or rgb, ignore alpha)
    function colorMatches(actual: string, expectedHex: string, expectedRgb: string) {
      actual = actual.trim().toLowerCase();
      return (
        actual === expectedRgb ||
        actual.startsWith(expectedRgb.replace(')', ', 1)')) || // rgb with alpha 1
        actual === expectedHex.toLowerCase() ||
        actual.includes(expectedHex.slice(1).toLowerCase()) // e.g., #4b4662 in rgb/rgba string
      );
    }
    // Check SurveySubmissionList table header styling
    const tableHeaders = await page.$$('thead th');
    // Debug: Log actual computed header background color
    if (tableHeaders.length > 0) {
      const debugHeaderBg = await tableHeaders[0].evaluate(el => getComputedStyle(el).backgroundColor);
      console.log('[DEBUG] First <th> computed backgroundColor:', debugHeaderBg);
    }
    for (const th of tableHeaders) {
      const headerBg = await th.evaluate(el => getComputedStyle(el).backgroundColor);
      const headerText = await th.evaluate(el => getComputedStyle(el).color);
      // Should use purple bg and white text
      expect(colorMatches(headerBg, TAILWIND_PURPLE, rgbPurple)).toBeTruthy();
      expect(headerText === 'rgb(255, 255, 255)' || headerText === '#fff' || headerText === 'white').toBeTruthy();
    }
    // Check table border and shadow presence
    const table = await page.$('table[aria-label="survey submissions"]');
    if (table) {
      const tableBoxShadow = await table.evaluate(el => getComputedStyle(el).boxShadow);
      const tableBorder = await table.evaluate(el => getComputedStyle(el).borderTopWidth);
      expect(parseFloat(tableBorder)).toBeGreaterThan(0);
      expect(tableBoxShadow).not.toBe('none');
    }

    // Check SurveySubmissionList table is centered and not overflowing
    expect(table).not.toBeNull();
    const tableBox = await table.boundingBox();
    const viewport = page.viewportSize();
    expect(tableBox).not.toBeNull();
    expect(viewport).not.toBeNull();
    // Table should be horizontally centered (allow small tolerance)
    const leftSpace = tableBox.x;
    const rightSpace = viewport.width - (tableBox.x + tableBox.width);
    expect(Math.abs(leftSpace - rightSpace)).toBeLessThanOrEqual(20);
    // Table should be vertically centered (allow small tolerance)
    const topSpace = tableBox.y;
    const bottomSpace = viewport.height - (tableBox.y + tableBox.height);
    expect(Math.abs(topSpace - bottomSpace)).toBeLessThanOrEqual(20);
    // Table should not overflow horizontally
    expect(tableBox.width).toBeLessThanOrEqual(viewport.width);
    // Table columns should not be excessively wide (no column > 400px)
    const ths = await table.$$('th');
    for (const th of ths) {
      const thBox = await th.boundingBox();
      expect(thBox.width).toBeLessThanOrEqual(400);
    }
  });
});