import { test, expect } from '@playwright/test';

test.describe('Patient survey page', () => {
  test('should display correct answers and UI elements for "basic_check" form', async ({ page }) => {
    // Arrange
    await page.goto('http://localhost/?patient_id=abc321');
    
    // Act
    await page.getByLabel('form selector').selectOption('basic_check');
    await page.getByRole('cell', { name: 'basic_check' }).click();
    await page.getByRole('button', { name: 'view' }).click();
    
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