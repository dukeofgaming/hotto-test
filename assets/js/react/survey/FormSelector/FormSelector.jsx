import React from "react";

function FormSelector({ forms, selectedFormId, onSelect }) {
  return (
    <select
      data-testid="form-selector"
      value={selectedFormId || ""}
      onChange={e => onSelect && onSelect(e.target.value)}
    >
      <option value="">Show all forms</option>
      {forms.map(form => (
        <option key={form.id} value={form.id}>
          {form.id}
        </option>
      ))}
    </select>
  );
}

export default FormSelector;
