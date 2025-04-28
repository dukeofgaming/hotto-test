import React from 'react';
import { createRoot } from 'react-dom/client';
import Hello from './Hello';

const name = window.REACT_PROPS;
const root = createRoot(document.getElementById('react-root'));
root.render(<Hello name={name} />);
