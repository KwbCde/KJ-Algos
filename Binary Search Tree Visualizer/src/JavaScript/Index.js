import {createRoot } from 'react-dom/client';

//Clear existing html
document.body.innerHTML = '<div id="app"></div>';

//render react component
const root = createRoot(document.getElementById('app'));
root.render(<h1>Hello, world</h1>);
