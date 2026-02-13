import { useState } from 'react';
import Proposal from './components/Proposal';
import Sunflower from './components/Sunflower';
import './App.css';

function App() {
  const [accepted, setAccepted] = useState(false);

  return (
    <div className="app-container">
      {!accepted ? (
        <Proposal onAccept={() => setAccepted(true)} />
      ) : (
        <Sunflower />
      )}
    </div>
  );
}

export default App;
