import './App.css';
import ApiGet from './apiGet'
import {BrowserRouter, Route, Routes} from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          {/* Home */}
          <Route exact path="/" element={<ApiGet />}/>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
