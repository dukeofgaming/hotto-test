import React from "react";

function FormSelector({ forms = [], selectedFormId, onSelect }) {
  return (
    <select
      aria-label="form selector"
      value={selectedFormId || ""}
      onChange={e => onSelect && onSelect(e.target.value)}
      className="text-black bg-white border border-gray-300 rounded px-2 py-1"
    >
      <option value="" className="text-black bg-white">Show all forms</option>
      {(forms || []).map(form => (
        <option key={form.id} value={form.id} className="text-black bg-white">{form.id}</option>
      ))}
    </select>
  );
}

export default FormSelector;
